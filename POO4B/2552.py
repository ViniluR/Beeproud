while True:
  try:
    n, m = map(int, input().split())
    tabu = []
    saida = []
    for x in range(n):
      newline = list(map(int, input().split()))
      ltab = []
      for s in range(m):
        ltab.append(0)
      if newline[1] == 1:
        ltab[0] += 1
      if newline[m-2] == 1:
        ltab[m-1] = 1
      for y in range(1, m-1):
        ltab[y] = 0
        if newline[y-1] == 1:
          ltab[y] += 1
        if newline[y+1] == 1:
          ltab[y] += 1
      tabu.append(newline)
      saida.append(ltab)
    if n > 1:
      for z in range(m):
        if tabu[1][z] == 1:
          saida[0][z] += 1
      for z in range(m):
        if tabu[n-2][z] == 1:
          saida[n-1][z] += 1
      for i in range(1, n-1):
        for o in range(m):
          if tabu[i-1][o] == 1:
            saida[i][o] += 1
          if tabu[i+1][o] == 1:
            saida[i][o] += 1
    for i in range(n):
      for o in range(m):
        if tabu[i][o] == 1:
          saida[i][o] = 9
    for i in range(n):
      linha = ''.join(map(str, saida[i]))
      print(linha)
  except EOFError:
    break