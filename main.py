import numpy as np
import sys
from LinearSpline import *
from QuadraticSpline import *
from NaturalCubicSpline import *
from Not_a_knot_CubicSpline import *
from PeriodicCubicSpline import *
from ClampedCubicSpline import *
print "Enter a number between 1 and 6"
choices_str = """
1. Linear spline
2. Quadratic spline
3. Natural cubic spline
4. Not-a-knot cubic spline
5. Periodic cubic spline
6. Clamped cubic spine
"""
print choices_str

try:
    choice = int(input())
except:
    print "Enter a integer only"
    exit(0)

if choice not in range(1,7): 
    print "Choice",choice,"Not valid"
    exit(0)

methodMap = {
    1: LinearSpline,
    2: QuadraticSpline,
    3: NaturalCubicSpline,
    4: Not_a_knot_CubicSpline,
    5: PeriodicCubicSpline,
    6: ClampedCubicSpline
}
sys.stdout = open("out","w")
methodMap[choice]()