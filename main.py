from flask import Flask, request

app = Flask(__name__)


@app.route('/webhooked')
def hello():
    content = request.json
    return f'Hello, World! {content}'