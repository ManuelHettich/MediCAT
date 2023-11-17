from openai import OpenAI
client = OpenAI()

def hello_chatgpt():
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Just say 'Hello, World'."},
        ]
    )

    return completion.choices[0].message.content


def plaintext_to_paragraphs(plaintext):
    """
    Convert plaintext to a list of paragraphs.
    """
    paragraphs = plaintext.split("\n\n")
    return paragraphs


def paragraphs_evaluation(paragraphs):
    """
    Evaluate the paragraphs with an LLM.
    """