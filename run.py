from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_tasks():
    return 'Hello World!'

app.run(debug=True)