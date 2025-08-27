import sympy as sp
from bisection import bisection_of, bisection_it_of



if __name__ == "__main__":
    x = sp.Symbol("x")
    f = -0.5*x**2 + 2.5*x + 4.5
    iterations = 90
    range_a = 5
    range_b = 10
    tolerance = 1e-16

    print( bisection_it_of(f, range_a, range_b, iterations) )
    print( bisection_of(f, range_a, range_b, tolerance) )