import os
from flask import Flask, flash, request, redirect, url_for, render_template, send_file
from werkzeug.utils import secure_filename
from tabula import read_pdf
from random import randint

UPLOAD_FOLDER = 'static\\uploaded-pdfs'
app=Flask(__name__, static_url_path='', static_folder='static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def loadMasterPage():
    if(request.method == "GET"):
        args = request.args
        is_success = False
        filename = None
        if('is_success' in args):
            is_success = args['is_success']
            filename = args['filename']
        return render_template('index.html', is_success = is_success, filename = filename)
    else:
        if('pdf-file' not in request.files):
            flash("No file part")
            return redirect(request.url)
        file = request.files['pdf-file']
        print("file", file)
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        filename = secure_filename(file.filename)
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(path)
        pdf = read_pdf(path)
        return redirect(url_for("loadMasterPage", is_success = True, filename = filename))

@app.route('/result/<filename>')
def download_file(filename):
    path = path = os.path.join("static", "result.xlsx")
    file =  open(path, 'rb')
    attachment_filename = filename.split(".")[0]+".xlsx"
    return send_file(file, as_attachment = True, attachment_filename=attachment_filename)

if __name__ == '__main__':
    port=randint(1025,9999)
    app.run('0.0.0.0',port)