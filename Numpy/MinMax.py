# yaad rakhio , axis zero is vertical axis and axis one is horizontal
import numpy
n, _m = map(int, input().split())
a = numpy.array([input().split() for _ in range(n)], int)
print(a.min(axis=1).max())
