import numpy as np
import sympy as sp
import math

from sympy.functions.special.polynomials import legendre as Legendre

from NewtonMethodForNonlinearSystem import newton_method_for_nonlinear_system



def gauss_method(func: sp.Function,
                 variable: sp.Symbol,
                 bottom_bound: float,
                 top_bound: float,
                 number_of_points: int,
                 error: float = 10**-6):

    def normalization(func: sp.Function,
                      variable: sp.Symbol,
                      bottom_bound: float,
                      top_bound: float) -> (sp.Function, sp.Symbol):
        t = sp.Symbol('t')
        func_normalized = func.subs(variable, (top_bound + bottom_bound + t*(top_bound - bottom_bound))/2)
        return func_normalized, t

    def d_legendre(n: int,
                   point: float):
        t = sp.Symbol('t')
        formula = n/(1 - t**2)*(Legendre(n-1, t) - t * Legendre(n, t))
        return sp.lambdify(t, formula, 'numpy')(point)

    # top and bottom bounds are +1 and -1 respectively
    fi, var = normalization(func, variable, bottom_bound, top_bound)

    # number_of_points == n -- index of Legendre Polynomial
    legendre = Legendre(number_of_points, var)

    # finding roots of legendre polynomial
    x_i_list = []

    for i in range(0, number_of_points):
        x_i_0 = np.sign(4 * i - 1) * math.cos(math.pi * (4 * i - 1)/(4 * number_of_points + 2))
        x_i_list += [newton_method_for_nonlinear_system([var], [legendre], x_0=[x_i_0])[0]]

    # finding weights
    w_i_list = []
    for i in range(0, number_of_points):
        w_i_list += [2/((1 - x_i_list[i]**2) * (d_legendre(number_of_points, x_i_list[i]))**2)]

    # constructing gauss integral
    gauss_integral = 0
    f = sp.lambdify(var, fi, 'numpy')
    for i in range(0, number_of_points):
        gauss_integral += w_i_list[i]*f(x_i_list[i])
    return gauss_integral




if __name__ == "__main__":
    x = sp.Symbol('x')
    f_x = sp.sin(100 * x) * sp.exp(x ** 2) * sp.cos(2 * x)
    print(gauss_method(f_x, x, 0, 3, 3))
