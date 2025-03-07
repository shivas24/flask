from flask import Flask, request, render_template,jsonify
import json

obj = Flask(__name__)

@obj.route('/')
def welcome():
    return "Welcome to FLASK"

@obj.route('/cal', methods=["GET"])
def math_operator():
    operation = request.json["operation"]
    num1=request.json["num1"]
    num2=request.json["num2"]
    

    if operation == "add":
        result =  int(num1) + int(num2)
    
    elif operation  ==  "multiply":
        result = int(num1) * int(num2)
    
    elif operation == "division":
        result = int(num1) / int(num2)
    
    else:
        result = int(num1) - int(num2)

    return jsonify(result)


if __name__ == '__main__':
    obj.run()