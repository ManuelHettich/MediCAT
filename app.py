from flask import Flask, request, jsonify, flash, render_template, request
from werkzeug.utils import secure_filename
from chatgpt_calls import hello_chatgpt, plaintext_to_paragraphs, paragraphs_evaluation
import os
from plaintext import extract_pdf

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
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

        # Save the output text to a file for debugging purposes
        plain_text_path = 'output_text_file.txt'
        
        # Delete output text file if it already exists
        if os.path.exists(plain_text_path):
            os.remove(plain_text_path)

        # Write the output text to a file
        with open(plain_text_path, 'w') as file:
            file.write(plain_text)

        # Use LLM to segment the text into paragraphs
        paragraphs = plaintext_to_paragraphs(plain_text)
        print(paragraphs)
        
        return paragraphs


if __name__ == '__main__':
    app.run(debug=True)
