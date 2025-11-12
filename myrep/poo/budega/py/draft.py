from Customer import Customer;
from Market import Market;

# Criando método main
def main():
    market: Market = Market(0);

    while True:
        line: str = input();
        args: list[str] = line.split(' ');
        print(f'${line}');

        match args[0]:
            case 'init':
                market = Market(int(args[1]));

            case 'show':
                print(market);

            case 'arrive':
                customer: Customer = Customer(args[1]);
                market.arrive(customer);

            case 'call':
                market.callCustomer(int(args[1]));

            case 'finish':
                market.finish(int(args[1]));

            case 'end':
                break;

            case _:
                print('fail: comando invalido');
# Fim método main

# Executando main
main()
# Fim da execução main