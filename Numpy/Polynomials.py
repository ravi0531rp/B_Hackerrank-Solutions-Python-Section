import numpy
a = numpy.array(input().split(), float)
b = float(input())
print(numpy.polyval(a, b))
