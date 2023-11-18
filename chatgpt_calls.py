from openai import OpenAI
client = OpenAI()

PROMPT_PARAGPRAPHS = """
please just segment it into paragraphs, forget about the json etc. Remove every footer and header pattern. please mention them afterwards. Only give the output without any introduction or explanaition. Retain the paragraph numbering in the output. If there is no paragraph number in front of it, it cannot be a new paragraph, so it belongs to the paragraph before.
"""

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

    completion = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": PROMPT_PARAGPRAPHS},
            {"role": "user", "content": plaintext},
        ]
    )

    return completion.choices[0].message.content


def paragraphs_evaluation(paragraphs):
    """
    Evaluate the paragraphs with an LLM.
    """

    return ""