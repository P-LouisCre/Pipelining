from flask import Flask, request

app = Flask(__name__)

@app.route('/testing', methods=['POST'])
def testing():
    payload = request.json
    ref = payload.get('ref', '')

    if ref == 'refs/heads/testing':
        # Logic for testing branch
        return "Testing branch hook received successfully!"

    return "Invalid branch hook received."

@app.route('/deployment', methods=['POST'])
def deployment():
    payload = request.json
    ref = payload.get('ref', '')

    if ref == 'refs/heads/main':
        # Logic for deployment branch
        return "Deployment branch hook received successfully!"

    return "Invalid branch hook received."

if __name__ == '__main__':
    app.run(debug=True)
