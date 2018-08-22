n = int(input())
lista = []
for _ in range(n):
    s = input().strip().split()
    command = s[0]
    a = s[1:]
    if command != "print":
        command += "(" + ",".join(a) + ")"
        eval("lista." + command)
    else:
        print(lista)
