from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Sup David."

@app.route('/gettest')
def xml():
    str1 = '{"patients":[{"firstname":"John", "lastname":"Doe", "id":1, "age":20, "esi":1, "queue":1, "resources":[123, 41, 1]},{"firstname":"Ben", "lastname":"Smith", "id":2, "age":32, "esi":1, "queue":2, "resources":[124, 40]}]}}'
    return str1

if __name__ == '__main__':
    app.run()
