def quadratic_to_factorial(a: float, r1: float, r2: float) -> str:
    """
    Converts quadratic function from standard form to factorial form.
    
    Args:
        a (float): Coefficient of x^2.
        b (float): Coefficient of x.
        c (float): Constant term.
        
    Returns:
        str: Factorial form of the quadratic function.
    """
    return f"{a}(x - {r1})(x - {r2})"
