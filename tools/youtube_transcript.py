from flask import Blueprint, render_template, request
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs

youtube_transcript_bp = Blueprint('youtube_transcript', __name__)

def get_video_id(url):
    parsed_url = urlparse(url)
    
    if parsed_url.netloc == 'youtu.be':
        return parsed_url.path[1:].split('?')[0]
    
    return parse_qs(parsed_url.query).get('v', [None])[0]

def get_available_languages(video_id):
    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        return {t.language_code: t.language for t in transcript_list}
    except Exception as e:
        return {}

def get_lyrics(video_id, language_code):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[language_code])
        lyrics = '\n'.join(entry['text'] for entry in transcript)
        return lyrics
    except Exception as e:
        return f"An error occurred: {str(e)}"

@youtube_transcript_bp.route('/', methods=['GET', 'POST'])
def transcript():
    transcript = None
    available_languages = {}
    error = None

    if request.method == 'POST':
        url = request.form.get('youtube_url')
        video_id = get_video_id(url)

        if not video_id:
            error = "Invalid YouTube URL"
        else:
            available_languages = get_available_languages(video_id)
            
            if not available_languages:
                error = "No captions available for this video."
            else:
                # Default to first available language if not specified
                selected_language = list(available_languages.keys())[0]
                transcript = get_lyrics(video_id, selected_language)

    return render_template('youtube_transcript.html', 
                           transcript=transcript, 
                           available_languages=available_languages,
                           error=error)