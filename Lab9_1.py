from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/hello')
def hello():
    return "Hello World Route!!!"

@app.route('/<opt>/<float:a>/<float:b>')
def operator(opt,a,b):
    if opt == 'add':
        ans = a+b
        return f'<h3>{a} + {b} = {ans}</h3>'
    elif opt == 'sub':
        ans = a-b
        return f'<h3>{a} - {b} = {ans}</h3>'
    elif opt == 'mul':
        ans = a*b
        return f'<h3>{a} * {b} = {ans}</h3>'
    elif opt == 'div':
        ans = a/b
        return f'<h3>{a} / {b} = {ans}</h3>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
