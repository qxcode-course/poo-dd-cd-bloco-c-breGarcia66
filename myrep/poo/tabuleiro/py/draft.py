from Board import Board;

# Criando método main
def main():
  board: Board = Board(0, 0);
  while True:
    line: str = input();
    args: list[str] = line.split(' ');
    print(f'${line}');

    match args[0]:
      case 'init':
        board = Board(
          nPlayers = int(args[1]),
          boardSize = int(args[2])
        );
      
      case 'show':
        print(board);
      
      case 'roll':
        board.roll(int(args[1]));
      
      case 'addTrap':
        board.addTrap(int(args[1]));

      case 'end':
        break;

      case _:
        print('fail: jogada invalida');
# Fim método main

# Executanto main()
main();
# Fim de execução