# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 20:33:42 2020

@author: AkoyaHome
"""
from matplotlib import pyplot as plt

Sel_x = []
def step1():
    Sel_x.clear()
    data = make_data()
    fig_cur = plot_figure(data)
    fig = fig_cur[0]
    cursor = fig_cur[1]
    cid1 = fig.canvas.mpl_connect('button_press_event', onclick_default)
    cid2 = fig.canvas.mpl_connect('close_event', step1_end )    
    print('cid1 = ', cid1)
    return(cid1, cid2, cursor)


def make_data():
    from numpy import arange
    # create data , notes = file name ; x and y tulps - elements could not be changed  
    notes = 'text' 
    # make a list from 0 to 100 with step 1
    x = arange(0, 100, 1.1)
    y = ((x-50)*(x-50))
    data = [notes, x, y]
    return (data)

def plot_figure(data):
    from matplotlib.widgets import Cursor
    # switch on interactive regime 
    plt.ion()
    # make figure window 
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, facecolor='#FFFFCC')
    # plot data with blue 'b' circles 'o'
    ax.plot(data[1], data[2], 'bo')
   
    
    # jenerate cursor
    cursor = Cursor(ax, useblit=True, color='red', linewidth=2)
#    plt.show() #the command is not suitable for intercative regime (works only ones)
    return (fig, cursor)
#    return(cursor)

def onclick_default(event):
        ######################################################################
          # origenal print function from Matplotlib documantation
          # used for debaging 
          print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
              ('double' if event.dblclick else 'single', event.button,
               event.x, event.y, event.xdata, event.ydata)) 
          Sel_x.append(event.xdata)
          
def step1_end(event):
    print('Sel_x=', Sel_x)




     