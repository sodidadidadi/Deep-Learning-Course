import math
def quadratic(a, b, c):
    p = b * b - 4 * a * c
    if p >= 0 and a != 0:
        x1 = (-b + math.sqrt(p))/(2 * a)
        x2 = (-b - math.sqrt(p))/(2 * a)
        return x1, x2
    elif a == 0:
        x1=x2= -c / b
        return x1
    else:
        return('方程无解')
a = float(input('input a='))
b = float(input('input b='))
c = float(input('input c='))
print(quadratic(a,b,c))
