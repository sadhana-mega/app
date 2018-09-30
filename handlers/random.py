import json
from random import choice

def main(app):
    with open('frames.json') as json_file:
        response_list = []
        data = json.load(json_file)
        text = choice(choice(data)['turns'])['text']
    return text