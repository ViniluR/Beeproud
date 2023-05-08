import math

class Circulo():
  def _init_(self):
    self.r = 0
  def calc_circ_area(self):
    area = math.pi * self.r ** 2
    circ = 2 * math.pi * self.r
    return f'Área = {area} / Circunferência = {circ}'

x = Circulo()
x.r = float(input())
print(x.calc_circ_area())