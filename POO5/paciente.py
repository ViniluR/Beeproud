import datetime

class Paciente():
  def __init__(self, nome, cpf, tele, nasci):
    self.__nome = str()
    self.__cpf = str()
    self.__tele = str()
    self.__nasci = str()
    self.setnome(nome)
    self.setcpf(cpf)
    self.settelefone(tele)
    self.setnascimento(nasci)
  def setnome(self, nome):
    self.__nome = nome
  def setcpf(self, cpf):
    self.__cpf = cpf
  def settelefone(self, tele):
    self.__tele = tele
  def setnascimento(self, nasci):
    self.__nasci = datetime.datetime(nasci[2], nasci[1], nasci[0])
  def getnome(self, nome):
    return self.__nome
  def getcpf(self, cpf):
    return self.__cpf
  def gettelefone(self, tele):
    return self.__tele
  def getnascimento(self, nasci):
    return self.__nasci
  def Idade(self):
    delta = datetime.datetime.today() - self.__nasci
    return delta
    # anos = dias // 365
    # meses = (dias % 365) // 30
    # return f'{anos} anos e {meses} meses'
  def __str__(self):
    return f'Nome: {self.__nome} | CPF: {self.__cpf} | Telefone: {self.__tele} | Data de nascimento: {self.__nasci}'

class UI:
  @staticmethod
  def main():
    nome = input('Informe seu nome: ')
    cpf = input('Informe seu CPF: ')
    telefone = input('Informe seu telefone: ')
    nascimento = list(map(int, input('Informe sua data de nascimento (DD/MM/AAAA): ').split('/')))
    x = Paciente(nome, cpf, telefone, nascimento)
    print(x.Idade())
    print(str(x))

UI.main()