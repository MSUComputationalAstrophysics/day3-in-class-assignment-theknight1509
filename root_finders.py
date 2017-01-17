"""
Purpose:
This program will introduce several methods for finding roots, and test 
the methods with extreme functions and intervals
"""
import numpy as np
import scipy.optimize as sp

def bisection(func, boundary, delta):
    """
    This function test the intervals determined by boundary-points and 
    their midpoint, RECURSIVLY, in order to find a value where 'func' 
    is zero (give or take a 'delta').
    """
    #test that func is function, boundary has two points
    a = boundary[0]
    b = boundary[1]
    if abs(func(a)) < delta:
        #there is a zero in b already
        return a
    elif abs(func(b)) < delta:
        #there is a zero in b already
        return b

    elif func(a)*func(b) > 0:
        #there is no zeros
        print "There was a bug in 'bisection'"
        print "there is no zeros in this interval: [%1.3f, %1.3f]"%(a, b)
        #sys.exit("Exiting")
        return False

    elif func(a)*func(b) < 0:
        #there is at least one zero between a and b
        #find midpoint c
        c = (a+b)/2.0
        if abs(func(c)) < delta:
            #there is a zero in c
            return c
        if func(a)*func(c) < 0:
            #there is a zero between a and c
            return bisection(func,[a,c],delta)
        if func(c)*func(b) < 0:
            #there is a zero between c and b
            return bisection(func,[c,b],delta)

def newton(func, dfunc, x_guess, delta):
    x_next = x_guess - func(x_guess)/dfunc(x_guess)
    if abs(x_next-x_guess) < delta:
        return x_next
    else:
        #make another step with the calculated step as the next next.
        return newton(func,dfunc,x_next,delta)

"""
def secant(func, boundary, x_guess, delta):
    #use newtons method, but with numerical approximated derivate.
    #x_guess = (boundary[0] + boundary[1])/2.0 #midpoint of boundaries
    dx = (boundary[1] - boundary[0])*1e-2 #stepsize
    f_guess = func(x_guess)
    f_deriv_guess = (func(x_guess+dx) - f_guess)/float(dx)
    x_next = x_guess - f_guess/f_deriv_guess
    
    if abs(x_next-x_guess) < delta:
        return x_next
    else:
        #make another step with the calculated step as the next next.
        return secant(func, boundary, x_next, delta)
"""

if __name__ == '__main__':
    import matplotlib.pyplot as pl

    #make some funky functions(with derivatives to test the functions)
    f1 = lambda x: np.sin(10*x)/x + (x-1)**2
    df1 = lambda x: np.cos(x)/x - np.sin(x)/x**2 + 2*(x-4)
    f_forest = lambda x: np.abs(x)**(1/4.0)
    df_forest = lambda x: np.abs(x)**(-3.0/4.0) /4.0
    
    #plot the testing-functions
    pl.figure("test-functions"); pl.grid(True)
    x = np.linspace(-5,5,1000)
    pl.plot(x,f1(x), label="f1")
    #pl.plot(x,f2(x), label="f2")
    pl.legend(loc='best')
    pl.show()
    
    #test the bisection method created by self and by scipy
    first_interval = [0.1,0.6]# [-4,4] doesn't work
    limit = 1e-7
    root_self = bisection(f1, first_interval, limit)
    root_scipy = sp.bisect(f1, first_interval[0], first_interval[1],
                           xtol=limit, rtol=limit)
    print "roots of bisection method, using the self-function and scipy"
    print root_self, root_scipy
    print ""
    
    #test bisection method, newtons method and brents method for Forests func.
    a = -2
    b = 3.0
    interval = [a,b]
    limit = 1e-7
    #these three methods break down
    #root_newton = newton(f_forest, df_forest, a, limit)
    #root_brent = sp.brenth(f_forest, a, b)
    #root_bisect = bisection(f_forest, interval, limit)
    #root_bisect = sp.bisect(f_forest, a,b)
