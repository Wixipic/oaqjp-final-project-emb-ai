"""
This file is the main server file that build the server
"""""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection  import emotion_detector

app=Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_detector():
    """
    Main app function
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    response=emotion_detector(text_to_analyze)
    dominant_check=response['dominant_emotion']

    if dominant_check is None:
        return "Invalid text! Please try again!."
    formatted_response = (f'For the given statement, the system response is'
                f'\'anger\': {response["anger"]},' 
                f'\'disgust\': {response["disgust"]}, \'fear\': {response["fear"]},'
                f'\'joy\': {response["joy"]} and \'sadness\': {response["sadness"]}.'
                f'The dominant emotion is {response["dominant_emotion"]}.')
    return formatted_response
@app.route("/")
def render_index_page():
    """
    Function to render frontend using the template index
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
