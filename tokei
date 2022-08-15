#!/usr/local/bin/python3.9

from PIL import Image, ImageDraw
import sys
from math import *
from datetime import datetime
import time

"""
https://pillow.readthedocs.io/en/stable/
"""

clock_w = 400
clock_h = 300
margins=10

hh=clock_w/2
mh=clock_w / 3 * 2
mh= clock_w/2

def main():
    now=datetime.now()
    fname="./{}_{}.png".format( now.hour,now.minute )
    make_clock(fname)
    time.sleep(1)

def make_clock(fname):
    now=datetime.now()

    im = Image.new("RGB", (clock_w, clock_h), (255, 255, 255))
    d = ImageDraw.Draw(im)

    drawmojiban(d)
    drowhands(d,now)

    im.save(fname, "PNG", optimize=True, quality=80)

def drawmojiban(d):

    d.arc( ( 0 + margins , 0 + margins
        , clock_w - margins 
        , clock_h- margins ) , 0 , 360 , fill="black", width=2 )

    for i in range(60):
        r = (360 / 60) * i #- 90

        ox = clock_w/2
        oy = clock_h/2
        ux = cos(radians(r))
        uy = sin(radians(r) )

        sx= ox + ux  * clock_w / 2 *0.90
        sy= oy + uy * clock_h /2 *0.90

        dx = ox + ux  *  clock_w/2 * 0.85
        dy = oy + uy *  clock_h/2 *0.85

        print ( "({},{})-({},{})".format(sx,sy,dx,dy))

        d.line( [(sx , sy) , (dx , dy)] , fill="black", width=2)

    for i in range(12):
        r = (360 / 12) * i - 90

        ox = clock_w/2
        oy = clock_h/2
        ux = cos(radians(r))
        uy = sin(radians(r) )

        sx= ox + ux * clock_w / 2 *0.90
        sy= oy + uy * clock_h /2 *0.90

        dx = ox + ux * clock_w/2 * 0.75
        dy = oy + uy * clock_h/2 *0.75

        lw=10
#        if i % 4 == 0 :
#            lw=20

        d.line( [(sx , sy) , (dx , dy)] , fill="black", width=lw)
        #print (" ( {} , {} ) - ( {} , {} )".format(sx,sy,dx,dy))





def drowhands(d,now):
    m=now.minute
    h=now.hour

#    if h>12:
#        h-=12

    print (" *** hh:mm = {}:{}".format(h,m))

    drowhands2(d,h,m)
    pass


def drowhands2(d,h,m):
    #shorter one
    r = (360/12) * h + (360/12/60) * m - 90
    dx = clock_w/2 + cos( radians(r) ) * clock_w * 0.25
    dy = clock_h/2 + sin( radians(r) ) *  clock_w *0.25

    ux = cos(radians(r))
    uy = sin(radians(r) )

    sx=clock_w/2 + ux * -clock_w * .10
    sy=clock_h/2 + uy * -clock_h * .10

    d.line( [sx , sy , dx , dy] , fill="black", width=12)
    #print (" ( {} , {} ) - ( {} , {} )".format(sx,sy,dx,dy))


    #longer one
    r = (360 / 60) * m -90
    dx = clock_w/2 + cos( radians(r)) * clock_w * 0.4
    dy = clock_h/2 + sin(radians(r) ) * clock_h * 0.4

    ux = cos( radians(r))
    uy = sin(radians(r) )

    sx=clock_w/2 + ux * -clock_w * .10
    sy=clock_h/2 + uy * -clock_h * .10

    d.line( [sx , sy , dx , dy] , fill="black", width=6)



    #ぽっちん
    ox = clock_w/2
    oy = clock_h/2

    d.arc( ( ox-5,oy-5,ox+5,oy+5 ) , 0 , 360 , fill="white", width=2 )
    #print ("radian ( {} , {} ) - ( {} , {} )".format(sx,sy,dx,dy))


if __name__ == "__main__":
    main()
