n=int(input())
tup = map(int,input().strip().split())
t=tuple(tup)
print(hash(t))
