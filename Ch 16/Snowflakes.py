# Draw a Koch snowflake
from turtle import *


def koch(a, order):
    if order > 0:
        for t in [60, -120, 60, 0]:
            koch(a/3, order-1)
            left(t)
    else:
        forward(a)

# Test
koch(100, 0)
pensize(3)
speed(1)
koch(100, 2)

