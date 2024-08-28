"""
This module creates the Flask server
which serves the web app to the user
that takes text input and returns
an emotional analysis of the text
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def home():
    """Renders index.html on the '/' route"""
    return render_template("index.html")

@app.route("/emotionDetector")
def analyze():
    """
    Connects to the emotion detector function with 
    text provided by user and returns appropriate response
    """
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

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
