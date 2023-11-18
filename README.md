# MediCAT

[Insert pic]

Pipeline[WIP]:

1) Medical guideline as PDF
2) Run plaintext2.py on the PDF to extract plain text [todo: prompt user for file name instead of hardcoding it]
3) Link to preconfigured LLM to refine the plaintext into consistent paragraphs and remove the header, footer, page numbers: https://chat.openai.com/g/g-k6P5O3xjk-cdss2 | *or via API*
4) Example output: paragraphs.txt
5) Categorize & Rank
    - Just Categorize paragraphs.txt (custom LLM): https://chat.openai.com/g/g-jjTX0bRBE-cdss3
    - Categorize and rank the relevance (custom LLM): https://chat.openai.com/g/g-QE9ApW7aM-cdss3r

![alt1](Step3.png)

![alt1](step5plusRelevance.png)

![alt1](Step5.png)

![alt1](static/logo.png)

Add your OpenAI API Key in your environmment as OPENAI_API_KEY:

```export OPENAI_API_KEY=<your-key>```


Link to final presentation: https://app.pitch.com/app/presentation/0459812a-7fac-4c17-9912-e4693c78876a/91459d0d-cf2b-4a19-ba8f-e6019a9081cb
