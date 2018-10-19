from math import pi

import sympy as sp

from SimpleIterationMethod import simple_iteration_root_searcher


if __name__ == '__main__':

    # Task 1

    # Input:

    x = sp.Symbol('x')
    func = sp.exp(x) * sp.sin(x) - 1
    bounds = [-10, 10]
    error = 10**(-6)

    # Solution:

    # функция непрерывна, ее экстремумы на отрезке можно найти аналитически. x = pi / 4 + pi * n, n - целое
    extrema = [-3*pi + pi/4,
               -2*pi + pi/4,
                 -pi + pi/4,
                       pi/4,
                  pi + pi/4,
              2 * pi + pi/4]

    # fi(x) = x = arcsin(e^(-x))
    # |fi'(x)| < 1 на [0, 10] => метод простых итерация сойдется для положительных корней

    fi = sp.asin(sp.exp(-x))

    print('One of roots: ' + str(simple_iteration_root_searcher(x, fi, extrema[4], extrema[5], error=error)))

