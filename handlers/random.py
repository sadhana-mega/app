import json

def main(app):
    total_text = ""
    with open('frames.json') as json_file:
        data = json.load(json_file)
        turns = data[0]['turns']
        for turn in turns:
            total_text += turn['text'] + "<br>"
    return total_text
    