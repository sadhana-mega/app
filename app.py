from flask import Flask, render_template
import handlers.upload
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/upload", methods=['POST'])
def upload():
    handlers.upload.main(app)