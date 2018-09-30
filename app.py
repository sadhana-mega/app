from flask import Flask, render_template
import handlers.upload
import handlers.random
app = Flask(__name__)
app.config["CACHE_TYPE"] = "null"

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/random")
def random():
    return handlers.random.main(app)

@app.route("/upload", methods=['POST'])
def upload():
    return handlers.upload.main(app)