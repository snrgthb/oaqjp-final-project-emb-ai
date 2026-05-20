from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

# Route to serve the main HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the emotion detection request – this is the "application calling function"
@app.route('/emotionDetector')
def emotion_detector_route():
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Call the emotion detection function (no error handling yet)
    result = emotion_detector(text_to_analyze)
    
    # Extract scores and dominant emotion
    anger = result['anger']
    disgust = result['disgust']
    fear = result['fear']
    joy = result['joy']
    sadness = result['sadness']
    dominant = result['dominant_emotion']
    
    # Format output exactly as required
    response_string = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, "
        f"'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant}."
    )
    return response_string

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)