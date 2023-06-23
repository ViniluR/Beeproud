m = []
o = input()
for x in range(12):
  m.append([])
  for y in range(12):
    i = float(input())
    m[x].append(i)

s = 0
for z in range(1, 13):
  for a in range(z):
    m[z-1].remove(m[z-1][0])
  s += sum(m[z-1])
  
if o == "S":
  print(f'{s:.1f}')
elif o == "M":
  m = s / 66
  print(f'{m:.1f}')
  