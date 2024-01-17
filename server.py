from flask import Flask, request

app = Flask(__name__)

import subprocess

def run_test_script():
    subprocess.run('test_script.bat', shell=True)

def run_deploy_script():
    subprocess.run('deploy_script.bat', shell=True)

@app.route('/staging', methods=['POST'])
def staging():
    payload = request.json
    ref = payload.get('ref', '')

    if ref == 'refs/heads/staging':
        # Logic for testing branch
        print("Run testing script")
        run_test_script()
        return "Testing branch hook received successfully!"

    return "Invalid branch hook received."

@app.route('/deployment', methods=['POST'])
def deployment():
    payload = request.json
    ref = payload.get('ref', '')

    if ref == 'refs/heads/main':
        # Logic for deployment branch
        print('Run deployment script')
        run_deploy_script()
        return "Deployment branch hook received successfully!"

    return "Invalid branch hook received."

"hey"

if __name__ == '__main__':
    app.run(debug=False)
