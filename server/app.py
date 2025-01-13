#!/usr/bin/env python3

from flask import Flask,Response

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<text>')
def print_text(text):
    print(text)  
    return text  

@app.route('/print/<string:username>')
def print_string(username):
    return f'<h1>Hello, {username}!</h1>'

@app.route('/count/<int:parameter>')
def count_view(parameter):
    numbers = "\n".join(str(i) for i in range(parameter)) + "\n"
    return Response(numbers, mimetype="text/plain")

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = int(num1) + int(num2)
    elif operation == '-':
        result = int(num1) - int(num2)
    elif operation == '*':
        result = int(num1) * int(num2)
    elif operation == 'div': 
        if num2 == '0':
            return f'Division by zero is not allowed'
        result = int(num1) / int(num2)
    elif operation == '%':
        if num2 == '0':
            return f'Division by zero is not allowed'
        result = int(num1) % int(num2)
    else:
        return f'Invalid operation'
    
    return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
