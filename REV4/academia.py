class Esporte:
  def __init__(self, nome, horario, mensalidade):
    self.__nome = str()
    self.__horario = str()
    self.__mensalidade = float()
    self.setnome(nome)
    self.sethorario(horario)
    self.setmensalidade(mensalidade)

  def setnome(self, nome):
    if nome != '': self.__nome = nome
    else: raise ValueError()

  def sethorario(self, horario):
    if horario != '': self.__horario = horario
    else: raise ValueError()

  def setmensalidade(self, mensalidade):
    if mensalidade > 0: self.__mensalidade = mensalidade
    else: raise ValueError()

  def getmensalidade(self):
    return self.__mensalidade

  def __str__(self):
    return f'{self.__nome} no horário das {self.__horario}. {self.__mensalidade} por mês'

class Academia:
  def __init__(self, nome, endereco):
    self.__nome = str()
    self.__endereco = str()
    self.__esportes = []
    self.setnome(nome)
    self.setendereco(endereco)

  def setnome(self, nome):
    if nome != '': self.__nome = nome
    else: raise ValueError()
      
  def setendereco(self, endereco):
    if endereco != '': self.__endereco = endereco
    else: raise ValueError()

  def inserir(self, esporte):
    self.__esportes.append(esporte)

  def listar(self):
    lista = ''
    for e in self.__esportes:
      lista += f'{str(e)}\n'
    return lista

  def media_mensalidade(self):
    soma = 0
    for esporte in self.__esportes:
      soma += esporte.getmensalidade()
    return soma / len(self.__esportes)

  def __str__(self):
    return f'{self.__nome}, {self.__endereco}'

class UI:
  @staticmethod
  def main():
    x = Academia('Fique torto', 'Rua dos bobos')
    e1 = Esporte('Crossfit', '16h', 220)
    e2 = Esporte('Programar', '2h', 2.50)
    e3 = Esporte('Spining', '15h', 333.33)
    x.inserir(e1)
    x.inserir(e2)
    x.inserir(e3)
    print(x)
    print(x.listar())
    print(f'Média das mensalidades: {x.media_mensalidade():.2f}')

UI.main()