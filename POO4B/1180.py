n = int(input())
s = []
x = input().split()
o = x[0]
for y in range(n):
  if int(x[y]) < int(o):
    o = x[y]
    a = y
print(f'Menor valor: {o}')
print(f'Posicao: {a}')