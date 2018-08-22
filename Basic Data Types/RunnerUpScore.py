if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    #print(arr)
    sor = sorted(arr)
    #print(sor)
    i = n-1
    while sor[i] == sor[-1]:
        i -= 1
        if(sor[i] != sor[-1]):
            break
    print(sor[i])
