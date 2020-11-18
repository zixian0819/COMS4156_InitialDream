import os
from flask import Flask, render_template, request
from flask import Blueprint
from flaskr.db import get_db
# import our OCR function
from ocr_core import ocr_core

# define a folder to store and later serve the images
UPLOAD_FOLDER = '/static/uploads/'

# allow files of a specific type
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

bp = Blueprint('ocr', __name__, url_prefix='/ocr')


# function to check the file extension
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# route and function to handle the upload page
@bp.route('/upload', methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
        username = request.form['username']
        # check if there is a file in the request
        if 'file' not in request.files:
            return render_template('/ocr/upload.html', msg='No file selected')
        file = request.files['file']
        # if no file is selected
        if file.filename == '':
            return render_template('/ocr/upload.html', msg='No file selected')

        if file and allowed_file(file.filename):

            # call the OCR function on it
            extracted_text = ocr_core(file)

            if 'Negative' in extracted_text:
                db = get_db()
                db.execute('DELETE FROM yellow_pool WHERE yellow_user = ?', (username,))
                db.commit()
                return render_template('/ocr/upload.html',
                                       msg='Your test result is Negative, you will recieve Green Pass!')
            else:
                return render_template('/ocr/upload.html',
                                       msg='Automatic identification failed. Please request manual identification!')
            '''
            return render_template('/ocr/upload.html',
                                   msg='Successfully processed',
                                   extracted_text=extracted_text,
                                   img_src=UPLOAD_FOLDER + file.filename)
            '''
    elif request.method == 'GET':
        return render_template('/ocr/upload.html')
