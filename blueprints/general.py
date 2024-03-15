from flask import Blueprint

app = Blueprint('general', __name__)


@app.route('/')
def main():  # put application's code here
    return 'this is maim page!'


@app.route('/about')
def about():  # put application's code here
    return 'about us!'
