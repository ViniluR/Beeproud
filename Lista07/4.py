def aprovado(nota1, nota2):
  if nota1 + nota2 >= 60:
    return "Aprovado"
  else:
    return "Reprovado"

nota1 = int(input())
nota2 = int(input())
print(aprovado(nota1, nota2))