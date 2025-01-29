"""
Emotion Detection API using Flask.

This application serves a simple emotion detection API that uses
a custom emotion_detector function to analyze user-provided text
and return the dominant emotion.
"""

from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """
    Renders the index.html page.
    
    Returns:
        str: Rendered HTML template for the index page.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotion_detector_route():
    """
    Emotion detection route to process user input.

    This route processes a user-provided text input via the
    'textToAnalyze' query parameter, analyzes it using the
    emotion_detector function, and returns the emotion analysis
    or an error message if the input is invalid.

    Returns:
        Response: JSON response with emotion analysis or error message.
    """
    statement = request.args.get('textToAnalyze')

    if statement:
        # Use the emotion_detector function to get the emotion analysis
        result = emotion_detector(statement)

        # Check if dominant_emotion is None (i.e., invalid text)
        if result['dominant_emotion'] is None:
            return jsonify({"error": "Invalid text! Please try again."}), 400

        # Prepare the response message
        response = {
            'anger': result['anger'],
            'disgust': result['disgust'],
            'fear': result['fear'],
            'joy': result['joy'],
            'sadness': result['sadness'],
            'dominant_emotion': result['dominant_emotion']
        }

        print(response)

        response_text = (
            f"For the given statement, the system response is 'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
            f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
            f"The dominant emotion is {result['dominant_emotion']}."
        )

        return jsonify({"response": response_text})

    # Handle the case where no input is provided
    return jsonify({'error': 'Please provide a statement for emotion detection.'}), 400

if __name__ == '__main__':
    app.run(debug=True, host="localhost", port=5001)
