"""
This module defines the `emotion_detector` function
"""
import json
import requests

def emotion_detector(text_to_analyze):
    """
    This function sends the input text to Watson's NLP API
    """
    url = (
    'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/'
    'NlpService/EmotionPredict'
    )
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header, timeout=20)
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        emotion_scores = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        emotion_scores['dominant_emotion']=dominant_emotion
    elif response.status_code == 400:
        emotion_scores = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    return emotion_scores
