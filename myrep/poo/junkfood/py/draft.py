from VendingMachine import VendingMachine;

# Criando método main
def main():
  vendingMachine: VendingMachine = VendingMachine();

  while True:
    line: str = input();
    args: list[str] = line.split(' ');
    print(f'${line}');

    match args[0]:
      case 'init':
        vendingMachine = VendingMachine(int(args[1]));
      
      case 'show':
        print(vendingMachine);
      
      case 'set':
        vendingMachine.setSlot(
          index = int(args[1]),
          name = args[2],
          quantity = int(args[3]),
          price = float(args[4])
        );
      
      case 'limpar':
        vendingMachine.clear(int(args[1]));
      
      case 'dinheiro':
        vendingMachine.insertCash(int(args[1]));
      
      case 'troco':
        vendingMachine.withdrawCash();

      case 'comprar':
        vendingMachine.buyItem(int(args[1]));

      case 'end':
        break;

      case _:
        print('fail: comando invalido');
# Fim método main


# Executanto main
main()
# Fim de execução