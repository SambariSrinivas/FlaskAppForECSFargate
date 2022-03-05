from flask import render_template
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/app')
def blog():
    return "Hello, from App!"

@app.route('/version')
def blog():
    return "This App version is 1.0.1"

@app.route('/eat')
def blog():
    return "We are sorry, we are building the kitchen, will take your order after sometime"

if __name__ == '__main__':
    app.run(threaded=True,host='0.0.0.0',port=8081)