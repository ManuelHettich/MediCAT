from flask import Flask
from openai import OpenAI
client = OpenAI()


app = Flask(__name__)

@app.route('/', methods=["POST"])
def hello_world():
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Just say 'Hello, World'."},
        ]
    )

    print(completion.choices)

    return str(completion.choices[0].message.content)

if __name__ == '__main__':
    app.run(debug=True)
