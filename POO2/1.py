class Circulo():
  def _init_(self):
    self.__r = 0
  def set_raio(self, r):
    if r > 0: self.__r = r
    else: raise ValueError()
  def get_raio(self):
    return 'O raio do círculo é ' + str(self.__r)
  def calc_area(self):
    return 'A área desse círculo é ' + str((self.__r ** 2 * 3.14))
  def calc_circ(self):
    return 'A circunferência desse círculo é ' + str((self.__r * 2 * 3.14))

class UI():
  @staticmethod
  def main():
    c = Circulo()
    r = int(input('Insira o raio do círculo: '))
    c.set_raio(r)
    print(c.get_raio())
    print(c.calc_area())
    print(c.calc_circ())

UI.main()