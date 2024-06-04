import matplotlib.pyplot as plt
import numpy as np

def plot_parabola(a: float, b: float, c: float) -> None:
    """
    Plots the parabola corresponding to the given quadratic function.
    
    Args:
        a (float): Coefficient of x^2.
        b (float): Coefficient of x.
        c (float): Constant term.
    """
    # Generate x values
    x = np.linspace(-10, 10, 400)
    
    # Calculate y values for the parabola
    y = a * x**2 + b * x + c
    
    # Plot the parabola
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f'{a}x^2 + {b}x + {c}')
    plt.title('Parabola Plot')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    plt.legend()
    plt.show()
