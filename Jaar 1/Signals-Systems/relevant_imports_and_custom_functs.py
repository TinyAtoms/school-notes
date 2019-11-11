from scipy import signal
from numpy import *
import matplotlib.pyplot as plt

def stepfunction(input_arr, n):
    '''
    This is my attempt at making a stepfunction.
    it returns an array of bools. True where input[a] > n, else false
    IT NEEDS WORK, currently no way to do the -stepfun(t-2) so it's 0 after t=2
    '''
    # heaviside(input_arr - n, 0) is something i could just use in here,
    # or just use the plain heaviside, looks just like the one in matlab
    # The current implementation of stepfunction is most likely slower than the heaviside function itself. 
    # at the moment, I do not need the increased performance. with small (~1k elements) arrays it is in the ms range difference
    # TODO: when situation occurs where this is too slow, profile and optimize
    output_arr = input_arr > n
    return output_arr.astype(int)


def ramp(xvals, delta):
    '''
    My attempt at a ramp/unit impulse function.
    takes an array and a position from where the ramp function starts(delta)
    '''
    unfinished = stepfunction(xvals, delta)
    finished =  xvals * unfinished
    return finished




def plot(xvals, yvals, xlabel="time/sample", ylabel="Amplitude"):
    '''
    My default plot function. I'm lazy. Just send 2 arraylike objects,
    first for the x axis, second for the y axis
    3th and 4th are labels for the axis, but since this is mainly for S&S, they are pretty ok as-is
    ''' 
    plt.plot(xvals, yvals)
    plt.margins(0.5, 0.5)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    try:
        # I seem to be having problems when exponential functions are used to create yvals
        x_margin = (max(xvals) - min(xvals)) * 0.05
        y_margin = (max(yvals) - min(yvals)) * 0.05
        ymin = min(yvals) - y_margin
        ymax = max(yvals) + y_margin
        plt.xlim(min(xvals) - x_margin, max(xvals) + x_margin )
        plt.ylim(ymin, ymax)
    except ValueError:
        plt.autoscale(enable=True, axis='both', tight=True)

    plt.grid(True)
    plt.show()
    
    

def stem(xvals, yvals, xlabel="time/sample", ylabel="Amplitude"):
    '''
    My default plot function. I'm lazy. Just send 2 arraylike objects,
    first for the x axis, second for the y axis
    3th and 4th are labels for the axis, but since this is mainly for S&S, they are pretty ok as-is
    '''
    plt.stem(xvals, yvals, use_line_collection=True)
    plt.margins(0.5, 0.5)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    # so that the plot is slightly larger than the values being plotted
    try:
        # I seem to be having problems when exponential functions are used to create yvals
        x_margin = (max(xvals) - min(xvals)) * 0.05
        y_margin = (max(yvals) - min(yvals)) * 0.05
        ymin = min(yvals) - y_margin
        ymax = max(yvals) + y_margin
        plt.xlim(min(xvals) - x_margin, max(xvals) + x_margin )
        plt.ylim(ymin, ymax)
    except ValueError:
        plt.autoscale(enable=True, axis='both', tight=True)

    plt.grid(True)
    plt.show()

# some settings for better plotting
plt.rcParams['figure.figsize'] = [12, 6]