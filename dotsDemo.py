#Sam Krimmel
#3/1/18
#dotsDemo.py - how to use loops with graphics

from ggame import *

RADIUS = 25

green = Color(0x00FF00,1)

dot = CircleAsset(RADIUS,LineStyle(1,green),green)

for i in range(12): #putting a row of dots
    for j in range(12): #putting columns of dots
        Sprite(dot,(10+(2*RADIUS+10)*i,10+(2*RADIUS+10)*j))

App().run()