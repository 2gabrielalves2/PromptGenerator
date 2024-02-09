import json
import openai
from flask import Flask, render_template, request, jsonify
from env import API_KEY
import api

app = Flask(__name__)

quiz_data: str = ''


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        prompt = request.form['prompt']

        res={}
        res['answer'] = api.generateChatResponse(prompt)
        print(res)
        return res

    return render_template('main.html', **locals())


@app.route('/quiz', methods=['POST', 'GET'])
def quiz():
    global quiz_data
    if request.method == 'POST':
        prompt = request.form['prompt']

        quiz_data += '{"role": "user", "content": ' + prompt + '}'

        res = {}
        res['answer'] = api.generateQuizResponse(quiz_data)

        quiz_data += ',{"role": "assistant", "content": ' + str(res) + '},'

        print(quiz_data)
        print(res)
        return jsonify(res), 200
    else:
        quiz_data = ''

    return render_template('quiz.html', **locals())


@app.route('/chat', methods=["POST", "GET"])
def chat():
    if request.method == "POST":
        task = request.form["task"]
        context = request.form["context"]
        topic = request.form["topic"]
        style = request.form["style"]
        tone = request.form["tone"]
        audience = request.form["audience"]
        word_limit = request.form["word_limit"]
        format = request.form["format"]
        example = request.form["example"]

        prompt = "Task: " + task + "\nContent: " + context + "\nTopic: " + topic + "\nStyle: " + style + "\nTone: " + tone \
                 + "\nAudience: " + audience + "\nWord Limit: " + word_limit + "\nFormat: " + format + "\nExample: " + example

        print(prompt)

        res = api.generateChatResponse(prompt)

        print(res)
        jsonify(res), 200

        return render_template('chat.html', form_text=res, generated_prompt=prompt)
    return render_template('chat.html')


if __name__ == '__main__':
    app.run()