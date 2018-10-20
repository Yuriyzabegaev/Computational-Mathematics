import sympy as sp
import math

def simple_iteration_root_searcher(variable: sp.Symbol,
                                   func: sp.Expr,
                                   bottom_bound: float,
                                   top_bound: float,
                                   error: float) -> float:

    assert top_bound > bottom_bound

    x_0 = (top_bound + bottom_bound)/2
    x = x_0
    fi = sp.lambdify(variable, func, "numpy")
    diff = float('Inf')

    while True:
        x_previous = x
        x = fi(x)
        diff_new = abs(x - x_previous)

        assert diff_new < diff

        diff = diff_new

        if diff <= error:
            return x
