# Criando classe Slot

class Slot:
  # Construtor
  def __init__(
      self,
      name: str = 'empty',
      price: float = 0.00,
      quantity: int = 0 
  ):
    self.__name: str = name;
    self.__price: float = price;
    self.__quantity: int = quantity;
  # Fim construtor


  # Método str
  def __str__(self) -> str:
    junkFoodNameFormatted = '{:''>7}'.format(self.getName());

    return f'[ {junkFoodNameFormatted} : {self.getQuantity()} U : {self.getPrice():.2f} RS]';
  # Fim método str


  # Método de acesso
  def getName(self) -> str:
    return self.__name;

  def getPrice(self) -> float:
    return self.__price;

  def getQuantity(self) -> int:
    return self.__quantity;
  # Fim método de acesso


  # Método mutante
  def setName(self, name: str):
    self.__name = name;

  def setPrice(self, price: float):
    if price < 0:
      print('fail: preco invalido');
      return;

    self.__price = price;

  def setQuantity(self, quantity: int):
    if quantity < 0:
      print('fail: quantidade invalida');
      return;

    self.__quantity = quantity;
  # Fim método mutante

# Fim classe Slot
