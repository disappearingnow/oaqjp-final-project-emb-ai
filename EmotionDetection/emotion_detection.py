import requests
import json

def emotion_detector(text_to_analyze):
    url='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json={ "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = input_json, headers=headers)
    response_json = json.loads(response.text)
    emotions = response_json["emotionPredictions"][0]["emotion"]

    dominant_emotion = {'name': None, 'score': 0}
    for emotion in emotions:
        if emotions[emotion] > dominant_emotion['score']:
            dominant_emotion['name'] = emotion
            dominant_emotion['score'] = emotions[emotion]

    return {**emotions, 'dominant_emotion': dominant_emotion['name']}







