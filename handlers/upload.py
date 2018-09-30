import os
import io
from watson_developer_cloud import SpeechToTextV1
from flask import Flask, flash, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename

def allowed_file(filename, allowed_extensions):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

def main(app):
    if request.method == 'POST':
        status = {}
        if 'file' not in request.files:
            status = {
                'valid' : False,
                'text' : 'No file part'
            }
        file = request.files['file']
        if file.filename == '':
            status = {
                'valid' : False,
                'text' : 'No selected file'
            }
        if file and allowed_file(file.filename, allowed_extensions = set(['wav', 'mp3'])):
            file.save('/home/sripravan/Projects/sadhana-mega/app/static/audio/test.wav')
            with io.open('/home/sripravan/Projects/sadhana-mega/app/static/audio/test.wav', 'rb') as audio_file:
                speech_to_text = SpeechToTextV1(username='3ec1ed34-e5e2-42bd-aac5-c6cea9ae85aa', password='8gVumSNEqyGn')
                speech_recognition_results = speech_to_text.recognize(audio=audio_file, content_type="audio/wav", timestamps=True, smart_formatting=True).get_result()
                status = {
                    'valid' : True,
                    'transcript' : speech_recognition_results
                }
    return jsonify(status)