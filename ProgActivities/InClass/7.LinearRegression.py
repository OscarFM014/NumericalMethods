import math


def regresionLinear(x, y, n):
    sumaX = sumaY = sumaXY = sumaX2 = sr = st = 0
    for i in range(n):
        sumaX = sumaX + x[i]
        sumaY = sumaY + y[i]
        sumaXY = sumaXY + x[i] * y[i]
        sumaX2 = sumaX2 + x[i] * x[i]
    xM = sumaX / n
    yM = sumaY / n
    a1 = (n * sumaXY - sumaX * sumaY) / (n * sumaX2 - sumaX**2)
    a0 = yM - a1 * xM
    for i in range(n):
        st = st + (y[i] - yM)**2
        sr = sr + (y[i] - a1 * x[i] - a0)**2
    syx = math.sqrt(sr / (n-2))
    r = math.sqrt((st - sr) / st)
    return a0, a1, r, syx


if __name__ == "__main__":

    x = [1, 2, 3, 4, 5, 6, 7, 8]
    y = [1, 2, 3, 4, 5, 6, 7, 8]
    n = 8

    print(regresionLinear(x, y, n))


# Linda
# Oscar
