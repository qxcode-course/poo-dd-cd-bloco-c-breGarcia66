from Client import Client;

# Criando classe Theater
class Theater:

    # Construtor
    def __init__(self, capacity: int):
        self.__seats: list[Client | None] = [None] * capacity;
    # Fim construtor

    # Método string

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
    def verifyIndex(self, index: int) -> bool:
        try:
            self.getSeats()[index];
            return True;

        except IndexError:
            return False;

    def search(self, name: str) -> int:
        for client in self.getSeats():
            if client is not None and client.getId() == name:
                return self.getSeats().index(client);

        return -1;

    # Fim métodos privados do objeto

    # Métodos públicos do objeto
    def reserve(self, id: str, phone: int, index: int):
        client: Client = Client(id, phone);

        try:


            if self.search(id) != -1:
                print('fail: cliente ja esta no cinema');
                return;

            if self.getSeats()[index] is not None:
                print('fail: cadeira ja esta ocupada');
                return;

            self.getSeats()[index] = client;

        except IndexError:
            print('fail: cadeira nao existe');


    def cancel(self, id: str):
        indexSeat =  self.search(id);

        if indexSeat == -1:
            print('fail: cliente nao esta no cinema');
            return;

        self.getSeats()[indexSeat] = None;
        return;
    # Fim métodos públicos do objeto

t = Theater(5);
print(t.getSeats());

t.reserve('carlos', 5555, 2);
print(t.getSeats());

t.reserve('pedro', 4444, 0);
print(t.getSeats());

t.cancel('carlos');
print(t.getSeats());

t.cancel('adriana');
print(t.getSeats());


