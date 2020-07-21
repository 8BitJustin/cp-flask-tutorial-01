from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home/users/<string:name>/posts/<int:id>')
def hello(name, id):
    return f'Hello, {name}, you are viewing post {id}.'


@app.route('/onlyget', methods=['GET'])
def only_get():
    return "You can only get this webpage"


if __name__ == "__main__":
    app.run(debug=True)
