class Entrada():
  def _init_(self):
    self.dia = 0
    self.hora = 0
    self.minuto = 0
  def calc(self):
    if self.dia == 'Seg' or self.dia == 'Ter' or self.dia == 'Qui':
      base = 16
    elif self.dia == 'Qua':
      return 'Inteira e meia: R$8,00'
    else:
      base = 20
    if self.hora >= 17:
      base *= 1.5
    return f'Inteira: R${base},00 / Meia: R${int(base/2)},00'

x = Entrada()
x.dia = input('Dia da sessão (Ex: "Ter"): ')
x.hora, x.minuto = map(int, input('Horário da sessão (Ex: "12h30"): ').split('h'))
print(x.calc())