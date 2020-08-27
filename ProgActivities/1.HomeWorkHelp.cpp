#include <iostream>

using namespace std;

double fx(double x)
{
    return (3.0 * (x + 1.0)) * (x - 0.5) * (x - 1.0);
}

double newFx(double x)
{
    double normal = (-0.9 * x * x) + (1.7 * x) + 2.5;
    double derivative = (-1.8 * x) + 1.7;
    cout << "Funcion Normal:   " << normal << endl;
    cout << "Funcion Derivada: " << derivative << endl;

    double division = normal / derivative;
    cout << "Division: " << division << endl;

    double totalX = x - division;
    cout << "Resultado: " << totalX << endl;
    return totalX;
}

int main()
{
    //Problem:
    /*  Using the algorithm seen in class for the bisection method, 
    find the root for the function: f (x) = 3 (x + 1) (x − 12) (x − 1). 
    Consider the interval [−2,0.2] to find the root. You must attach an 
    image with all your calculations */
    double i = -2.0;
    while (i < 0.4)
    {
        cout << "x: " << i << " : " << fx(i) << endl;
        i += 0.2;
    }

    cout << endl;

    //Problem:
    /*  Using the algorithm seen in class for the Newton-Raphson method, 
    calculate the root hand for the function: f (x) = −0.9x2 + 1.7x + 2.5. 
    Use as values x0 = 5, ea = 0.001, maxiter = 5 You must attach a picture 
    with all your calculations. */
    double actual = 5.0;
    double prev = 5.0;
    double iter = 0;
    while (iter < 6)
    {
        cout << "ITERACION: " << iter << endl;
        actual = newFx(prev);
        prev = actual;
        iter++;
        cout << endl;
    }
}