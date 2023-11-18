from openai import OpenAI
client = OpenAI()

PROMPT_PARAGPRAPHS = """
Please just segment this text into paragraphs. Remove every footer and header pattern. Only give the output without any introduction or explanation. Retain the paragraph numbering in the output. If there is no paragraph number in front of it, it cannot be a new paragraph, so it belongs to the paragraph before.
Make your output adhere to this JSON format (one object in the list per paragraph) but don't add a JSON comment at the beginning or end, just output the pure JSON as in this example:
{
    [
        {
            "text": "",
            "category_ID": "",
            "paragraph_number": "": 
        }
    ]
}
"""

PROMPT_CLASSIFICATION = """
Categorize each paragraph of the medical guideline fed into the GPT into one of the following six categories:
1: diagnostic recommendations,
2: medication and other therapeutic recommendations,
3: recommendations of monitoring and follow-up
4: possible interactions with other guidelines, including comorbidities
5: early warning signs, estimation of risk and poor evolution 
6: none of the above five categories

Make your output adhere to this JSON format (one object in the list per paragraph).
text: unshortened original paragraph without the paragraph number at the beginning
category_ID: 1, 2, 3, 4, 5, 6 (see above)
paragraph_number: original paragraph number from the paragraph numbering as a string

Make your output adhere to this JSON format (one object in the list per paragraph) but don't add a JSON comment at the beginning or end, just output the pure JSON as in this example:
{
    [
        {
            "text": "",
            "category_ID": "",
            "paragraph_number": "": 
        }
    ]
}
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
    Convert plaintext to a list of paragraphs as JSON with an LLM.
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
    Evaluate the list of paragraphs as JSON with an LLM.
    """

    completion = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": PROMPT_CLASSIFICATION},
            {"role": "user", "content": paragraphs},
        ]
    )

    return completion.choices[0].message.content