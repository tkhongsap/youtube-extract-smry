
# YouTube Transcript Extractor and Summarizer

This project provides a set of tools for extracting transcripts from YouTube videos, searching for YouTube videos based on specific criteria, and summarizing video content using the Claude API. The project is divided into three main scripts:

1. `01-youtube-extraction.py`
2. `02-search-youtube-extraction.py`
3. `03-search-extract-summarize-llm.py`

## Requirements

- Python 3.x
- Required Python packages:
  - `pytube`
  - `youtube_transcript_api`
  - `google-api-python-client`
  - `anthropic` (for LLM summarization)
  - `python-dotenv` (for loading environment variables)

## Installation

1. Clone the repository.
2. Install the required packages using pip:

```bash
pip install pytube youtube_transcript_api google-api-python-client anthropic python-dotenv
```

3. Set up your environment variables by creating a `.env` file in the root directory of the project and adding your API keys:

```
YOUTUBE_API_KEY=your_youtube_api_key
CLAUDE_API_KEY=your_claude_api_key
```

## Scripts Overview

### 1. `01-youtube-extraction.py`

This script extracts transcripts from YouTube videos and saves them in Markdown format.

**Usage:**

Run the script and follow the prompts to enter a YouTube URL and the desired language for the transcript. The transcript will be saved as a Markdown file.

### 2. `02-search-youtube-extraction.py`

This script allows users to search for YouTube videos based on specific criteria, extract transcripts, and save them in Markdown format.

**Usage:**

Run the script and follow the prompts to search for YouTube videos, select a video, and specify the language for the transcript. The transcript will be saved as a Markdown file in the `output` directory.

### 3. `03-search-extract-summarize-llm.py`

This script combines the functionality of searching for YouTube videos, extracting transcripts, and summarizing the content using the Claude API. The summaries are formatted for social media posting and saved as Markdown files.

**Usage:**

Run the script and follow the prompts to search for YouTube videos or enter a specific URL. After extracting the transcript, the script will summarize the content and save both the transcript and the summary as Markdown files in the `output` directory.

## Running the Scripts

To run any of the scripts, use the following command:

```bash
python script_name.py
```

Replace `script_name.py` with the name of the script you want to run (e.g., `01-youtube-extraction.py`).

## Example

Here is an example of how to use the `03-search-extract-summarize-llm.py` script:

1. Run the script:

```bash
python 03-search-extract-summarize-llm.py
```

2. Follow the prompts to search for a YouTube video or enter a specific URL.
3. Specify the language for the transcript (default is English).
4. The script will extract the transcript, summarize the content, and save the results in the `output` directory.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgements

- [pytube](https://github.com/pytube/pytube)
- [YouTube Transcript API](https://github.com/jdepoix/youtube-transcript-api)
- [Google API Python Client](https://github.com/googleapis/google-api-python-client)
- [Anthropic](https://www.anthropic.com/)

## Contact

For any questions or inquiries, please contact [Your Name] at [Your Email].
