# How to pop a plot window and make it disappear a while after

from pylab import *
import time

x = [1,2,3,4]
y = [2,4,6,8]

ion() # turn the interactive mode ON
plot(x,y)
draw() 
draw() # necessary to display the plot result. Weird but whatever...

time.sleep(5)
close()
