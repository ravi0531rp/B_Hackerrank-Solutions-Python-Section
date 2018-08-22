import numpy

a, b, c = map(int, input().split())
z1 = [input().strip().split() for _ in range(a)]
z2 = [input().strip().split() for _ in range(b)]
z11 = numpy.array(z1, int)
z22 = numpy.array(z2, int)
print(numpy.concatenate((z11, z22), axis=0))
