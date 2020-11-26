# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 16:10:40 2020

@author: Pipa
create empty list:
    a=[] a.append(a)
create empty tulpe (elememts could not be changed)
    a=() a=b+c
check:
    print(type(a))

"""
from matplotlib import pyplot as plt
from matplotlib.widgets import Cursor
from numpy import arange
# polyfit requares np
import numpy as np

def MCtool():
    # create data , notes = file name ; x and y tulps - elements could not be changed  
    notes = 'text' 
    # make a list from 0 to 100 with step 1
    x = arange(0, 100, 1.1)
    y = ((x-50)*(x-50))
    data = [notes, x, y]
    
    
    # switch on interactive regime 
    plt.ion()
    # make figure window 
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, facecolor='#FFFFCC')
    # plot data with blue 'b' circles 'o'
    line, = plt.plot(data[1], data[2], 'bo')
    #plt.show()-the command is not suitable for intercative regime (works only ones)
    
    # jenerate cursor
    cursor = Cursor(ax, useblit=True, color='red', linewidth=2)
    
    # start record maus clicks
    left_clicks = []
    Sel_Index = []
    Sel_x = [] 
    Sel_y = []
    y_poply = []
    z = []
    def onclick(event):
        ######################################################################
          # origenal print function from Matplotlib documantation
          # used for debaging 
          #print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          #    ('double' if event.dblclick else 'single', event.button,
          #     event.x, event.y, event.xdata, event.ydata))
          ####################################################################
          # my function
          ####################################################################
          if event.dblclick:
              # diconnect the function at double click
              fig.canvas.mpl_disconnect(cid)
              print('x of left button clicks =', left_clicks)
          ####################################################################
          elif event.button == 1:   
              # left button clic, record position
              left_clicks.append(event.xdata)
              # seporate first click
              if len(left_clicks)== 1:
                  print('left maus button first time')
                  i = 0
                  # associate the click position with data via index of the data
                  while data[1][i] < event.xdata:
                       i = i + 1
                  # record the index of the data
                  Sel_Index.append(i)
                  # print(' StatIndex =',  i) # for debugging
                  
              # seporate second  click
              elif len(left_clicks)== 2:
                  print('left maus button second time')
                  i = 0
                  while data[1][i] < event.xdata:
                       i = i + 1
                  Sel_Index.append(i) 
 #                 print (' StatIndex =',  Sel_Index[0])  # for debugging
 #                 print(' EndIndex =',  Sel_Index[1])     # for debugging
 #                 print(' minIndex =', min(Sel_Index[0], Sel_Index[1]))  # for debugging
                  
                  # record the data between click possitions 
                  for i in range(min(Sel_Index[0], Sel_Index[1]), 
                                 max(Sel_Index[0], Sel_Index[1])):
                      Sel_x.append(data[1][i])
                      Sel_y.append(data[2][i])
 #                 print(' Sel_x =',  Sel_x)    # for debagging
                  # make polyfit of the selected data
                  polynom_order = 3
                  z = np.polyfit(Sel_x, Sel_y, polynom_order)
                  # calculate polynome for whole range
                  y_poply.clear()
                  for i in range (0, len(data[1])):
                      #  print ('len(data[1][i]) = ', data[1][i])
                      p = np.polyval(z, data[1][i])
                      y_poply.append(p)
                      
                  # plot selected data on the figure by red 'r' circles 'o'
                  ax.plot(Sel_x, Sel_y, 'ro')
                  # plot calculated polynome
                  Poly, =plt.plot(data[1], y_poply, 'r')
                  Poly.set_data(data[1], y_poply)
                  # re-fresh the graphics
                  fig.canvas.draw()
                  fig.canvas.flush_events()
                 
                  # clean click positions for seporation of the I and II clicks
                  left_clicks.clear()
                  Sel_Index.clear()
              #escape while loop if a click is outside graphic data range   
              else : 
                  print('left_clicks x = ', left_clicks)
                  left_clicks.clear()
          ####################################################################
          #keep an option for the mause wheel        
          elif event.button == 2:
              print('mause wheel')
          ####################################################################
          #clean data on right maus click
          elif event.button == 3:
              print('right maus button') 
              # clean calculaed variables
              Sel_x.clear()
              Sel_y.clear()
              y_poply.clear()
              # clean plot
              plt.cla()
              # plot data again with blue 'b' circles 'o'
              ax.plot(data[1], data[2], 'bo')              
              fig.canvas.draw()
          
          else : print('unknown maus button')   

    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    
    print('polinom coefficients = ', z)# for debagging
    print(' Sel_x =',  Sel_x)    # for debagging

    plt.ioff()
    plt.show()
    
    # display cursor and maus events
    return(cid, cursor, z)

    print('polinom coefficients = ', z)# for debagging