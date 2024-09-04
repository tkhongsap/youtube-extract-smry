
import logging
import re
import os
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from datetime import datetime, timedelta
from urllib.parse import urlparse, parse_qs
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Replace with your actual API key

DEVELOPER_KEY = os.getenv('YOUTUBE_API_KEY')
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def clean_filename(filename):
    """Remove or replace characters that are unsafe for filenames."""
    unsafe_chars = r'[<>:"/\\|?*\u0000-\u001F]'
    filename = re.sub(unsafe_chars, '_', filename)
    filename = filename.strip('. ')
    return filename if filename else 'untitled'

def extract_video_id(url):
    """Extract the video ID from various forms of YouTube URLs."""
    parsed_url = urlparse(url)
    if parsed_url.hostname == 'youtu.be':
        return parsed_url.path[1:]
    if parsed_url.hostname in ('www.youtube.com', 'youtube.com'):
        if parsed_url.path == '/watch':
            return parse_qs(parsed_url.query)['v'][0]
        if parsed_url.path.startswith(('/embed/', '/v/')):
            return parsed_url.path.split('/')[2]
    raise ValueError("Invalid YouTube URL")

def sanitize_filename(url):
    """Convert URL to a filename-friendly format with .md extension."""
    try:
        video_id = extract_video_id(url)
        safe_id = clean_filename(video_id)
        return f"youtube_{safe_id}.md"
    except ValueError as e:
        logger.error(f"Error sanitizing filename: {str(e)}")
        return "youtube_transcript.md"  # Fallback filename

def extract_transcript(youtube_url, language='en'):
    """Extract transcript from a YouTube video with fallback options."""
    try:
        video_id = extract_video_id(youtube_url)
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[language])
            logger.info(f"Transcript found in {language}")
            return transcript
        except NoTranscriptFound:
            logger.warning(f"No transcript found for language: {language}. Trying English.")
            try:
                transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
                logger.info("Transcript found in English")
                return transcript
            except NoTranscriptFound:
                logger.warning("No transcript found in English. Trying any available language.")
                transcript = YouTubeTranscriptApi.get_transcript(video_id)
                logger.info("Transcript found in an available language")
                return transcript
    except TranscriptsDisabled:
        logger.error("Transcripts are disabled for this video")
        raise
    except Exception as e:
        logger.exception(f"Error extracting transcript: {str(e)}")
        raise

def format_transcript_as_markdown(transcript, youtube_url):
    """Format the transcript as Markdown."""
    try:
        yt = YouTube(youtube_url)
        md_content = f"# Transcript: {yt.title}\n\n"
        md_content += f"[Watch Video]({youtube_url})\n\n"
        md_content += "| Timestamp | Text |\n|-----------|------|\n"
        for entry in transcript:
            timestamp = f"{int(entry['start'] // 60):02d}:{int(entry['start'] % 60):02d}"
            md_content += f"| {timestamp} | {entry['text']} |\n"
        return md_content
    except Exception as e:
        logger.error(f"Error formatting transcript: {str(e)}")
        raise

def save_transcript_to_file(md_content, filename):
    """Save the Markdown formatted transcript to a file in the output directory."""
    try:
        output_dir = 'output'  # Use the 'output' directory directly

        os.makedirs(output_dir, exist_ok=True)
        
        # Join the output directory path with the filename
        file_path = os.path.join(output_dir, filename)
    
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(md_content)
        logger.info(f"Transcript saved to {file_path}")
        return file_path
    except Exception as e:
        logger.exception(f"Error saving transcript to file: {str(e)}")
        raise

def process_youtube_url(url, language='en'):
    """Main function to process YouTube URL, extract transcript, and save to Markdown file."""
    try:
        filename = sanitize_filename(url)
        transcript = extract_transcript(url, language)
        md_content = format_transcript_as_markdown(transcript, url)
        save_transcript_to_file(md_content, filename)
        return filename
    except Exception as e:
        logger.error(f"Failed to process YouTube URL: {url}. Error: {str(e)}")
        return None

def get_language_code(language):
    """Convert language name to code."""
    language_codes = {
        'english': 'en',
        'french': 'fr',
        'spanish': 'es',
        'thai': 'th',
        'chinese': 'zh',
        'japanese': 'ja'
    }
    return language_codes.get(language.lower(), 'en')

def parse_advanced_query(query):
    """Parse advanced search syntax."""
    terms = query.split()
    include = [term for term in terms if not term.startswith('-') and ':' not in term]
    exclude = [term[1:] for term in terms if term.startswith('-')]
    exact = ' '.join([term.strip('"') for term in query.split('"') if term.strip()])
    return ' '.join(include), ' '.join(exclude), exact

def get_start_date(time_range):
    """Calculate the start date based on the selected time range."""
    now = datetime.now()
    if time_range == '3d':
        return now - timedelta(days=3)
    elif time_range == '7d':
        return now - timedelta(days=7)
    elif time_range == '15d':
        return now - timedelta(days=15)
    elif time_range == '30d':
        return now - timedelta(days=30)
    elif time_range == '3m':
        return now - timedelta(days=90)
    else:  # 'all' or any other value
        return None

def youtube_search(query, max_results=5, order='relevance', time_range='all', channel_id=None):
    """Enhanced YouTube search function with time range support."""
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    # Parse advanced query
    include, exclude, exact = parse_advanced_query(query)
    
    # Construct search query
    search_query = f'"{exact}"' if exact else include
    if exclude:
        search_query += f' -{exclude}'

    try:
        # Prepare search parameters
        search_params = {
            'q': search_query,
            'type': 'video',
            'part': 'id,snippet',
            'maxResults': max_results,
            'order': order
        }

        # Add time range filter
        start_date = get_start_date(time_range)
        if start_date:
            search_params['publishedAfter'] = start_date.isoformat() + 'Z'

        # Add channel filter if provided
        if channel_id:
            search_params['channelId'] = channel_id

        # Execute search
        search_response = youtube.search().list(**search_params).execute()

        videos = []
        for search_result in search_response.get('items', []):
            if search_result['id']['kind'] == 'youtube#video':
                videos.append({
                    'title': search_result['snippet']['title'],
                    'url': f"https://www.youtube.com/watch?v={search_result['id']['videoId']}",
                    'channel': search_result['snippet']['channelTitle'],
                    'publish_date': search_result['snippet']['publishedAt']
                })
        return videos

    except HttpError as e:
        logger.error(f'An HTTP error {e.resp.status} occurred:\n{e.content}')
        return []

if __name__ == "__main__":
    print("Welcome to YouTube Transcript Extractor!")
    print("Type 'quit' or 'bye' to exit the program.")
    
    while True:
        try:
            choice = input("\nEnter '1' to search YouTube or '2' to enter a specific URL (or 'quit' to exit): ").strip()
            if choice.lower() in ['quit', 'bye']:
                print("Thank you for using YouTube Transcript Extractor. Goodbye!")
                break
            
            if choice == '1':
                query = input("Enter your search query: ")
                time_range = input("Select time range (3d, 7d, 15d, 30d, 3m, all): ").lower()
                if time_range not in ['3d', '7d', '15d', '30d', '3m', 'all']:
                    time_range = 'all'
                
                order = input("Select order (date, rating, relevance, title, viewCount): ").lower()
                if order not in ['date', 'rating', 'relevance', 'title', 'viewCount']:
                    order = 'relevance'
                
                channel_id = input("Enter channel ID (optional): ").strip() or None
                
                videos = youtube_search(query, time_range=time_range, order=order, channel_id=channel_id)
                if videos:
                    print("\nSearch results:")
                    for i, video in enumerate(videos, 1):
                        print(f"{i}. {video['title']}")
                        print(f"   Channel: {video['channel']}")
                        print(f"   Published: {video['publish_date']}")
                        print(f"   URL: {video['url']}\n")
                    
                    selection = int(input("Select a video number: ")) - 1
                    youtube_url = videos[selection]['url']
                else:
                    print("No videos found.")
                    continue
            elif choice == '2':
                youtube_url = input("Enter the YouTube URL: ").strip()
            else:
                print("Invalid choice. Please try again.")
                continue
            
            language = input("Enter the language (e.g., English, French, Spanish, Thai, Chinese, Japanese) or press Enter for English: ").strip()
            language_code = get_language_code(language) if language else 'en'
            
            result = process_youtube_url(youtube_url, language_code)
            if result:
                print(f"Transcript saved to {result}")
            else:
                print("Failed to extract and save transcript.")
        except KeyboardInterrupt:
            print("\nProgram interrupted. Exiting...")
            break
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            logger.exception("Unexpected error")
