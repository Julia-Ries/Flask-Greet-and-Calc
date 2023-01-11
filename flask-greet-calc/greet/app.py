from flask import Flask

app = Flask(__name__)


@app.route('/welcome')
def welcome_page():
    html = """
    <h1> Welcome!
    </h1>
    """
    return html


@app.route('/')
def main_page():
    return """
    <p>This is the main page!</p>
    """

@app.route('/welcome/home')
def home_page():
    return """
    <p>Welcome Home!</p>
    """


@app.route('/welcome/back')
def back_page():
    return """
    <p>Welcome back!</p>
    """