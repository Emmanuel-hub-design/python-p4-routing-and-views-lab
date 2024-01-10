#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)  # Prints the string in the console
    return f'<h2>Printed String: {parameter}</h2>'

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = '<h2>Counted Numbers:</h2>'
    for num in range(parameter):
        numbers += f'<p>{num}</p>'
    return numbers

@app.route('/math/<float:num1>/<operation>/<float:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return '<h2>Error: Division by zero!</h2>'
    elif operation == '%':
        result = num1 % num2

    if result is not None:
        return f'<h2>Result of {num1} {operation} {num2}: {result}</h2>'
    else:
        return '<h2>Invalid operation or input!</h2>'

if __name__ == '__main__':
    app.run(debug=True)
