from flask import Flask, request, jsonify, flash, render_template, request, send_file
from werkzeug.utils import secure_filename
from chatgpt_calls import hello_chatgpt, plaintext_to_paragraphs, paragraphs_evaluation
import os
import json
from plaintext import extract_pdf
from generateCSV import generateCSV

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
OUTPUT_FOLDER = "output"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('upload.html')


@app.route('/hello', methods=["POST"])
def hello_world():
    return hello_chatgpt()


@app.route('/process_pdf', methods=['POST'])
def process_pdf():
    # Check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(pdf_path)

        # Extract the plain text from the PDF
        plain_text = extract_pdf(pdf_path)

        print("-------- Plain PDF Text --------")
        print(plain_text)

        save_file(plain_text, "plain_text_file.txt")

        # Save the plain text to a file for debugging purposes
        #plain_text_path = 'plain_text_file.txt'
        
        # Delete plain text file if it already exists
        #if os.path.exists(plain_text_path):
        #    os.remove(plain_text_path)

        # Write the plain text to a file
        #with open(plain_text_path, 'w') as file:
        #    file.write(plain_text)

        # Use LLM to segment the text into paragraphs
        paragraphs_json = plaintext_to_paragraphs(plain_text)
        print("-------- Paragraphs --------")
        print(paragraphs_json)

        save_file(json.dumps(paragraphs_json), "paragraphs.txt")

        # Use the LLM to classify the paragraphs
        paragraphs_evaluated = paragraphs_evaluation(paragraphs_json)
        print("-------- Evaluation --------")
        print(paragraphs_evaluated)

        save_file(json.dumps(paragraphs_evaluated), "paragraphs_evaluated.txt")

        # Transform JSON into CSV
        print("-------- CSV Generation --------")
        generateCSV(json.loads(paragraphs_evaluated))
        return send_file("categorized_file.csv", as_attachment=True)


def save_file(file_content, filename):
    """
    Save the content to a file in UPLOAD_FOLDER
    """
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    # Delete text file if it already exists
    if os.path.exists(file_path):
        os.remove(file_path)

    # Write the text to a file
    with open(file_path, 'w') as file:
        file.write(file_content)
    
    return filename

if __name__ == '__main__':
    app.run(debug=True)
