import sympy as sp

# Definir un símbolo
x = sp.symbols('x')

# Definir la función f(x) que deseas derivar
f = x**3 + 2*x**2 - 4*x + 7

# Calcular la derivada de f(x) con respecto a x
derivative = sp.diff(f, x)

# Imprimir la derivada
print("Derivada de f(x):", derivative)
