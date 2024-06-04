import math

def calculate_quadratic(a: float, b: float, c: float) -> dict:
    """
    Calculates the roots, vertex, and other properties of a quadratic function.
    
    Args:
        a (float): Coefficient of x^2.
        b (float): Coefficient of x.
        c (float): Constant term.
        
    Returns:
        dict: A dictionary containing the following properties:
            - "delta": Delta value of the quadratic equation.
            - "roots": A list of roots (zero points) of the quadratic equation.
            - "vertex": Coordinates of the vertex (x, y) of the parabola.
            - "y_intercept": The y-intercept point of the parabola.
    """
    delta = b**2 - 4*a*c
    roots = []
    vertex_x = -b / (2*a)
    vertex_y = a * vertex_x**2 + b * vertex_x + c
    y_intercept = c
    
    if delta > 0:
        root1 = (-b + math.sqrt(delta)) / (2*a)
        root2 = (-b - math.sqrt(delta)) / (2*a)
        roots = [root1, root2]
    elif delta == 0:
        root = -b / (2*a)
        roots = [root]
    
    return {
        "delta": delta,
        "roots": roots,
        "vertex": (vertex_x, vertex_y),
        "y_intercept": y_intercept
    }
