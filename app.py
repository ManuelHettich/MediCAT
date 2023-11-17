from flask import Flask
from openai import OpenAI
client = OpenAI()


app = Flask(__name__)

@app.route('/', methods=["POST"])
def hello_world():
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
            {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
        ]
    )

    return completion.choices[0].message

if __name__ == '__main__':
    app.run(debug=True)
