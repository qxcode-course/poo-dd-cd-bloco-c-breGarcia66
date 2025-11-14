# Criando classe Client
class Client:

    # Construtor
    def __init__(self, id: str, phone: int):
        self.__id: str = id;
        self.__phone: int = phone;
    # Fim construtor
    def __str__(self) -> str:
        return f'{self.getId()}:{self.getPhone()}';
    # Método string

    # Fim método string

    # Método de acesso
    def getId(self) -> str:
        return self.__id;

    def getPhone(self) -> int:
        return self.__phone;
    # Fim método de acesso

    # Método mutante
    def setId(self, id: str):
        self.__id = id;

    def setPhone(self, phone: int):
        self.__phone = phone;
    # Fim método mutante
    
# Fim classe Client
