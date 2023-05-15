class Viagem():
  def _init_(self):
    self.d = 0
    self.h = 0
    self.m = 0
  def calc(self):
    kmh = self.d/((self.h*60 + self.m)/60)
    return f'{str(kmh)} hm/h'

x = Viagem()
x.d = float(input('Quantidade de quilômetros rodados: '))
x.h = float(input('Quantidade de horas: '))
x.m = float(input('Quantidade de minutos: '))
print(x.calc())