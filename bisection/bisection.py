import sympy as sp

# tolerance for the approximations, when comparing a value with zero, instead
# of hardcoding zero this must be used (floating point arithmetic).
tolerance_check = 1e-12


def _initial_setup(f:callable, a:float, b:float) -> callable:
    """
    TODO: document
    """
    x = sp.Symbol("x")
    num_func = sp.lambdify(x, f, 'math')

    if not check_viable_search(num_func, a, b):
        raise ValueError(f"It's not possible to perform a bisection in the given range [{a}, {b}] (root does not exists).")

    return num_func


def check_viable_search(num_func:callable, val1:float, val2:float) -> bool:
    """
    Checks if a bisection search is possible within the given interval.

    The condition for viability is:
        f(val1) * f(val2) < 0
    If the condition holds, the function returns True, meaning there is at least
    one root in the interval. Otherwise, it returns False.

    Args:
        num_func (callable): Function to evaluate. Typically generated with 
            sympy.lambdify, but any callable with a single float input works.
        val1 (float): Lower bound of the interval.
        val2 (float): Upper bound of the interval.

    Returns:
        bool: True if the interval is valid for a bisection search, 
        False otherwise.
    """
    return num_func(val1) * num_func(val2) < 0


def bisection_of(f, a, b, tolerance) -> tuple:
    """
    Performs the bisection method until the interval is smaller than the given tolerance
    or until the function value at the midpoint is close enough to zero.

    Args:
        f (sympy.Expr or callable): Function to evaluate. If a Sympy expression,
            it will be converted to a numeric function with lambdify.
        a (float): Lower bound of the interval.
        b (float): Upper bound of the interval.
        tolerance (float, optional): Stopping tolerance. Defaults to 1e-12.

    Returns:
        tuple[float, float]: A tuple containing:
            - The midpoint approximation of the root.
            - The function value evaluated at that midpoint.

    Raises:
        ValueError: If the interval does not contain a root (no sign change).
    """
    x = sp.Symbol("x")
    num_func = sp.lambdify(x, f, 'math') 
    m = 0

    num_func = None
    try:
        num_func = _initial_setup(f, a, b)
    except ValueError as e:
        print(e)
        return


    evaluation_a = num_func(a)
    while abs((b - a)) / 2 > tolerance:
        m = (a + b) / 2    
        evaluation_m = num_func(m)
        
        if abs(evaluation_m) < tolerance_check:
             return tuple([m, evaluation_m])
        elif evaluation_m * evaluation_a < 0:
            b = m
        else:
            a = m
            evaluation_a = evaluation_m

    m = (a + b) / 2
    evaluation_m = f(m)
    return tuple([m, evaluation_m])



def bisection_it_of(f, a:float, b:float, n:int) -> tuple[float, float]:
    """
    Performs the bisection method with the intended number of iterations.

    Args:
        f (sympy.Expr or callable): Function to evaluate. If a Sympy expression,
            it will be converted to a numeric function with lambdify.
        a (float): Lower bound of the interval.
        b (float): Upper bound of the interval.
        n (int): Number of iterations to perform. Must be greater than zero.

    Returns:
        tuple:
        A tuple containing:
            - The midpoint approximation of the root.
            - The function value evaluated at that midpoint.

    """
    m = 0
    num_func = _initial_setup(f, a, b)

    if n < 1:
        raise ValueError(f"The amount of iterations must be at least one or more, but {n} was given as input.")    


    evaluation_a = num_func(a)
    while n > 0:
        m = (a + b) / 2    
        evaluation_m = num_func(m)

        # this is if we don't want to execute redundant iterations
        # if abs(evaluation_m) < tol_check:
        #     return tuple([m, evaluation_m])
        # elif evaluation_m * evaluation_a < 0:
        if evaluation_m * evaluation_a < 0:
            b = m
        else:
            a = m
            evaluation_a = evaluation_m

        n -= 1
    

    return tuple([m, evaluation_m])

