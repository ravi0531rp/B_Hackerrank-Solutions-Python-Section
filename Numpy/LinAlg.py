import numpy
numpy.set_printoptions(legacy=1.13)
n = int(input())
arr = numpy.array([input().split() for _ in range(n)], dtype=float)
#print(arr)
print(round(numpy.linalg.det(arr),2))
