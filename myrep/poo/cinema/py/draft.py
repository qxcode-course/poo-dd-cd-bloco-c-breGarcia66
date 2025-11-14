from Theater import Theater;

# Criando método main
def main():
  theater: Theater = Theater(0);

  while True:
    line: str = input();
    args: list[str] = line.split(' ');
    print(f'${line}');

    match args[0]:
      case 'init':
        theater = Theater(int(args[1]));
      
      case 'show':
        print(theater);
      
      case 'reserve':
        theater.reserve(
          id = args[1],
          phone = int(args[2]),
          index = int(args[3])
        );
      
      case 'cancel':
        theater.cancel(args[1]);

      case 'end':
        break;

      case _:
        print('fail: comando invalido');

# Executanto main
main();
# Fim execução main

# Fim método main