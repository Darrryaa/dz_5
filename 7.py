n, m, k = input().split(sep=' ')
if int(n) >= int(m) and int(n) >= int(k):
    print(n)
elif int(m) >= int(n) and int(m) >= int(k):
    print(m)
else:
    print(k)