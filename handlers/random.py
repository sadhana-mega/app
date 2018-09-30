import json
from random import choice

def main(app):
    with open('frames.json') as json_file:
        data = json.load(json_file)
        turns = choice(data)['turns']
        agent_responses = []
        for i in range(0, len(turns)):
            if not i % 2 == 0:
                agent_responses.append(turns[i]['text'])
        text = choice(agent_responses)
    return text