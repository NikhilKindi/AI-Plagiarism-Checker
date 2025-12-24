# Use a pipeline as a high-level helper
# from transformers import pipeline

# pipe = pipeline("text-classification", model="sanalsprasad/ai-generated-text-classification")

import requests

API_URL = "https://api-inference.huggingface.co/models/priyabrat/AI.or.Human.text.classification"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	


def check_ai(text):
    # output = query("cats.jpg")
    # return output['']
    output = query({
        "inputs": text,
    })
    print(output)
    for i in output[0]:
        if i['label']=='LABEL_0':
            out_ai = round(i['score']*100,2)
            break
    print('AI-Percentage: ',out_ai)
    return out_ai