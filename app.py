from flask import Flask

from controller.list_se_controller import app_list_se

app = Flask(__name__)

app.register_blueprint(app_list_se)
"""
@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/calculator/add/<num1>/<num2>')
def add(num1,num2):

    return str(int(num1)+int(num2))
@app.route("/calculator/subtract/<num1>/<num2>")
def subtract(num1,num2):
    return str(int(num1)-int(num2))

@app.route("/calculator/multi/<num1>/<num2>")
def multi(num1,num2):
    return str(int(num1)*int(num2))

@app.route("/calculator/Split/<num1>/<num2>")
def split(num1,num2):
    return str(int(num1)/int(num2))

@app.route("/calculator/Enhance/<num1>/<num2>")
def enhacnce(num1,num2):
    return str(int(num1)**int(num2))

if __name__ == '__main__':
    app.run()
"""
