# Criando classe customer
class Customer:
    # Construtor
    def __init__(self, name: str):
        self.__name = name;
    # Fim construtor

    # Método str
    def __str__(self) -> str:
        return f"{self.getName()}";
    # Fim método str

    # Métodos de acesso
    def getName(self) -> str:
        return self.__name;
    # Fim métodos de acesso

    # Métodos mutantes
    def setName(self, name: str):
        self.__name = name;
    # Fim métodos mutantes
# Fim customer