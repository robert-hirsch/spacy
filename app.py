import json
import spacy

nlp = spacy.load("en_core_web_sm")

def lambda_handler(event, context):
    text = event.get('queryStringParameters', {}).get('text')
    
    print(event)
    print(type(text))
    
    if not isinstance(text, str):
        return {
            'statusCode': 400
        }
    
    doc = nlp(text)
    data = {"nouns": [token.lemma_ for token in doc if token.pos_ == "NOUN"], "verbs": [token.lemma_ for token in doc if token.pos_ == "VERB"]}
    
    return {
        'statusCode': 200,
        'headers': {'content-type': 'application/json'},
        'body': json.dumps(data)
    }