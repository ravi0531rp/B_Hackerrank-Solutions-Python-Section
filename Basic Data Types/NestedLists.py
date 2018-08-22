sheet = {}
a=[]
for _ in range(int(input())):  # range n
    name = input()
    score = float(input())
    sheet[name] = score
vals = sorted(set(sheet.values()))
for x in sheet.keys():
    if sheet[x] == vals[1]:
        a.append(x)
a=sorted(a)
for x in a:
    print(x)
