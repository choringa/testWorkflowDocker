from flask import Flask, request

app = Flask(__name__)


@app.route('/webhooked', methods =['POST'])
def hello():
    content = request.json
    return f'Hello, World! {content}'

@app.route('/')
def duck():
    return f'suck my duck 🦆'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080' ,debug=True)