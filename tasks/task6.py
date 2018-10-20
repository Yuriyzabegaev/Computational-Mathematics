import sympy as sp

from GaussIntegration import gauss_method


if __name__ == "__main__":
    x = sp.Symbol('x')
    f_x = sp.sin(100 * x) * sp.exp(-x ** 2) * sp.cos(2 * x)
    print(gauss_method(f_x, x, 0, 3, 200))
    # 100 - 0.032053229427044506
    # 50 - 0.22444300351573884
