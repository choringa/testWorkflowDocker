from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def duck():
    print("hi")
    return f'suck my duck 🦆'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000' ,debug=True)