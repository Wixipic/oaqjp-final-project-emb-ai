import requests
import json

def emotion_detector(text_to_analyze):
    """
    Function to call the Watson API emotion detector
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }

    #Calling the API emotion detector
    response = requests.post(url, json = myobj, headers=header)

    # Formating the json response
    formatted_response = json.loads(response.text)
    
    # Extracting all emotion scores
    emotion_scores = {}
    for prediction in formatted_response['emotionPredictions']:
        if 'emotion' in prediction:
            emotion_scores.update(prediction['emotion'])

   #Get the dominant emotion according to max score values 
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    emotion_scores["dominant emotion"] = dominant_emotion
    
    # Returning a dictionary containing emotion analysis results
    return emotion_scores
