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
        return 'Teste';
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
        self.getCounter().insert(index, self.getQueue().pop());
# Fim market


m = Market(counterCount = 2);

print(m);
print(m.getCounter());
print(m.getQueue());
