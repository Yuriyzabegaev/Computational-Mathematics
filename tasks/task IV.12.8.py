import math
import sympy as sp

from SimpleIterationMethod import simple_iteration_root_searcher

if __name__ == "__main__":
    # Task IV.12.8 б)

    # Input:
    x = sp.Symbol('x')
    f_x =  x * sp.exp(-x**2)
    error = 10**(-3)

    # Solution
    max_in_f_x = 1/math.sqrt(2)

    fi_x = 0.5 * 1/max_in_f_x *sp.exp(x**2 - 1/2)

    root_1 = simple_iteration_root_searcher(x, fi_x,
                                            bottom_bound=0,
                                            top_bound=max_in_f_x,
                                            error=error)

    fi_x = sp.sqrt(sp.log(x * 2*sp.sqrt(2) * sp.exp(0.5)))

    root_2 = simple_iteration_root_searcher(x, fi_x,
                                            bottom_bound=max_in_f_x,
                                            top_bound=3,
                                            error=error)

    print(root_2 - root_1)
