# Bisection method
# In mathematics, the bisection method is a root-finding
# method that applies to any continuous functions for which
# one knows two values with opposite signs.
# https://en.wikipedia.org/wiki/Bisection_method#Algorithm
#
import math

# Calculate with Binary Search
# tol is the tolerance
# x_l left value
# x_r right value
# x_m middle value
# fm is the evaluation of the function in the middle point


def biseccion(fun, x_l, x_r, tol):
    x_m = (x_r - x_l) / 2
    fm = fun(x_m)
    candidate = math.fabs(fm)
    while candidate > tol:
        x_m = (x_r - x_l) / 2
        fm = fun(x_m)
        candidate = math.fabs(fm)
        if candidate < tol:
            return x_m
        else:
            test = fun(x_l) * fm
            if test > 0:
                x_l = x_m
                # candidate = x_m
            else:
                x_r = x_m
    return x_m


if __name__ == "__main__":
    # x^2 + x - 6
    root = biseccion(lambda x: (x**2 + x - 6), -1, 100, 0.0001)
    print(root)
