from Customer import Customer;

# Criando classe market
class Market:
    # Construtor
    def __init__(self, counterCount: int):
        self.__counter: list[Customer | None] = [None for _ in range(counterCount)];
        self.__queue: list[Customer] = [];
    # Fim construtor
 
    # Método str
    def __str__(self):
        customers = '[' + ', '.join(list(map(lambda customer: customer.getName(), self.getQueue()))) + ']';

        counters = '[' +  ', '.join(list(map(lambda counter:counter.getName() if counter is not None else '-----', self.getCounter()))) + ']';
        
        return f'Caixas: {counters}\nEspera: {customers}';
    # Fim método str

    # Método de acesso
    def getCounter(self) -> list[Customer | None]:
        return self.__counter;

    def getQueue(self) -> list[Customer]:
        return self.__queue;
    # Fim método de acesso

    # Métodos do objeto
    def arrive(self, customer: Customer):
        self.getQueue().append(customer);

    def callCustomer(self, index: int):
        if index > len(self.getCounter()) - 1 or index < 0:
            print('fail: caixa inexistente');
            return;

        if self.getCounter()[index] is not None:
            print('fail: caixa ocupado');
            return;
            #raise Exception('fail: caixa ocupado');

        try:
            self.getCounter()[index] = self.getQueue().pop(0);

        except IndexError:
            print('fail: sem clientes');
            return;

    def finish(self, index: int) -> Customer | None:        
        try:            
            if self.getCounter()[index] is None:
                print('fail: caixa vazio');
                return;

            oldCustomer = self.getCounter()[index];
            self.getCounter()[index] = None;

        except IndexError:
            print('fail: caixa inexistente');
            return;

        return oldCustomer;

# Fim market
