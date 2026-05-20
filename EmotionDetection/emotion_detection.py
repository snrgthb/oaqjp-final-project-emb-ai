import requests
import json

def emotion_detector(text_to_analyze):
    """
    Sends a text to the Watson NLP emotion detection API and returns the response.

    Args:
        text_to_analyze (str): The text to analyze for emotions.

    Returns:
        dict: A dictionary containing emotion scores and the dominant emotion.
    """
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    response = requests.post(url, json=payload, headers=headers)
    formatted_response = json.loads(response.text)
    emotion_dict = formatted_response["emotionPredictions"][0]["emotion"]
    
    dominant_emotion = None
    max_score = float('-inf')
    for emotion, score in emotion_dict.items():
        if score > max_score:
            max_score = score
            dominant_emotion = emotion
    
    emotion_dict["dominant_emotion"] = dominant_emotion
    return emotion_dict