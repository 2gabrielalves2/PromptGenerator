import requests as requests

from env import API_KEY
from openai import OpenAI
import json
from flask import request

client = OpenAI(
    api_key=API_KEY
)

headers={"Authorization": f"Bearer {API_KEY}", "Content-type": "application/json"}
link = "https://api.openai.com/v1/chat/completions"
id_modelo = "gpt-3.5-turbo"


def generateChatResponse(prompt):
    body_mensagem = {
        "model": id_modelo,
        "messages": [{"role": "user", "content": prompt}]
    }
    body_mensagem = json.dumps(body_mensagem)

    requisicao = requests.post(link, headers=headers, data=body_mensagem)
    resposta = requisicao.json()

    try:
        answer = resposta['choices'][0]['message']['content']
    except:
        answer = 'Oops the AI can´t give u a answer, try another one.'

    return answer


def generateQuizResponse(prompt):
    body_mensagem = {
        "model": id_modelo,
        "messages": [
           {"role": "user", "content": prompt}
        ]
    }

    body_mensagem = json.dumps(body_mensagem)

    requisicao = requests.post(link, headers=headers, data=body_mensagem)
    resposta = requisicao.json()

    try:
        answer = resposta['choices'][0]['message']['content']
    except:
        answer = 'Oops the AI can´t give u a answer, try another one.'

    print(answer)
    return answer

