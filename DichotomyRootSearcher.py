import numpy as np
import sympy as sp
from numpy import sign


def dichotomy_root_searcher(var: sp.Symbol,
                            func: sp.Expr,
                            boundaries: (float, float),
                            error: float = 10**(-6)) -> float:

    f = sp.lambdify(var, func, 'numpy')
    (a, b) = boundaries

    while 1:
        middle = (a + b)/2
        if sign(f(a)) != sign(f(middle)):
            b = middle
        elif sign(f(middle)) != sign(f(b)):
            a = middle

        if b - a <= error:
            return middle


