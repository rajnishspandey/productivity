from flask import Flask, render_template
from tools.youtube_transcript import youtube_transcript_bp
from tools.world_clock import world_clock_bp
# Import other tool blueprints as you add them

app = Flask(__name__)

# Register blueprints for different tools
app.register_blueprint(youtube_transcript_bp, url_prefix='/youtube-transcript')
app.register_blueprint(world_clock_bp, url_prefix='/world-clock')

@app.route('/')
def home():
    tools = [
        {
            'name': 'YouTube Transcript',
            'description': 'Get captions from YouTube videos',
            'url': '/youtube-transcript'
        },
        {
            'name': 'World Clock',
            'description': 'Check time across different time zones',
            'url': '/world-clock'
        }
        # Add more tools as you develop them
    ]
    return render_template('home.html', tools=tools)

if __name__ == '__main__':
    app.run(debug=True)