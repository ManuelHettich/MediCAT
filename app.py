from flask import Flask, request, jsonify
from chatgpt_calls import hello_chatgpt, plaintext_to_paragraphs, paragraphs_evaluation

app = Flask(__name__)

@app.route('/', methods=["POST"])
def hello_world():
    return hello_chatgpt()


if __name__ == '__main__':
    app.run(debug=True)
