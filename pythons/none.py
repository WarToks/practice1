from turtle import *
import random
import time
import math

tan_degree = lambda theta:math.tan(math.radians(theta))

n = 1000
def main(k):
    speed(15)
    ht()
    for i in range(k):
        leng = random.randrange(1,1000)/100
        dirc = random.randrange(0,360)
        right(dirc)
        forward(leng)
    done()
    return None


main(10000)
