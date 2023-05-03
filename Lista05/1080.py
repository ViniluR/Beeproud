y = 0
a = 0
for x in range(1,100+1):
    n = int(input())
    if n > y:
        y = n
        a = x
print(y)
print(a)