class Disciplina():
  def _init_(self):
    self.__nome = str()
    self.__n1 = int()
    self.__n2 = int()
    self.__n3 = int()
    self.__n4 = int()
    self.__nf = int()
  def set_nome(self, nome):
    if nome != '': self.__nome = nome
    else: raise ValueError()
  def set_nota1(self, n1):
    if 0 <= n1 <= 100: self.__n1 = n1
    else: raise ValueError()
  def set_nota2(self, n2):
    if 0 <= n2 <= 100: self.__n2 = n2
    else: raise ValueError()
  def set_nota3(self, n3):
    if 0 <= n3 <= 100: self.__n3 = n3
    else: raise ValueError()
  def set_nota4(self, n4):
    if 0 <= n4 <= 100: self.__n4 = n4
    else: raise ValueError()
  def set_nota_final(self, nf):
    if 0 <= nf <= 100: self.__nf = nf
    else: raise ValueError()
      