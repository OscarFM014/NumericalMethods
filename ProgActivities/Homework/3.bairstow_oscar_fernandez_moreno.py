# Bairstow Method
# https://es.wikipedia.org/wiki/M%C3%A9todo_de_Bairstow

import math


def bairstow(a, ed1, ed2, r0, s0, maxiter, n):
    b = []
    c = []
    roots = []
    for i in range(0, n):
        b.append(0)
        c.append(0)
        roots.append(0+0j)

    b.append(0)
    c.append(0)
    iter = 0
    while (iter < maxiter) and n >= 3:
        iter = 0
        ea1 = 1
        ea2 = 1
        r = r0
        s = s0
        while iter < maxiter and (ea1 > ed1 or ea2 > ed2):
            iter = iter + 1
            b[n] = a[n]
            b[n-1] = a[n-1] + r*b[n]

            c[n] = b[n]
            c[n-1] = b[n-1] + r*c[n]

            for i in range(n-2, -1, -1):
                b[i] = a[i] + r * b[i + 1] + s * b[i+2]
                c[i] = b[i] + r * c[i + 1] + s * c[i+2]

            det = c[2] * c[2]-c[3]*c[1]

            if math.fabs(det) > ed1:
                dr = (-b[1] * c[2] + b[0] * c[3]) / det
                ds = (-b[0] * c[2] + b[1] * c[1]) / det
                r = r + dr
                s = s + ds
                if math.fabs(r) > ed1:
                    ea1 = math.fabs(dr / (r+dr))
                if math.fabs(s) > ed1:
                    ea2 = math.fabs(ds / (s+ds))
            else:
                r = r + 1
                s = s + 1
                iter = 0
        c1 = quadratic(-s, -r, 1)
        c2 = quadratic(-s, -r, 1)
        roots[n-1] = c1
        roots[n-2] = c2
        n = n - 2
        for i in range(0, n+1):
            a[i] = b[i+2]
    if n < 3:
        if n == 2:
            c1 = quadratic(a[0], a[1], a[2])
            c2 = quadratic(a[0], a[1], a[2])
            roots[0] = c1
            roots[1] = c2
        else:
            roots[0] = -a[0] / a[1]
    return roots


def quadratic(c, b, a):

    x0 = 0+0j
    x1 = 0+0j
    disc = (b**2)-(4*a*c)
    if disc >= 0:
        val = math.sqrt(disc)
        x0 = (-b+val)/(2*a)+0j
        x1 = (-b-val)/(2*a)+0j
    else:
        val = math.sqrt(-disc)
        x0 = (-b+(val) * 1j)/2*a
        x1 = (-b-(val) * 1j)/2*a
    return x0, x1


if __name__ == "__main__":
    poly = []
    poly.append(4)
    poly.append(0)
    poly.append(-5)
    poly.append(0)
    poly.append(1)

    print(bairstow(poly, 0.0000001, 0.0000001, 0, 0, 100, 4))

# Angela Rodriguez
# Oscar Fernandez
