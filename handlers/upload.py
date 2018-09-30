import os
import assemblyai
from flask import Flask, flash, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

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
           aai = assemblyai.Client(token='6a4fddfb6ae9430c93c29f24dc109a80')
           transcript = aai.transcribe(filename='/home/sripravan/Projects/sadhana-mega/app/static/audio/test.wav', format_text=False)
           while transcript.status != 'completed':
               transcript = transcript.get()
           status = {
               'valid' : True,
               'transcript' : transcript.dict
           }
    return jsonify(status)