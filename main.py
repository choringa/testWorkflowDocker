from flask import Flask, request

app = Flask(__name__)


@app.route('/webhooked', methods =['POST'])
def hello():
    content = request.json
    print(f"request data: {request.data}")
    print(f"content: {content}")
    return f'Hello, World! {content}'

@app.route('/')
def duck():
    print("hi")
    return f'suck my duck 🦆'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080' ,debug=True)