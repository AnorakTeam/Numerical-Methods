import sympy as sp
from regula_falsi import false_position_it_of, false_position_of



if __name__ == "__main__":
    x = sp.Symbol("x")
    f = x**2 - 4
    iterations = 10
    range_a = 1
    range_b = 3
    tolerance = 1e-16

    print( false_position_it_of(f, range_a, range_b, iterations) )
    print( false_position_of(f, range_a, range_b, tolerance) )