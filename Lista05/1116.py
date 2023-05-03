n = int(input())

for x in range(n):
    i, o = input().split()
    i = int(i)
    o = int(o)
    if o == 0:
        print('divisao impossivel')
    else:
        ok = i / o
        print(ok)