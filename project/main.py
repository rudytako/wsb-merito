from quadratic_calculator import calculate_quadratic
from standard_form import quadratic_to_standard
from vertex_form import quadratic_to_vertex
from factorial_form import quadratic_to_factorial
from plot_parabola import plot_parabola

def main():
    # Get coefficients from the user
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    
    # Calculate properties of the quadratic function
    result = calculate_quadratic(a, b, c)
    
    # Display results
    print("\nDelta:", result["delta"])
    print("Roots:", result["roots"])
    print("Vertex:", result["vertex"])
    print("Y-intercept:", result["y_intercept"])

    # Convert quadratic function to different forms
    print("\nQuadratic function in standard form:", quadratic_to_standard(a, b, c))
    print("Quadratic function in vertex form:", quadratic_to_vertex(a, b, c))
    print("Quadratic function in factorial form:", quadratic_to_factorial(a, b, c, result["vertex"][0], result["vertex"][1]))

    plot_parabola(a, b, c)

if __name__ == "__main__":
    main()
