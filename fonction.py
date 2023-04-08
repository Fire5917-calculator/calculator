import numpy as np
import matplotlib.pyplot as plt
from math import *

def plot_function(start, end, step, function):
    function = function.replace("²", "**2")
    function = function.replace("^", "**")
    function = function.replace("sqrt", "np.sqrt")
    function = function.replace("sin", "np.sin")
    function = function.replace('cos', 'np.cos')
    function = function.replace("tan", "np.tan")
    

    

    x = np.arange(start, end, step)
    

    y = eval(function)
    

    plt.plot(x, y)
    plt.axhline(y=0, color='black', linewidth=1)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Courbe de la fonction f(x) = ' + function)
    plt.grid(True)
    plt.show()