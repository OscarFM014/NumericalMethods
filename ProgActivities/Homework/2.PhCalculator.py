# Problem
# Make a Python program that calculates the pH of rainwater,
# starting from a carbon dioxide concentration of 482 ppm.
import math


# The new method of bisection of the class
def newBiseccion(fun, x_l, x_r, tol):
    fl = fun(x_l)
    candidate = x_r
    prev = x_l
    while math.fabs(candidate - prev) > tol:
        candidate = (x_r + x_l) / 2
        fr = fun(candidate)
        test = fl * fr
        if math.fabs(test) < tol:
            prev = candidate
        elif test < 0:
            x_r = candidate
        else:
            x_l = candidate
            fl = fr
    return candidate


# The method of bisection the last class
def lastBiseccion(fun, x_l, x_r, tol):
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


def calH(co, h):
    k1 = 10**-6.3
    kH = 10**-1.4
    k2 = 10**-10.3
    kW = 10**-14
    return ((k1*kH*co) / (10**6 * h)) + ((2 * k2*k1*kH*co)/(10**6*(h**2))) + ((kW/h) - h)


def calPH(co, x_l, x_r, error):
    h = newBiseccion(lambda h: calH(co, h), x_l, x_r, error)
    #h = lastBiseccion(lambda h: calH(co, h), x_l, x_r, error)
    # print(h)
    pH = math.log10(h) * -1
    return pH


if __name__ == "__main__":
    print(">>> PH Calculator <<<")
    co = float(input("Enter the CO: "))
    x_l = float(input("Enter the left range: "))
    x_r = float(input("Enter the right range: "))
    error = float(input("Enter the error: "))

    # This is the results with the last class bisection method
    """
        Enter the CO: 1958
        Enter the left range: 10**-6
        Enter the right range: 0.00001
        Enter the error: 0.00001
        5.34678748622
    """

    # This is the results with the new class bisection method
    """
        Enter the CO: 1958
        Enter the left range: 10**-6
        Enter the right range: 0.00001
        Enter the error: 0.00001
        5.0
    """

    print(calPH(co, x_l, x_r, error))

# Oscar
