import requests
import json

def emotion_detector(text_to_analyze):
    # Define the URL and headers
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    # Prepare the input JSON
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Send POST request to the Watson API
    response = requests.post(url, headers=headers, json=payload)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Convert the response text into a dictionary
        response_data = response.json()

        emotion_predictions = response_data['emotionPredictions'][0]['emotion']
        
        # Extract the required emotions and their scores
        emotions = emotion_predictions.get('emotion', {})
        anger_score = emotion_predictions.get('anger', 0)
        disgust_score = emotion_predictions.get('disgust', 0)
        fear_score = emotion_predictions.get('fear', 0)
        joy_score = emotion_predictions.get('joy', 0)
        sadness_score = emotion_predictions.get('sadness', 0)
        
        # Find the dominant emotion by determining the highest score
        emotion_scores = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }
        
        # Find the dominant emotion
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        
        # Return the output in the required format
        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
    
    else:
        # Handle the case where the request was not successful
        return f"Error: {response.status_code}, {response.text}"

