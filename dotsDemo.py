#Sam Krimmel
#3/1/18
#dotsDemo.py - how to use loops with graphics

from ggame import *

colr = Color(0x00FF00,1)

dot = CircleAsset(5,LineStyle(1,colr),colr)

Sprite(dot)

App().run()