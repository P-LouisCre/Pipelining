from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# In-memory database
items = []

import subprocess

def run_test_script():
    subprocess.run('test_script.bat', shell=True)

def run_deploy_script():
    subprocess.run('deploy_script.bat', shell=True)

@app.route('/')
def index():
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add_item():
    item = request.form.get('item')
    if item:
        items.append(item)
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete_item(index):
    if index < len(items):
        items.pop(index)
    return redirect(url_for('index'))

@app.route('/update/<int:index>', methods=['POST'])
def update_item(index):
    if index < len(items):
        items[index] = request.form.get('new_item')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
