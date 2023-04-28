def formatar_nome(nome):
  palavras = nome.split()
  nome = ''
  for palavra in palavras:
    nome += palavra[0].upper()
    nome += palavra[1:].lower()
    nome += ' '
  return nome

nome = input()
print(formatar_nome(nome))
  