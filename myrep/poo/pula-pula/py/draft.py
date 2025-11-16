from Kid import Kid;
from Trampoline import Trampoline;

# Criando método main
def main():
  trampoline: Trampoline = Trampoline();

  while True:
    line: str = input();
    args: list[str] = line.split(' ');
    print(f'${line}');

    match args[0]:
      case 'arrive':
        kid: Kid = Kid(
          name = args[1],
          age = int(args[2])
        );
      
        trampoline.arrive(kid);
      
      case 'show':
        print(trampoline);
      
      case 'enter':
        trampoline.enter();
      
      case 'leave':
        trampoline.leave();
      
      case 'remove':
        trampoline.remove(args[1]);

      case 'end':
        break;

      case _:
        print('fail: comando invalido');
# Fim método main

# Executando main
main()
# Fim de execução