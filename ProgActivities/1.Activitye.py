# Calculate the value of e^x for any value nEN
# https://www.google.com/search?q=serie+de+euler&tbm=isch&ved=2ahUKEwjmt_Omr5jrAhXHWKwKHce7AycQ2-cCegQIABAA&oq=serie+de+euler&gs_lcp=CgNpbWcQAzICCAAyAggAMgYIABAIEB46BggAEAUQHlDzPliIQmCMQ2gAcAB4AIABeIgBhAOSAQMzLjGYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=V0s1X6awEsexsQXH9464Ag&bih=838&biw=1440&client=firefox-b-d#imgrc=-YCJ_M38ziNyoM
# n = 20
# x = 1,2,... 10
from math import exp as e

def fac(x):
    val = 0
    if x <= 1:
        return 1
    else:
        val = fac(x-1) * x
        return val        


def serie(x):
    limit = 20 
    acu = 1 + x
    # n  
    for i in range(2,limit):
        acu += (x**i) / fac(i)
    return acu

def ite(x):
    for i in range(1,x+1):
        a_value = serie(i)
        r_value = e(i)
        e_v = r_value - a_value

        print('Real Value: ' + str(r_value))
        print('Approximate Value: ' + str(a_value))
        print('Error: ' + str(e_v))

if __name__ == "__main__":
    print(ite(10))







