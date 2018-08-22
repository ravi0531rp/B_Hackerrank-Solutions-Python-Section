n, m = map(int,input().split())
pattern = [('.|.'*(2*i - 1)).center(m, '-') for i in range(1,n//2 +1)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))
