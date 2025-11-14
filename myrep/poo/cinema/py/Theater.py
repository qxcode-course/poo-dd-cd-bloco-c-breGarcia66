from Client import Client;

# Criando classe Theater
class Theater:

    # Construtor
    def __init__(self, capacity: int):
        self.__seats: list[Client | None] = [None] * capacity;
    # Fim construtor

    # Método string
    def __str__(self) -> str:
        seats = '[' + ' '.join(list(map(lambda client: f'{client}' if client is not None else '-', self.getSeats()))) + ']';

        return f'{seats}';
    # Fim método string

    # Método de acesso
    def getSeats(self) -> list[Client | None]:
        return self.__seats;
    # Fim método de acesso

    # Método mutante
    def setSeat(self, capacity: int):
        self.__seats: list[Client |None] = [None] * capacity;
    # Fim método mutante

    # Métodos privados do objeto
    def __verifyIndex(self, index: int) -> bool:
        try:
            self.getSeats()[index];
            return True;

        except IndexError:
            return False;

    def __search(self, name: str) -> int:
        for client in self.getSeats():
            if client is not None and client.getId() == name:
                return self.getSeats().index(client);

        return -1;
    # Fim métodos privados do objeto

    # Métodos públicos do objeto
    def reserve(self, id: str, phone: int, index: int):
        client: Client = Client(id, phone);

        if self.__verifyIndex(index) == False:
            print('fail: cadeira nao existe');
            return;

        if self.__search(id) != -1:
            print('fail: cliente ja esta no cinema');
            return;

        if self.getSeats()[index] is not None:
            print('fail: cadeira ja esta ocupada');
            return;

        self.getSeats()[index] = client;

    def cancel(self, id: str):
        indexSeat =  self.__search(id);

        if indexSeat == -1:
            print('fail: cliente nao esta no cinema');
            return;

        self.getSeats()[indexSeat] = None;
        return;
    # Fim métodos públicos do objeto
# Fim classe Theater