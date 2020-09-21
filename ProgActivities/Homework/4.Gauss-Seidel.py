import math


def gauss_seidel(a, b, n, xInv, iMax, tol, relFac):
    x = []
    x = xInv
    for i in range(n):
        dummy = a[i][i]
        if dummy > tol:
            for j in range(n):
                a[i][j] = a[i][j] * dummy
            b[i] = b[i]/dummy

        else:
            return "Error hay un cero en la diagonal"

    for i in range(n):
        suma = b[i]
        for j in range(n):
            if i != j:
                suma = suma - (a[i][j]*x[j])
        xI = suma

    itera = 1
    sentinel = True

    while sentinel == True and (itera < iMax):
        sentinel = False
        for i in range(n):
            old = x[i]
            suma = b[i]
            for j in range(n):
                if i != j:
                    suma = suma - (a[i][j] * x[j])
            x[i] = relFac * suma+(1-relFac)*old
            if (sentinel == False and math.fabs(x[i]) > tol):
                ea = math.fabs((x[i] - old)/x[i])
                # ed no existe WFT
                if ea > tol:
                    sentinel = True
        itera += 1
    return x


if __name__ == "__main__":
     a = [[1, 1, 1, 0, 0, 0],
         [0, -1, 0, 1, -1, 0],
         [0, 0, -1, 0, 0, 1],
         [0, 0, 0, 0, 1, -1],
         [0, 10, -10, 0, -15, -5],
         [5, -10, 0, -20, 0, 0]]
    b = [0,0,0,0,0,200]
    tol = 0.5
    n = 6 
    iMax = 0
    relFac = 0
    xInv = []

    # Linda Nayeli
    # Oscar Fernández 
