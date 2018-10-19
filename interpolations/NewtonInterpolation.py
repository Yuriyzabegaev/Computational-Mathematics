import math
import sympy as sp

from DividedSubtracts import *



class NewtonInterpolation:

    def __init__(self, x: list, f_x: list):
        self.x_list = x
        self.f_x_list = f_x
        self.divided_subtracts = DividedSubtracts(x, f_x)

        self.var = sp.Symbol('x')

        self.polynomial_power = len(self.divided_subtracts[0]) - 1

        self.expression = self.__construct_interpolation()


    def get_polynomial_function(self):
        return sp.lambdify(self.var, self.expression, 'numpy')


    def __construct_interpolation(self) -> sp.Expr:

        d = self.divided_subtracts
        x = self.var
        x_i = self.x_list

        result = 0

        for i in range(0, self.polynomial_power + 1):

            # constructing (x - x0)*(x - x1)*...*(x - xi)
            x_polynomial = 1
            for j in range(0, i):
                x_polynomial *= (x - x_i[j])

            result += x_polynomial * d[0, i]

        result = result.simplify()
        return result


if __name__ == "__main__":
    # Task VI.9.32 a)

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

    # Solution
    n = NewtonInterpolation(x=v_x,
                            f_x=v_f).get_polynomial_function()
    print('difference in extrapolation: ' + str(n(110) -  308745538))
