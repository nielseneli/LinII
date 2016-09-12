# here is me using numpy as a graphing calculator for surfaces
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
import math


# i made it a function so i can choose what to graph at the bottom and do not
# have to keep commenting and uncommenting things.
def plot_the_thing(which_problem):

    # initialize the plotty things
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # setting variables for each different problem

    # a. {(x, y, x^2 - y^2) | -1 <= x <= 1 and -1 <= y <= 1}
    if which_problem is 'a':
        X = np.arange(-1, 1, 0.1)
        Y = np.arange(-1, 1, 0.1)
        X, Y = np.meshgrid(X, Y)
        Z = X**2 - Y**2

    # b. {(x, y, x^2 + y^2) | -1 <= x <= 1 and -1 <= y <= 1}
    if which_problem is 'b':
        X = np.arange(-1, 1, 0.1)
        Y = np.arange(-1, 1, 0.1)
        X, Y = np.meshgrid(X, Y)
        Z = X**2 + Y**2

    # c. {(x, y, x^3 - 3*x*y^2) | -1 <= x <= 1 and -1 <= y <= 1}
    if which_problem is 'c':
        X = np.arange(-1, 1, 0.1)
        Y = np.arange(-1, 1, 0.1)
        X, Y = np.meshgrid(X, Y)
        Z = X**3 - 3*X*Y**2

    # d. {(y^2 + z^2, y, z)  | -1 <= y <= 1 and -1 <= z <= 1}
    if which_problem is 'd':
        Y = np.arange(-1, 1, 0.1)
        Z = np.arange(-1, 1, 0.1)
        Y, Z = np.meshgrid(Y, Z)
        X = Y**2 + Z**2

    # e. {(cos(t)*cos(s), sin(t)*cos(s), sin(s)) | 0 <= t <= 2*pi and 0 <= s <= pi}
    if which_problem is 'e':
        t = np.linspace(0, 2*np.pi, 50)
        s = np.linspace(0, np.pi, 50)
        X = np.outer(np.cos(t), np.cos(s))
        Y = np.outer(np.sin(t), np.cos(s))
        Z = np.sin(s)

    # f. {(2*cos(t)*cos(s), 3*sin(t)*cos(s), 5*sin(s)) | 0 <= t <= 2*pi and 0 <= s <= pi}
    if which_problem is 'f':
        t = np.linspace(0, 2*np.pi, 50)
        s = np.linspace(0, np.pi, 50)
        X = 2 * np.outer(np.cos(t), np.cos(s))
        Y = 3 * np.outer(np.sin(t), np.cos(s))
        Z = 5 * np.sin(s)

    # g. {((3 + cos(t))*cos(s), (3 + cos(t))*sin(s), sin(t)) | 0 <= t <= 2*pi and 0 <= s <= 2*pi}
    if which_problem is 'g':
        t = np.linspace(0, 2*np.pi, 50)
        s = np.linspace(0, 2*np.pi, 50)
        X = np.outer(3 + np.cos(t), np.cos(s))
        Y = np.outer(3 + np.cos(t), np.sin(s))
        Z = np.sin(t)

    # h. {(cos(t), sin(t), s) | 0 <= t <= 2*pi, 0 <= z <= 1}
    # TODO: fix
    if which_problem is 'h':
        t = np.linspace(0, 2*np.pi, 50)
        s = np.linspace(0, np.pi, 50)
        X = np.cos(t)
        Y = np.sin(t)
        Z = s


    # i. {((3 + sin(t) + cos(s))*cos(2t), (3 + sin(t) + cos(s))*sin(2t), sin(s) + 2*cos(t)) | 0 <= t <= 2*pi and 0 <= s <= 2*pi}
    if which_problem is 'i':
        t = np.linspace(0, 2*np.pi, 50)
        s = np.linspace(0, 2*np.pi, 50)
        X = np.outer(3 + np.sin(t) + np.cos(s), np.cos(2*t))
        Y = np.outer(3 + np.sin(t) + np.cos(t), np.sin(2*t))
        Z = np.sin(s) + 2*np.cos(t)


    # CALLING GRAPHING THINGS
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1)
    plt.show()

if __name__ == "__main__":
    plot_the_thing('i')
