import random;

# Definindo classe FOO
class Foo:
    # Contrutor
    def __inti__(self, x: int):
        self.x = x;
    # Fim construtor

    # Método string
    def __str__(self) -> str:
        return f'Foo({self.x})';
    # Fim método string
# Fim Foo

# Criando arrays vazios
listaInt: list[int] = [];
listaFoo: list[Foo] = [];


# Criando lista já preenchida
listaNumerica: list[int] = [1, 2, 3, 4, 5];


# Obtendo tamanho de um array
# usando listaNumerica para obter tamanho
print(len(listaNumerica));


# Adicionando elemento em um array
# usando listaNumerica

# no fim
listaNumerica.append(7);
print(listaNumerica);

# no começo
listaNumerica.insert(0, 0);
print(listaNumerica);

# posição específica
listaNumerica.insert(4, 6);
print(listaNumerica);


# Removendo elemento de um array
# usando listaNumerica

# no fim
removerFim = listaNumerica.pop();
print(listaNumerica);
print(removerFim);

# no começo
removerComeco = listaNumerica.pop(0);
print(listaNumerica);
print(removerComeco);

# posição específica
removerEspecifico = listaNumerica.pop(4);
print(listaNumerica);
print(removerEspecifico);


# Usando Join
listaFrase = ["bom", "dia", "!"]
retornoJoin = " ".join(listaFrase);
print(listaFrase);
print(retornoJoin);


# Criando array em sequência de 0 a n
listaSequencia = list(range(11));
print(listaSequencia);

# Array com valores aleatórios
listaRandom = [random.randint(0, 100) for _ in range(11)];
print(listaRandom);


# Acessando elemento por índice
print(listaNumerica[1]);

