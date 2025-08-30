from flask import Flask , jsonify
import speech_recognition as sr
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/listen', methods=["GET"])


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('Say Rock , Paper , Scissors')
        audio = recognizer.listen(source, timeout=3 , phrase_time_limit=3)
        
    try:
        text = recognizer.recognize_google(audio).lower()
        print(f"You Said : {text}")
    
        if 'rock' in text:
            return jsonify({'choice' : 'rock'})
        elif 'paper' in text:
            return jsonify({'choice' : 'paper'})
        elif 'scissors' in text or 'scissor' in text:
            return jsonify({'choice' : 'scissors'})
        else:
            return jsonify({'choice' : 'invalid'})
            
    except Exception as e:
        return jsonify({'choice' : 'error'})
    
if __name__ == "__main__":
    app.run(debug=True , port=5000) 
        