# 4 -> Area of a given shape (rectangle, triangle and circle) reading shape and appropriate values from standard input
import math
def calcRectArea(l,w):
    return l*w

def calcTriArea(b,h):
    return 0.5 * b * h

def calcCircArea(r):
    return math.pi * r ** 2

while(True):
    print("1 -> Rectangle, 2 -> Triangle, 3 -> Circle, 4 ->Exit")
    opt=int(input("Enter your choice: "))
    if opt == 1:
        l = float(input("Enter Length: "))
        w = float(input("Enter Width: "))
        area = calcRectArea(l,w)
        print("Area of rectangle is: ",area)
    elif opt == 2:
        b = float(input("Enter Base: "))
        h = float(input("Enter Height: "))
        area = calcTriArea(b,h)
        print("Area of Triangle is: ",area)
    elif opt == 3:
        r = float(input("Enter Radius: "))
        area = calcCircArea(r)
        print("Area of Circle is: ",area)
    elif opt == 4:
        print("Exiting the program...")
        break
    else:
        print("Invalid Choice")

