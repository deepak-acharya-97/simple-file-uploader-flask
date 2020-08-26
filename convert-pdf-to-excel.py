from flask import Flask, render_template
from random import randint

app=Flask(__name__)

@app.route('/')
def loadMasterPage():
    return render_template('index.html')

if __name__ == '__main__':
    port=randint(1025,9999)
    app.run('0.0.0.0',port)