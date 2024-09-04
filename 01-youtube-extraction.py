import logging
import os
from urllib.parse import urlparse, parse_qs
import re
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Define dark red color using ANSI escape codes
DARK_RED = "\033[31m"
RESET_COLOR = "\033[0m"

def print_markdown_red(text):
    """Print text in Markdown style with dark red color."""
    print(f"{DARK_RED}{text}{RESET_COLOR}")

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
    """Convert YouTube video title to a filename-friendly format with .md extension."""
    try:
        # Extract the video title using pytube
        yt = YouTube(url)
        video_title = yt.title
        safe_title = clean_filename(video_title)
        return f"{safe_title}.md"
    except Exception as e:
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
    """Save the Markdown formatted transcript to a file in the output folder."""
    try:
        # Ensure the output directory exists
        output_dir = os.path.join(os.getcwd(), 'output')
        os.makedirs(output_dir, exist_ok=True)

        # Create the full file path
        file_path = os.path.join(output_dir, filename)

        # Write the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(md_content)
        logger.info(f"Transcript saved to {file_path}")
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

if __name__ == "__main__":
    print_markdown_red("# Welcome to YouTube Transcript Extractor!")
    print_markdown_red("Type 'quit' or 'bye' to exit the program.")
    
    while True:
        try:
            youtube_url = input("\nEnter the YouTube URL (or 'quit' to exit): ").strip()
            if youtube_url.lower() in ['quit', 'bye', 'exit']:
                print_markdown_red("Thank you for using YouTube Transcript Extractor. Goodbye!")
                break
            
            language = input("Enter the language (e.g., English, French, Spanish, Thai, Chinese, Japanese) or press Enter for English: ").strip()
            language_code = get_language_code(language) if language else 'en'
            
            result = process_youtube_url(youtube_url, language_code)
            if result:
                print_markdown_red(f"**Transcript saved to output/{result}**")
            else:
                print_markdown_red("**Failed to extract and save transcript.**")
        except KeyboardInterrupt:
            print_markdown_red("\nProgram interrupted. Exiting...")
            break
        except Exception as e:
            print_markdown_red(f"**An error occurred: {str(e)}**")
            logger.exception("Unexpected error")
