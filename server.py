from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/emotionDetector")
def analyze():
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    
    anger = f"'anger': {response['anger']}"
    disgust = f"'disgust': {response['disgust']}"
    fear = f"'fear': {response['fear']}"
    joy = f"'joy': {response['joy']}"
    sadness = f"'sadness': {response['sadness']}"
    dominant_emotion = response['dominant_emotion']

    response_string = f"""
    For the given statement, the system response is 
    {anger}, {disgust}, {fear}, {joy}, {sadness}.
    The dominant emotion is {dominant_emotion}
    """

    return response_string

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)