n = int(input())
b = 0
c = 0
r = 0
s = 0

for x in range(n):
    a = input().split()
    i = int(a[0])
    f = str(a[1])
    b = b + i
    if f == 'C':
        c += i
    if f == 'R':
        r += i
    if f == 'S':
        s += i

print(f'''Total: {b} cobaias
Total de coelhos: {c}
Total de ratos: {r}
Total de sapos: {s}''')

u = b / 100

c = c / u
r = r / u
s = s / u

print(f'''Percentual de coelhos: {c:.2f} %
Percentual de ratos: {r:.2f} %
Percentual de sapos: {s:.2f} %''')