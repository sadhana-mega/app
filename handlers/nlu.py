import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions

def main(app, user_text):
    service = NaturalLanguageUnderstandingV1(version='2018-03-16', username='3984c664-3ec5-481a-a762-01f3dbcffcd7', password='hHwBvGdN7Fsm')
    response = service.analyze(text=user_text, features=Features(entities=EntitiesOptions(), keywords=KeywordsOptions())).get_result()
    return json.dumps(response, indent=2)