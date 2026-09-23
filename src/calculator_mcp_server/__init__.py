import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from mcp.server.mcpserver import MCPServer

from app import add as _add
from app import subtract as _subtract
from app import multiply as _multiply
from app import divide as _divide
from app import power as _power
from app import modulo as _modulo
from app import square as _square
from app import cube as _cube

mcp = MCPServer("Calculator")


@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers together."""
    return _add(a, b)


@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return _subtract(a, b)


@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers together."""
    return _multiply(a, b)


@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide a by b. Raises an error if b is zero."""
    return _divide(a, b)


@mcp.tool()
def power(a: float, b: float) -> float:
    """Raise a to the power of b."""
    return _power(a, b)


@mcp.tool()
def modulo(a: float, b: float) -> float:
    """Return the remainder of a divided by b. Raises an error if b is zero."""
    return _modulo(a, b)


@mcp.tool()
def square(a: float) -> float:
    """Return a squared."""
    return _square(a)


@mcp.tool()
def cube(a: float) -> float:
    """Return a cubed."""
    return _cube(a)


def main() -> None:
    mcp.run()