from Kid import Kid;

# Criando classe Trampoline
class Trampoline:
  # Construtor
  def __init__(self):
    self.__playing: list[Kid] = [];
    self.__waiting: list[Kid] = [];
  # Fim construtor

  # Método str
  def __str__(self):
    kidsWaiting = ', '.join(list(map(lambda kid: f'{kid}', self.getWaiting())));
    kidsPlaying = ', '.join(list(map(lambda kid: f'{kid}', self.getPlaying())));

    return f'[{kidsWaiting}] => [{kidsPlaying}]';
  # Fim método str

  # Método de acesso
  def getPlaying(self) -> list[Kid]:
    return self.__playing;

  def getWaiting(self) -> list[Kid]:
    return self.__waiting;
  # Fim método de acesso

  # Método do objeto
  def _removeFromList(self, name: str, list: list[Kid]) -> Kid | None:
    for kid in list:
      if kid.getName() == name:
        return list.pop(list.index(kid));

    return;

  def arrive(self, kid: Kid):
    self.getWaiting().insert(0, kid);

  def enter(self):
    self.getPlaying().insert(0, self.getWaiting().pop());

  def leave(self):
    try:
      self.getWaiting().insert(0, self.getPlaying().pop());

    except IndexError:
      return;

  def remove(self, name: str) -> Kid | None:
    playingListReturn = self._removeFromList(name, self.getPlaying());
    waitingListReturn = self._removeFromList(name, self.getWaiting());

    if playingListReturn is not None:
      return playingListReturn;

    elif waitingListReturn is not None:
      return waitingListReturn;

    else:
      print(f'fail: {name} nao esta no pula-pula');
      return;
  # Fim método do objeto
# Fim classe Trampoline
