#Sam Krimmel
#3/1/18
#dotsDemo.py - how to use loops with graphics

from ggame import *

green = Color(0x00FF00,1)

dot = CircleAsset(5,LineStyle(1,green),green)

for i in range(10): #putting a row of dots
    for j in range(12):
        Sprite(dot,(10+(25*i),15+(30*j)))


App().run()