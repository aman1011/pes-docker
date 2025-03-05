from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_docker():
    return 'Hello, Quest!'

@app.route('/pm')
def hello_pm():
    return "Hello, Aman!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)