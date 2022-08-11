#!python3

from turtle import *
#import math
from math import *
import random

# turtle のリファレンス https://docs.python.org/ja/3/library/turtle.html#turtle.shape

def main():

    setup (width=500, height=500, startx=0, starty=0)
    colormode(255)  # 色モードをカラーに
    shape("turtle") # カメ

    for  i in range(1,1000):
        daikei()

    input("完了！ENTERを押してね！")


def daikei():
    # 乱数で決める要素
    b=random.randrange(30,160)  # ∠B 下底と斜辺の狭角
    ab=random.randrange(10,200) # AB 下底
    bc=random.randrange(10,200) # BC 斜辺
    cd=random.randrange(10,200) # CD 上底
    start=random.randrange(0,365) # 書き始めの角度

    #color('red', 'yellow')
    #begin_fill()

    #fillcolor ... カメの色と共通
    fillcolor(  
        random.randrange(0,colormode() )
        , random.randrange(0,colormode() )
        , random.randrange(0,colormode() ))
    
    pencolor(
        random.randrange(0,colormode() )
        , random.randrange(0,colormode() )
        , random.randrange(0,colormode() ))

    # 各辺、角度の計算
    c = 180 - b
    ah = bc * sin( radians(b) ) #高さ
    be = ab * cos( radians(b) )
    ae = be * tan( radians(b))
    ce = bc - be
    acb = degrees( atan( ae / ce) )
    acd = c - acb
    ac = ce / cos ( radians(acb) )
    cf = cd * cos( radians (acd) ) 
    df = cf * tan ( radians(acd) )
    af = ac - cf
    adf = degrees( atan( af / df ) )
    cdf = 90- acd
    d = adf  + cdf 
    da = df / cos( radians(adf) )

    if 0 :
        #print ("∠a     : {}".format(a) )
        print ("∠b     : {}".format(b) )
        print ("∠c     : {}".format(c) )
        print ("∠d     : {}".format(d) )
        print ("∠acd     : {}".format(acd) )
        print ("∠acb     : {}".format(acb) )
        print ("∠adf     : {}".format(adf) )
        print ("∠cdf     : {}".format(cdf) )
        print ("--------------------------")
        print ("ah     : {}".format(ah) )
        print ("--------------------------")
        print ("ab     : {}".format(ab) )
        print ("bc     : {}".format(bc) )
        print ("cd     : {}".format(cd) )
        print ("da     : {}".format(da) )
        print ("ae     : {}".format(ae) )
        print ("cf     : {}".format(cf) )
        print ("df     : {}".format(df) )
        print ("af     : {}".format(af) )

        print ("--------------------------")
        print ("ac     : {}".format(ac) )

    width(5) # 太さ


    #描画 
    left(start)

    #forward(ab)
    for i in range(20):
        #ペン色の指定（ランダム）
        pencolor( 
            random.randrange(0,colormode())
            , random.randrange(0,colormode())
            , random.randrange(0,colormode()))
        forward(ab/20)

    #斜辺 BC
    left( 180 - b )

    #forward(bc)
    for i in range(20):
            #ペン色の指定（ランダム）
        pencolor( int(random.randrange(0,colormode() ))
            ,int(random.randrange(0,colormode() )),
            int(random.randrange(0,colormode() )))
        forward(bc/20)

    #上底 
    left( 180- c ) 

    #forward(cd)
    for i in range(20):
            #ペン色の指定（ランダム）
        pencolor( random.randrange(0,colormode() )
            , random.randrange(0,colormode() )
            , random.randrange(0,colormode() ))
        forward(cd/20)

    #斜辺 DA
    left( 180 - d )

    #forward(da)
    for i in range(20):
            #ペン色の指定（ランダム）
        pencolor( random.randrange(0,colormode() )
            , random.randrange(0,colormode() )
            , random.randrange(0,colormode() ))
        forward(da/20)

    #end_fill() #塗りつぶし終了
    #done()


main()
