# Criando classe Player
class Player:
  # Contrutor
  def __init__(self, label: int):
    self.__label: int = label;
    self.__pos: int = 0;
    self.__free: bool = True;
  # Fim construtor

  # Método str
  def __str__(self) -> str:
    return f'{self.getLabel()}';
  # Fim método str

  # Método de acesso
  def getLabel(self) -> int:
    return self.__label;

  def getPos(self) -> int:
    return self.__pos;

  def isFree(self) -> bool:
    return self.__free;
  # Fim método de acesso

  # Método mutante
  def setPos(self, pos: int):
    self.__pos = pos;

  def setFree(self, free: bool):
    self.__free = free;

  def setLabel(self, label: int):
    self.__label = label;
  # Fim método mutante
# Fim classe Player
