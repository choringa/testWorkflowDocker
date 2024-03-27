from flask import Flask, request
import subprocess
import hashlib
import hmac

app = Flask(__name__)

def verify_signature(payload_body, secret_token, signature_header):
    """Verify that the payload was sent from GitHub by validating SHA256.

    Raise and return 403 if not authorized.

    Args:
        payload_body: original request body to verify (request.body())
        secret_token: GitHub app webhook token (WEBHOOK_SECRET)
        signature_header: header received from GitHub (x-hub-signature-256)
    """
    if not signature_header:
        raise Exception(status_code=403, detail="x-hub-signature-256 header is missing!")
    hash_object = hmac.new(secret_token.encode('utf-8'), msg=payload_body, digestmod=hashlib.sha256)
    expected_signature = "sha256=" + hash_object.hexdigest()
    if not hmac.compare_digest(expected_signature, signature_header):
        raise Exception(status_code=403, detail="Request signatures didn't match!")

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
    if(request.headers.has_key("X-Hub-Signature-256")):
        print(request.headers.get("X-Hub-Signature-256"))

    update()
    return f'Hello, from updater!'

@app.route('/')
def duck():
    print("updater")
    return f'i\'m updater'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080' ,debug=True)