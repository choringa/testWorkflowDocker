from flask import Flask, request
import subprocess

app = Flask(__name__)

def update():
    print ("Starting update")
    execution_list = ['bash', './updater.sh']
    try:
        p = subprocess.run(execution_list, capture_output=True, text=True, input="n")
        print(f"stdout of process: {p.stdout}")
        if p.returncode == 0:
            print("En teoria todo good")
        else:
            print(f"Error: {p.stderr}")
    except Exception as e:
        print(f"Fail runing updater script: {str(e)})")

@app.route('/webhooked', methods =['POST'])
def hello():
    content = request.json
    print(f"request data: {request.data}")
    print(f"request headers: {request.headers}")
    print(f"content: {content}")
    update()
    return f'Hello, from updater!'

@app.route('/')
def duck():
    print("updater")
    return f'i\'m updater'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080' ,debug=True)