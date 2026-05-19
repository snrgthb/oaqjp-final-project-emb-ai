import requests

def emotion_detector(text_to_analyze):
    """
    Sends a text to the Watson NLP emotion detection API and returns the response.

    Args:
        text_to_analyze (str): The text to analyze for sentiment.

    Returns:
        str: The raw JSON response from the API.
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
    return response.text