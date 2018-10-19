import sympy as sp
import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt

from DividedSubtracts import *


class SplineInterpolation:

    def __init__(self,
                 x_list: list,
                 f_x_list: list):
        self.x_list = x_list
        self.f_x_list = f_x_list
        self.divided_subtracts = DividedSubtracts(x=x_list,
                                                  f_x=f_x_list)
        self._x = sp.Symbol('x')
        self._chunks_cache = [0] * len(x_list)

        self.__construct_interpolation()

    def __getitem__(self, point: float) -> sp.Expr:

        # get the expression
        e = self.get_equation(point)
        return e

    def __call__(self, point: float) -> float:

        # calculate the function

        func = sp.lambdify(self._x, self[point], 'numpy')
        return func(point)

    def __construct_interpolation(self) -> None:

        # implemented algorithm: https://www.math.ntnu.no/emner/TMA4215/2008h/cubicsplines.pdf

        n = len(self.x_list)

        t = self.x_list
        y = self.f_x_list

        h = lambda i: t[i + 1] - t[i]               # i = 0, ..., n-1
        b = lambda i: self.divided_subtracts[i, 1]  # i = 0, ..., n-1
        v = lambda i: 2 * (h(i - 1) + h(i))         # i = 1, ..., n-1
        u = lambda i: 6 * (b(i) - b(i - 1))         # i = 1, ..., n-1

        # finding z - second derivative coefficients

        tridiagonal_matrix = np.zeros((3, n - 2))
        free_column = np.zeros(n - 2)

        for place_in_row in range (0, n - 2):
            i = place_in_row + 1
            h_i = h(i)

            tridiagonal_matrix[0][place_in_row] = h_i
            tridiagonal_matrix[1][place_in_row] = v(i)
            tridiagonal_matrix[2][place_in_row] = h_i

            free_column[place_in_row] = u(i)

        z = list(la.solve_banded((1, 1), tridiagonal_matrix, free_column))

        z = [0] + z + [0]
        self._z = z


    def get_equation(self, point: float) -> sp.Expr:

        t = self.x_list
        y = self.f_x_list
        var = self._x

        h = lambda i: t[i + 1] - t[i]   # i = 0, ..., n-1

        z = self._z

        # estimating which chunk is requires

        chunk_index = float('Inf')

        if point < t[0]:
            chunk_index = 0
        elif point > t[-1]:
            chunk_index = len(t) - 2
        else:
            for index, x in enumerate(t):
                if x >= point:
                    chunk_index = index - 1
                    break

        i = chunk_index

        if self._chunks_cache[i] is not 0:
            return self._chunks_cache[i]

        chunk = z[i+1]/(6 * h(i)) * (var - t[i])**3 +\
                          z[i]/(6 * h(i)) * (t[i+1] - var)**3 +\
                          (y[i + 1]/h(i) - z[i+1]/6 * h(i)) * (var - t[i]) +\
                          (y[i]/h(i) - h(i)/6 * z[i]) * (t[i+1] - var)

        self._chunks_cache[i] = chunk

        return chunk





if __name__ == '__main__':
    # Task VI.9.32 б)

    # Input
    v_x = [i * 10 for i in range(1, 11)]
    v_f = [92228496.0,
           106021537.0,
           123202624.0,
           132164569.0,
           151325798.0,
           179323175.0,
           203211926.0,
           226545805.0,
           248709873.0,
           281421906.0]
    # x = np.linspace(-4, 4, 50, endpoint=True)
    # y = [math.sin(math.exp(x)) for x in x]
    # f = SplineInterpolation(x, y)
    # x = np.linspace(-4, 4, 400, endpoint=True)
    # y = [f(x) for x in x]
    # plt.plot(x, y, 'r')

    f = SplineInterpolation(v_x, v_f)

    print('difference in extrapolation: ' + str(f(110) - 308745538))


    # x_theory = np.linspace(-4, 4, 400, endpoint=True)
    # y_theory = [math.sin(math.exp(x)) for x in x]
    #
    # plt.plot(x_theory, y_theory, 'b')
    # plt.show()

