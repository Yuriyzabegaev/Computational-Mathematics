import sympy as sp
import numpy as np
import scipy.linalg as la


def newton_method_for_nonlinear_system(variables: list,
                                       equations: list,
                                       boundaries: [(float, float)] = None,
                                       x_0: list = None,
                                       error: float = 10**(-6)) -> list:

    # http://algowiki-project.org/ru/Метод_Ньютона_для_систем_нелинейных_уравнений

    assert len(variables) == len(equations)

    # calculating W

    val = sp.Matrix(variables)
    func = sp.Matrix(equations)

    jacobi_matrix = func.jacobian(val)
    if x_0 is None:
        x_i = [(a + b)/2 for a, b in boundaries]
    else:
        x_i = x_0

    jacobi_matrix_func = sp.lambdify(variables, jacobi_matrix, 'numpy')
    free_column_func = sp.lambdify(variables, equations, 'numpy')

    counter = 0

    while 1:
        counter += 1
        # calculating W (jacobi matrix)
        W = jacobi_matrix_func(*x_i)
        W_inv= la.inv(W)

        # calculating f (free column)
        f = free_column_func(*x_i)

        # solving differential linear equation system
        delta_x = np.dot(W_inv, f)

        # approximating
        x_i = x_i - delta_x

        # calculating error
        current_error = np.linalg.norm(delta_x)

        if current_error <= error:
            return x_i

