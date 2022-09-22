# logs.py
#
# Outputs the value of g(x) = ln(100-x^2) + sqrt(84 - 5x - x^2) at the input x-value.

import math

def g(x):
    return math.log(100 - x**2) + math.sqrt(84 - 5*x - x**2)

x = input("Input the value for x: ")
x = float(x)

if x>-10 and x<=7:
    print("g(" + str(x) + ") = " + str(g(x)))
else:
    print('invalid input, number must be in between -10 and 7, program stopped.')