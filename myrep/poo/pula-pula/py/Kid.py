# Criando calsse Kid
class Kid:
  # Construtor
  def __init__(self, name: str, age: int):
    self.__name: str = name;
    self.__age: int = age;
  # Fim construtor

  # Método str
  def __str__(self) -> str:
    return f'{self.getName()}:{self.getAge()}';
  # Fim método str

  # Método de acesso
  def getName(self) -> str:
    return self.__name;

  def getAge(self) -> int:
    return self.__age;
  # Fim método de acesso

  # Método mutante
  def setName(self, name: str):
    self.__name = name;

  def setAge(self, age: int):
    self.__age =  age;
  # Fim método mutante
# Fim classe Kid