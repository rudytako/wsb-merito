def quadratic_to_vertex(a: float , b :float, c: float) -> str:
    """
    Converts quadratic function from standard form to vertex form.
    
    Args:
        a (float): Coefficient of x^2.
        b (float): Coefficient of x.
        c (float): Constant term.
        
    Returns:
        str: Vertex form of the quadratic function.
    """
    p = -b / (2*a)
    q = a * p**2 + b * p + c
    return f"{a}(x - {p})^2 + {q}"
