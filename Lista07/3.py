def iniciais(nome):
  palavras = nome.split()
  a = ""
  for palavra in palavras:
    a += palavra[0]
  return a

nome = input()
print(iniciais(nome))