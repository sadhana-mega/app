from flask import Flask, render_template
import handlers.upload
import handlers.random
import handlers.nlu
app = Flask(__name__)
app.config["CACHE_TYPE"] = "null"

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/random")
def random():
    return handlers.random.main(app)

@app.route("/chat")
def chat():
    return render_template('chat.html')

@app.route("/upload", methods=['POST'])
def upload():
    return handlers.upload.main(app)

@app.route("/nlu/<user_text>")
def nlu(user_text):
    return handlers.nlu.main(app, user_text)

@app.after_request
def add_header(request):
    request.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    request.headers["Pragma"] = "no-cache"
    request.headers["Expires"] = "0"
    request.headers['Cache-Control'] = 'public, max-age=0'
    return request