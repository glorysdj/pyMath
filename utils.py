import random
from turtle import *


def get_random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def angle_for_n(n):
    sum = (n - 2) * 180
    avg = sum / n
    angle = 180 - avg
    return angle


def draw_for_n(n, length):
    for j in range(n):
        forward(length)
        right(angle_for_n(n))