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

    def search(self, name: str) -> int | None:
        try:
            for client in self.getSeats():
                if client is not None and client.getId() == name:
                    return self.getSeats().index(client);

        except:
            return -1;

    # Fim métodos privados do objeto

c1 = Client('Roger', 5555);
c2 = Client('Pedro', 5555);
c3 = Client('João', 5555);

t = Theater(5);
