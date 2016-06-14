# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 20:22:51 2016

@author: lijiahe
"""
import pylab as pl

x1 = [1, 2, 3, 4, 5]# Make x, y arrays for each graph

y1 = [1, 4, 9, 16, 25]

x2 = [1, 2, 4, 6, 8]

y2 = [2, 4, 8, 12, 16]

plot1 = pl.plot(x1, y1, 'r')# use pylab to plot x and y : Give your plots names

plot2 = pl.plot(x2, y2, 'go')

pl.title('plot of y vs. ')# give plot a title

pl.xlabel('x axis')# make axis labels

pl.ylabel('y axis')

pl.xlim(0.0, 9.0)# set axis limits

pl.ylim(0.0, 30.)

pl.legend([plot1, plot2], ('red line', 'green circles'), 'best', numpoints=1)# make legend

pl.show()# show the plot on the screen
