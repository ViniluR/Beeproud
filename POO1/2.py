class Pop():

  def _init_(self):
    self.nome = 0
    self.n1 = 0
    self.n2 = 0
    self.n3 = 0
    self.n4 = 0
    self.final = 0

  def calc_media(self):
    mediap = (self.n1 * 2 + self.n2 * 2 + self.n3 * 3 + self.n4 * 3) / 10
    if mediap < 60:
      mediaf = (mediap + self.final) / 2
      return f'Média parcial = {mediap:.1f} / Média final = {mediaf:.1f}'
    else:
      return f'Média parcial = {mediap:.1f}'


x = Pop()
x.nome = input('Nome da disciplina: ')
x.n1 = int(input())
x.n2 = int(input())
x.n3 = int(input())
x.n4 = int(input())
x.final = int(input())
print(x.calc_media())
