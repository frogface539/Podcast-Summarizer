from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
import re

def extract_video_id(url: str) -> str:
    patterns = [
        r"youtu\.be/([^&\n?#]+)",
        r"youtube\.com/watch\?v=([^&\n?#]+)",
        r"youtube\.com/embed/([^&\n?#]+)",
    ]

    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    raise ValueError("Invalid Youtube URL format..")

def fetch_transcript(video_url: str, lang='en') -> str:
    video_id = extract_video_id(video_url)

    # try:
    #     transcript = YouTubeTranscriptApi.get_transcript(video_id,languages=['en'])
    #     formatter = TextFormatter()
    #     text = formatter.format_transcript(transcript)
    #     return text
    
    # except Exception as e:
    #     raise RuntimeError(f"Failed to fetch transcript: {str(e)}")

    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

        try:
            transcript = transcript_list.find_transcript(['en'])

        except:
            if transcript_list.find_manually_created_transcript(['hi']):
                transcript = transcript_list.find_manually_created_transcript(['hi'])
            else:
                transcript = transcript_list.find_generated_transcript(['hi'])

        transcript_data = transcript.fetch()
        formatter = TextFormatter()
        return formatter.format_transcript(transcript_data)
    
    except Exception as e:
        raise RuntimeError(f"Failed to fetch transcript: \n{str(e)}")
    
## Testing 
if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=Im-lOY5s5UM"
    try:
        transcript = fetch_transcript(url)
        print("\n ---- Transcript Sample --- \n")
        print(transcript)

    except Exception as e:
        print(e)