from Player import Player;

# Criando classe Board
class Board:
  # Construtor
  def __init__(self, nPlayers: int, boardSize: int):
    self.__trapList: list[int] = [];
    self.__players: list[Player] = [Player(x) for x in range(1, nPlayers + 1)];
    self.__running: bool = True;
    self.__boardSize: int = boardSize;
    self.__playerTurn: int = 1;
  # Fim construtor

  # Método str
  def __str__(self) -> str:
    quantityPlayer: int = len(self.getPlayers());
    txtFormated: str = '';

    for numPlayer in range(1, quantityPlayer + 1):
      txtFormated += f'player{numPlayer}: ';

      for pos in range(self.getBoardSize() + 1):
        if pos == self.getPlayers()[numPlayer - 1].getPos():
          txtFormated += str(numPlayer);

        else:
          txtFormated += '.';
         
      txtFormated += '\n';
    
    txtFormated += 'traps__: ';
    for pos in range(self.getBoardSize() + 1): 
      if pos not in self.getTrapList():
        txtFormated += '.'

      else:
        txtFormated += 'x';

    return txtFormated;
  
  # Fim método str

  # Método de acesso
  def getTrapList(self) -> list[int]:
    return self.__trapList;

  def getPlayers(self) -> list[Player]:
    return self.__players;

  def isRunning(self) -> bool:
    return self.__running;

  def getBoardSize(self) -> int:
    return self.__boardSize;

  def getPlayerTurn(self) -> int:
    return self.__playerTurn;
  # Fim método de acesso

  # Método mutante
  def setPlayerTurn(self, value: int):
    self.__playerTurn = value;
  
  def setRunning(self, value: bool):
    self.__running = value;
  # Fim método mutante
  
  # Método do objeto
  def addTrap(self, pos: int):
    if pos == 0:
      print('fail: nao pode colocar traps no inicio');
      return;
   
    if pos < 0 or pos > self.getBoardSize():
      print('fail: nao e possivel adicionar traps fora do escopo do tabuleiro');
      return;
  
    self.getTrapList().append(pos);

  def roll(self, value: int):
      currentPlayer = self.getPlayers()[self.getPlayerTurn() -1];

      def changeTurn():
        if self.getPlayerTurn() == len(self.getPlayers()):
          self.setPlayerTurn(1);

        else:
          self.setPlayerTurn(self.getPlayerTurn() + 1);

      # Condinções para interrupções
      if value < 0 or value > 20:
        print('fail: os valores de rolagem somente podem ir de 1 a 20');
        return;
  
      if self.isRunning() is False:
        print('game is over');
        return;
      # Fim condinções para interrupções
      
      # Condição para sair de uma armadilha;
      if currentPlayer.isFree() is False and value % 2 == 0:
        currentPlayer.setFree(True);
        print(f'player{currentPlayer} se libertou');

        changeTurn();
        return;
  
      elif currentPlayer.isFree() is False and value % 2 != 0:
        print(f'player{currentPlayer} continua preso');

        changeTurn();
        return;

      # Rolagem de dado e condição para rolar o dado      
      currentPlayer.setPos(currentPlayer.getPos() + value);
      
      # Condição para ganhar o jogo
      if currentPlayer.getPos() > self.getBoardSize():
        print(f'player{currentPlayer} ganhou');
        currentPlayer.setPos(self.getBoardSize());
        
        self.setRunning(False);
        return;
      # -
      
      print(f'player{currentPlayer} andou para {currentPlayer.getPos()}');

      # Quando player cair em uma armdilha
      if currentPlayer.getPos() in self.getTrapList():
        currentPlayer.setFree(False);
        print(f'player{currentPlayer} caiu em uma armadilha');
        changeTurn();
        return;
      
      
      # Caso nenhum player caia em uma armadilha ou ganhe o jogo prossegue normal
      else:
        changeTurn();
      # -
    # -

  # Fim método do objeto
# Fim clsse Board
