from flask import request, jsonify
from . import blueprint
import PyPDF2
import re

# @blueprint.route('/process_pdf', methods=['POST'])
# def process_pdf():
#   file = request.files.get('file')

#   if not file:
#       return jsonify({'error': 'No file provided'})

#   pdf_reader = PyPDF2.PdfReader(file)
#   if len(pdf_reader.pages)== 0:
#     return jsonify({'errors': 'File is empty'})

#   first_page = pdf_reader.pages[0]
#   text = first_page.extract_text()
#   words = text.split()[:3]

#   return jsonify({'file_name': file.filename, 'first_three_words': ' '.join(words)})\
  
# @blueprint.route('/process_pdf', methods=['POST'])
# def process_pdf():
#   words = ["frontend", "backend", "developer", "Javascript", "python"]

#   file = request.files['file']
#   pdf_reader = PyPDF2.PdfReader(file)

#   if not file:
#     return jsonify({'error': 'No file provided'}) 

#   results = {}

#   for word in words:
#     count = 0

#     for page in range(len(pdf_reader.pages)):
#       page_text = pdf_reader.pages[page].extract_text()
#       count += page_text.lower().count(word.lower())

#     if count > 0:
#       results[word] = count

#   return jsonify(results)

# Extract name and count keyword occurrences
@blueprint.route('/process_pdf', methods=['POST'])
def process_pdf():
    words = ["frontend", "backend", "developer", "javascript", "python"]
    file = request.files['file']
    list =request.form.get('list')
    print(list)

    if not file:
        return jsonify({'error': 'No file provided'})
    if not file.filename.endswith('.pdf'):
      return jsonify({'error': 'File must be a PDF'})

    results = {'data': {}}

    pdf_reader = PyPDF2.PdfReader(file)
    first_name, last_name = extract_name(file)
    results['candidate_name'] = f"{first_name} {last_name}"
    for page in range(len(pdf_reader.pages)):
        page_text = pdf_reader.pages[page].extract_text()
        for word in words:
            count = page_text.lower().count(word.lower())
            if count > 0:
              results["data"][word] = results.get(word, 0) + count
    return jsonify(results)

def extract_name(cv_file):
  pdf_reader = PyPDF2.PdfReader(cv_file)
  text = "".join([page.extract_text() for page in pdf_reader.pages])
  # Extract first and last name from the text
  match = re.search(r"(\b[A-Z][a-z]+\b)\s(\b[A-Z][a-z]+\b)", text)
  first_name = match.group(1)
  last_name = match.group(2)
  return first_name, last_name
