# Put your app in here.

from flask import Flask, request

app = Flask(__name__)

from operations import add, sub, mult, div


@app.route("/add")
def do_add():
    """Adds a and b and returns result as the body."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)

    return str(result)


@app.route("/sub")
def do_sub():
    """subtract b from a"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a, b)

    return str(result)


@app.route("/mult")
def do_mult():
    """Multiply a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a, b)

    return str(result)


@app.route("/div")
def do_div():
    """Divide a by b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a, b)

    return str(result)



operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }


@app.route("/math/<oper>")
def do_math(oper):
    """run the operator on a and b """


    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)

    return str(result)