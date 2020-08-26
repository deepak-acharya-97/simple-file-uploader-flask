import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from random import randint

UPLOAD_FOLDER = 'static\\uploaded-pdfs'
app=Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def loadMasterPage():
    if(request.method == "GET"):
        return render_template('index.html')
    else:
        if('pdf-file' not in request.files):
            flash("No file part")
            return redirect(request.url)
        file = request.files['pdf-file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        filename = secure_filename(file.filename)
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(path)
        return redirect(request.url)

if __name__ == '__main__':
    port=randint(1025,9999)
    app.run('0.0.0.0',port)