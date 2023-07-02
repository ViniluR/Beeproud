class Jogador:

  def __init__(self, nome, camisa, gols):
    self.__nome = str()
    self.__camisa = int()
    self.__gols = int()
    self.setnome(nome)
    self.setcamisa(camisa)
    self.setgols(gols)

  def setnome(self, nome):
    if nome != "": self.__nome = nome
    else: raise ValueError()

  def setcamisa(self, camisa):
    if 0 < camisa < 100: self.__camisa = camisa
    else: raise ValueError()

  def setgols(self, gols):
    if gols >= 0: self.__gols = gols
    else: raise ValueError()

  def __str__(self):
    return f'Nome = {self.__nome} | Camisa = {self.__camisa} | Gols = {self.__gols}'


class Time:

  def __init__(self, nome, estado):
    self.__nome = str()
    self.__estado = str()
    self.__jogadores = []
    self.setnome(nome)
    self.setestado(estado)

  def setnome(self, nome):
    if nome != '': self.__nome = nome
    else: raise ValueError()

  def setestado(self, estado):
    if estado != '': self.__estado = estado
    else: raise ValueError()

  def inserir(self, jogador):
    self.__jogadores.append(jogador)

  def listar(self):
    lista = str()

  # def artilheiro(self):
  #   if len(self.__jogadores) == 0: return None
  #   else:
  #     return max(self.__jogadores)


class UI:

  @staticmethod
  def main():
    x = Time('Madrinhas', 'Caótico')
    j1 = Jogador('Sâmia', 13, 3)
    j2 = Jogador('Kauê', 12, 1)
    j3 = Jogador('Vinícius', 24, 7)
    x.inserir(str(j1))
    x.inserir(str(j2))
    x.inserir(str(j3))
    print(x.listar())
    # x.artilheiro()


UI.main()
