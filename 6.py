n, m = input().split(sep=':')
if int(n) < int(m):
    print(2)
elif int(m) < int(n):
    print(1)
else:
    print(0)