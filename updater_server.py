from flask import Flask, request
import subprocess
import hashlib
import hmac
import os

app = Flask(__name__)

def verify_signature(payload_body, secret_token, signature_header):
    hash_object = hmac.new(secret_token.encode('utf-8'), msg=payload_body, digestmod=hashlib.sha256)
    expected_signature = "sha256=" + hash_object.hexdigest()
    if not hmac.compare_digest(expected_signature, signature_header):
        raise Exception("Request signatures didn't match!")

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
    request_dict = request.json
    if(request.headers.get("X-Hub-Signature-256")):
        print(f"1: {request_dict.get('author')}")
        print(f"hub ignature: {request.headers.get('X-Hub-Signature-256')}")
        secret = os.getenv("GITHUB_WEBHOOK_SECRET")
        if(secret):
            verify_signature(request.data, secret, request.headers.get("X-Hub-Signature-256"))
            update()
        else:
            print("No GITHUB_WEBHOOK_SECRET set on the environment variables")
    else:
        print(f"No X-Hub-Signature-256 header")
    return f'Hello, from updater!'

@app.route('/')
def duck():
    print("updater")
    return f'i\'m updater'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080' ,debug=True)