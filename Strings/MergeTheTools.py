def merge_the_tools(string, k):
    y = zip(*[iter(string)] * k)
    for i in y:
        d = dict()
        print(''.join([d.setdefault(c, c) for c in i if c not in d]))
    
    
