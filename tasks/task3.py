import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

from NewtonMethodForNonlinearSystem import newton_method_for_nonlinear_system
from SimpleIterationMethod import simple_iteration_root_searcher


if __name__ == '__main__':

    # Task 3

    # Input:

    x = sp.Symbol('x')
    y = sp.Symbol('y')

    system = [
        x ** 2 + y ** 2 - 1,
        y - sp.tan(x)
    ]

    error = 10**(-6)

    # Solution:

    # Корни определены графически

    segment1 = [[-1, -.5], [-1, -.5]]
    segment2 = [[.5, 1], [.5, 1]]

    print(newton_method_for_nonlinear_system([x, y], system, segment2, error))
    print(newton_method_for_nonlinear_system([x, y], system, segment1, error))
