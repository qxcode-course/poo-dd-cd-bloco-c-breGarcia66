from Lead import Lead;
from Pencil import Pencil;

# Criando método main
def main():
  pencil: Pencil = Pencil(0);
  
  while True:
    line: str = input();
    args: list[str] = line.split(' ');
    print(f'${line}');

    match args[0]:
      case 'init':
        pencil = Pencil(float(args[1]));

      case 'show':
        print(pencil);

      case 'insert':
        lead: Lead =  Lead(
          thickness = float(args[1]),
          hardness = args[2],
          size = int(args[3])
        );
      
        pencil.insert(lead);
      
      case 'pull':
        pencil.pull();
      
      case 'write':
        pencil.write();
      
      case 'remove':
        pencil.remove();

      case 'end':
        break;

      case _:
        print('fail: comando invalido');
# Fim método main

# Execução do método main
main();
# Fim de execução