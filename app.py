from flask import Flask, jsonify, request, send_from_directory

from calculator_mcp_server.core import add as _add
from calculator_mcp_server.core import subtract as _subtract
from calculator_mcp_server.core import multiply as _multiply
from calculator_mcp_server.core import divide as _divide
from calculator_mcp_server.core import power as _power
from calculator_mcp_server.core import modulo as _modulo
from calculator_mcp_server.core import square as _square
from calculator_mcp_server.core import cube as _cube

app = Flask(__name__)


# Plain wrapper functions — these call core.py directly.
# MCP will import THESE (from app.py), not core.py directly.
def add(a: float, b: float) -> float:
    """Add two numbers together."""
    return _add(a, b)


def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return _subtract(a, b)


def multiply(a: float, b: float) -> float:
    """Multiply two numbers together."""
    return _multiply(a, b)


def divide(a: float, b: float) -> float:
    """Divide a by b. Raises an error if b is zero."""
    return _divide(a, b)


def power(a: float, b: float) -> float:
    """Raise a to the power of b."""
    return _power(a, b)


def modulo(a: float, b: float) -> float:
    """Return the remainder of a divided by b. Raises an error if b is zero."""
    return _modulo(a, b)


def square(a: float) -> float:
    """Return a squared."""
    return _square(a)


def cube(a: float) -> float:
    """Return a cubed."""
    return _cube(a)


@app.route("/")
def index():
    return send_from_directory("static", "index.html")


@app.route("/add", methods=["POST"])
def add_route():
    data = request.get_json()
    return jsonify({"result": float(add(data["a"], data["b"]))})


@app.route("/subtract", methods=["POST"])
def subtract_route():
    data = request.get_json()
    return jsonify({"result": float(subtract(data["a"], data["b"]))})


@app.route("/multiply", methods=["POST"])
def multiply_route():
    data = request.get_json()
    return jsonify({"result": float(multiply(data["a"], data["b"]))})


@app.route("/divide", methods=["POST"])
def divide_route():
    data = request.get_json()
    try:
        result = divide(data["a"], data["b"])
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    return jsonify({"result": float(result)})


@app.route("/power", methods=["POST"])
def power_route():
    data = request.get_json()
    return jsonify({"result": float(power(data["a"], data["b"]))})


@app.route("/modulo", methods=["POST"])
def modulo_route():
    data = request.get_json()
    try:
        result = modulo(data["a"], data["b"])
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    return jsonify({"result": float(result)})


@app.route("/square", methods=["POST"])
def square_route():
    data = request.get_json()
    return jsonify({"result": float(square(data["a"]))})


@app.route("/cube", methods=["POST"])
def cube_route():
    data = request.get_json()
    return jsonify({"result": float(cube(data["a"]))})


if __name__ == "__main__":
    app.run(debug=True, port=5000)