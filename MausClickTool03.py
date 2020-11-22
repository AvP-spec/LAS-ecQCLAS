# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 16:10:40 2020

@author: Pipa
create empty list:
    a=[] a.append(a)
create empty tulpe
    a=() a=b+c
check:
    print(type(a))

"""
from matplotlib import pyplot as plt
from matplotlib.widgets import Cursor

def MCtool():
    # create data , notes = file name ; x and y tulps - elements could not be changed  
    notes = 'text' 
    x = (1.2, 2.2, 3.2, 4.2, 5.2, 6.2, 7.2, 8.2, 9.2, 10.2, 11.2, 12.2, 13.2, 14.2, 15.2, 16.2, 17.2, 18.2, 19.2, 20.2)
    y = (1.3, 2.3, 3.3, 4.3, 5.3, 6.3, 7.3, 8.3, 9.3, 10.3, 11.3, 12.3, 13.3, 14.3, 15.3, 16.3, 17.3, 18.3, 19.3, 20.3)
    data = [notes, x, y]
    
    # plot data
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, facecolor='#FFFFCC')
    ax.plot(data[1], data[2], 'o')
    plt.show()
    
    # jenerate cursor
    cursor = Cursor(ax, useblit=True, color='red', linewidth=2)
    
    # start record maus clicks
    left_clicks = []
    Sel_Index = []
    Sel_x = [] 
    Sel_y = []
    def onclick(event):
        ######################################################################
          # origenal print function from Matplotlib documantation
          # used for debaging 
          #print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          #    ('double' if event.dblclick else 'single', event.button,
          #     event.x, event.y, event.xdata, event.ydata))
          #####################################################################
          # my function
          if event.dblclick:
              fig.canvas.mpl_disconnect(cid)
              print('x of left button clicks =', left_clicks)
          elif event.button == 1:              
              left_clicks.append(event.xdata)
              
              if len(left_clicks)== 1:
                  print('left maus button first time')
                  i = 0
                  while data[1][i] < event.xdata:
                       i = i + 1
                  Sel_Index.append(i)
                  print(' StatIndex =',  i)
              elif len(left_clicks)== 2:
                  print('left maus button second time')
                  i = 0
                  while data[1][i] < event.xdata:
                       i = i + 1
                  Sel_Index.append(i) 
                  print (' StatIndex =',  Sel_Index[0]) 
                  print(' EndIndex =',  Sel_Index[1])
                  print(' minIndex =', min(Sel_Index[0], Sel_Index[1]))
                  for i in range(min(Sel_Index[0], Sel_Index[1]), 
                                 max(Sel_Index[0], Sel_Index[1])):
                      Sel_x.append(data[1][i])
                      Sel_y.append(data[2][i])
                  ax.plot(Sel_x, Sel_y, 'o', 'r')
                  #plt.show()
                  print(' Sel_x =',  Sel_x)
                  left_clicks.clear()
                  Sel_Index.clear()
                  #Sel_x.clear()
                  #Sel_y.clear()
                  
              else : 
                  print('left_clicks x = ', left_clicks)
                  left_clicks.clear()
                  
          elif event.button == 2:
              print('wheel')
          elif event.button == 3:
              print('right maus button') 
          else : print('unknown maus button')

    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    
    # display cursor and maus events
    return(cid, cursor)