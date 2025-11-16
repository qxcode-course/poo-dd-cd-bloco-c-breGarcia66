from Slot import Slot;

# Criando classe VendingMachine

class VendingMachine:
  # Construtor
  def __init__(self, capacity: int = 0):
    self.__slots: list[Slot] = [Slot()] * capacity;
    self.__profit: float = 0.00;
    self.__cash: float = 0.00;
    self.__capacity: int = capacity;
  # Fim construtor


  # Método str
  def __str__(self) -> str:
    strReturn = f'saldo: {self.getCash():.2f}\n';
    for slot in range(self.getCapacity()):
      if slot != self.getCapacity() - 1:
        strReturn += f'{slot} {self.getSlot(slot)}\n';

      else:
        strReturn += f'{slot} {self.getSlot(slot)}';

    return strReturn;
  # Fim método str


  # Método de acesso
  def getSlot(self, index: int) -> Slot | None:
    try:
      return self.__slots[index];
  
    except IndexError:
      return;

  def getProfit(self) -> float:
    return self.__profit;

  def getCash(self) -> float:
    return self.__cash;

  def getCapacity(self) -> int:
    return self.__capacity;
  # Fim método de acesso


  # Método mutante
  def setSlot(self, index: int, name: str, quantity: int, price: float):
    try:
      slot: Slot = Slot(
        name = name,
        quantity = quantity,
        price = price
      );

      self.__slots[index] = slot;

    except IndexError:
      print('fail: indice nao existe');
      return;

  def setCash(self, value: float):
    if value < 0:
      return;
  
    self.__cash = value;
  
  def setProfit(self, value: float):
    if value < 0:
      return;

    self.__profit = value;
  # Fim método mutante


  # Método do objeto
  def clear(self, index: int):
    try:
      self.__slots[index] = Slot();

    except IndexError:
      return;

  def insertCash(self, value: float):
    self.setCash(self.getCash() + value);

  def withdrawCash(self) -> float:
    change: float = self.getCash();
    self.setCash(0);

    print(f'voce recebeu {change:.2f} RS');
    return change;

  def buyItem(self, index: int):
    try:
      chosenItem: Slot | None = self.getSlot(index); 

      if chosenItem is None:
        print('fail: indice nao existe');
        return;

      if chosenItem.getQuantity() == 0:
        print('fail: espiral sem produtos');
        return;

      if self.getCash() < chosenItem.getPrice():
        print('fail: saldo insuficiente');
        return;

      self.setCash(self.getCash() - chosenItem.getPrice());
      self.setProfit(self.getProfit() + chosenItem.getPrice());
    
      chosenItem.setQuantity(chosenItem.getQuantity() - 1);
      print(f'voce comprou um {chosenItem.getName()}');

    except IndexError:
      print('fail: indice nao existe');
      return;

    except AttributeError:
      print('fail: indice nao existe');
      return;
  # Fim método do objeto

# Fim classe VendingMachine
