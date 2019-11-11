from numpy import array
from numpy import arange
from numpy import sin
import matplotlib.pyplot as plt


def stepfunction(input_arr):
    '''
    This is my attempt at making a stepfunction.
    it returns an array of bools. True where input[a] > n, else false
    '''
    # heaviside(input_arr - n, 0) is something i could just use in here,
    # or just use the plain heaviside, looks just like the one in matlab
    # The current implementation of stepfunction is most likely slower than the heaviside function itself. 
    # at the moment, I do not need the increased performance. with small (~1k elements) arrays it is in the ms range difference
    # TODO: when situation occurs where this is too slow, profile and optimize
    output_arr = input_arr > 0
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
    plt.rcParams['figure.figsize'] = [12, 6]
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
    plt.rcParams['figure.figsize'] = [12, 6]
    plt.grid(True)
    plt.show()

    
    
def multiplot(data, labels):
    '''
    pass along a numpy 2d array with the first row being t/n and the rest the response/amplitudo/xt/thing
    and a list of names for all the figures
    '''
    # making sure there are thr right ammount of labels
    if(len(labels) + 1 != len(data)):
        raise IndexError("not enough or too much labels")
        
    colors = ["mediumspringgreen",  "plum", "skyblue", "chartreuse", "lightcoral",
             "orange", "darksalmon", "gold", "lightgreen", "darkgrey", "paleturquoise"]
    
    dmax = 0
    dmin = 0
    # adding lines to the plot    
    for i in range(1, len(data)):
        plt.plot( data[0], data[i], color=colors[i-1], linewidth=2)
        # for axes ranges
        if(min(data[i]) < dmin):
            dmin = min(data[i])
        if(max(data[i]) > dmax):
            dmax = max(data[i])
            
    #some sane configs, such as range of axes, etc  
    plt.grid(True)
    plt.legend(labels)
    plt.rcParams['figure.figsize'] = [12, 6]
    try:
        x_margin = (max(data[0]) - min(data[0])) * 0.05
        y_margin = (dmax - dmin) * 0.05
        plt.xlim(min(data[0]) - x_margin, max(data[0]) + x_margin )
        plt.ylim(dmin - y_margin, dmax + y_margin)
    except ValueError:
        # sometimes it bugs out when exponents are used
        plt.autoscale(enable=True, axis='both', tight=True)

def multiplot2(data, labels):
    '''
    pass along a nested list of [t/xt] or [n/xn] pairs
    Use this when your xaxis does not stay the same length for all lines
    and a list of names for all the figures
    '''
    # making sure there are thr right ammount of labels
    if(len(labels) != len(data)):
        raise IndexError("not enough or too much labels")
    colors = ["mediumspringgreen",  "plum", "skyblue", "chartreuse", "lightcoral",
             "orange", "darksalmon", "gold", "lightgreen", "darkgrey", "paleturquoise"]
    
    xmin = xmax = ymin = ymax = 0
    # adding lines to the plot    
    for i in range(len(data)):
        plt.plot( data[i][0], data[i][1], color=colors[i], linewidth=2)
        
        if ( min(data[i][0]) < xmin):
            xmin = min(data[i][0])
        if (max(data[i][0]) > xmax):
            xmax = max(data[i][0])
        if ( min(data[i][1]) < ymin):
            ymin = min(data[i][1])
        if (max(data[i][1]) > ymax):
            ymax = max(data[i][1])
    
    plt.grid(True)
    plt.legend(labels)
    plt.rcParams['figure.figsize'] = [12, 6]
    try:
        xmargin = (xmax - xmin) * 0.05
        ymargin = (ymax - ymin) * 0.05
        plt.xlim(xmin - xmargin, xmax + xmargin)
        plt.ylim(ymin - ymargin, ymax + ymargin)
    except ValueError:
        # sometimes it bugs out when exponents are used
        plt.autoscale(enable=True, axis='both', tight=True)



def multistem(data, labels):
    '''
    pass along a numpy 2d array with the first row being t/n and the rest the response/amplitudo/xt/thing
    and a list of names for all the figures
    '''
    # making sure there are thr right ammount of labels
    if(len(labels) + 1 != len(data)):
        raise IndexError("not enough or too much labels")
    colors = ["mediumspringgreen",  "plum", "skyblue", "chartreuse", "lightcoral",
             "orange", "darksalmon", "gold", "lightgreen", "darkgrey", "paleturquoise"]

    dmax = 0
    dmin = 0
    for i in range(1, len(data)):
        plt.stem( data[0], data[i], linefmt=colors[i-1], use_line_collection = True, markerfmt=".")
        if(min(data[i]) < dmin): # setting range of axes
            dmin = min(data[i])
        if(max(data[i]) > dmax):
            dmax = max(data[i])
            
    # some configs for the plot        
    plt.grid(True)
    plt.legend(labels)   
    plt.rcParams['figure.figsize'] = [12, 6]
    try:
        x_margin = (max(data[0]) - min(data[0])) * 0.05
        y_margin = (dmax - dmin) * 0.05
        plt.xlim(min(data[0]) - x_margin, max(data[0]) + x_margin )
        plt.ylim(dmin - y_margin, dmax + y_margin)
    except ValueError:
        plt.autoscale(enable=True, axis='both', tight=True)

    
