# Criando classe Lead
class Lead:
  # Construtor
  def __init__(self, thickness: float, hardness: str, size: int = 0):
    self.__thickness: float = thickness;
    self.__harndess: str = hardness.upper();
    self.__size: int = 0;
  
    self.setSize(size);
  # Fim construtor

  # Método str
  def __str__(self) -> str:
    return f'[{self.getThickness()}:{self.getHardness()}:{self.getSize()}]';
  # Fim método str

  # Método de acesso
  def getThickness(self) -> float:
    return self.__thickness;

  def getHardness(self) -> str:
    return self.__harndess;

  def getSize(self) -> int:
    return self.__size;
  # Fim método de acesso

  # Método mutante
  def setSize(self, value: int):
    if value < 0 or value > 50:
      print('fail: tamanho invalido para um grafite');
      return;
  
    self.__size = value;
  # Fim método mutante

  # Método do objeto
  def usagePerSheet(self) -> int:
    match self.getHardness():
      case 'HB':
        return 1;
      
      case '2B':
        return 2;
      
      case '4B':
        return 4;
      
      case '6B':
        return 6;

      case _:
        return 0;
  # Fim método do objeto
# Fim classe Lead
