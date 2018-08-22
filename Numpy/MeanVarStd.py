import numpy
numpy.set_printoptions(legacy='1.13')
col, row = map(int, input().split())
arr = numpy.array([input().split() for _ in range(col)], numpy.float)
print(numpy.mean(arr, axis=1))
print(numpy.var(arr, axis=0))
print(numpy.std(arr))
