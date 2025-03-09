from IPython.display import display, Math
import sympy as sp

x = sp.Symbol('x')

equation = sp.Eq(x**2 + 2*x + 1, 0)
latex_equation = sp.latex(equation)

# Display the equation
display(Math(latex_equation))
