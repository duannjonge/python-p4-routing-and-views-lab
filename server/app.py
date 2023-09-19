#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

app.route('</print/string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter


app.route('/count/<integer:parameter>')
def count(parameter):
    for x in range (parameter):
        print(x)

# def math(operation,num1,num2):
#     pass
@app.route('/math/<float:num1><operation><float:num2>')
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
            return "Division by zero is not allowed", 400
    elif operation == '%':
        if num2 != 0:
            result = num1 % num2
        else:
            return "Modulus by zero is not allowed", 400
    else:
        return "Invalid operation", 400

    return f"The result of {num1} {operation} {num2} is {result}"



if __name__ == '__main__':
    app.run(port=5555, debug=True)
