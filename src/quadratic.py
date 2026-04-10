import numpy as np

def func(x: float, coefficients: tuple[float]) -> float:
    a, b, c = coefficients
    res = a*(pow(x, 2)) + b*x + c
    return res

def solutions(coefficients: tuple[float]) -> tuple[float]:
    a, b, c = coefficients
    x1 = (-b + np.sqrt((pow(b, 2) - (4*a*c)))) / 2*a
    x2 = (-b - np.sqrt((pow(b, 2) - (4*a*c)))) / 2*a
    return x1, x2

a, b, c = 1, 10, 25
x = np.linspace(-100, 100, 1000)
y = func(x, (a, b, c))
alpha, beta = solutions((a, b, c))
vertex = (alpha + beta) / 2

print(f"EQUATION : {a}x² + {b}x + {c} = 0")
print(f"ROOTS : {alpha} & {beta}")
print(f"VERTEX : {vertex}")