import numpy

a, b = map(int, input().split())
z = [input().strip().split() for i in range(a)]
array = numpy.array(z, int)
print(array.transpose())
print(array.flatten())
