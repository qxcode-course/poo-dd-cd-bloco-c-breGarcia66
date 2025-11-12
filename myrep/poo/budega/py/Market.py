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
        filaDeEspera: list[str] = [];
        for customer in self.getQueue():
           filaDeEspera.append(customer.getName());
        
        caixas: list[str | None] = [];
        for caixa in self.getCounter():
            if caixa is None:
                caixas.append(None)
            
            else:
                caixas.append(caixa.getName());
        
        return f'Caixa: {caixas}\n Fila: {filaDeEspera}';
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
        if self.getCounter()[index] is not None:
            
            raise Exception('fail: caixa ocupado');

        try:
            self.getCounter()[index] = self.getQueue().pop(0);

        except IndexError:
            print('fail: sem clientes');
            return;

    def finish(self, index: int):
        if self.getCounter()[index] is None:
            print('fail: caixa vazio');

        try:
            self.getCounter()[index] = None;

        except IndexError:
            print('fail: caixa vazio');

# Fim market
