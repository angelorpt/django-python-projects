# comentário de 1 linha

"""
Comentário
de
muitas
linhas
"""


# Tipos Primitivos
idade = 14
saldo = 30.5
nome = "Nome"
isSaved = True
vazio = None

print(idade)
print(type(idade))

print(saldo)
print(type(saldo))

print(nome)
print(type(nome))

print(isSaved)
print(type(isSaved))

print(vazio)
print(type(vazio))

# Regras

# Padrão snake_case para variáveis
valor_total = 10.5

# sem acentos
# não pode começar com número
# não pode usar espaço
# usa underline

# tipagem dinâmica e fortemente tipado

# Listas

frutas = ["maçã", "banana", "laranja", "abacaxi"]
print(frutas)
print(type(frutas))
print(frutas[0])
print(frutas[2])

frutas[3]="abacate"
print(frutas[3])


# Tuplas
## São imutáveis

coord = (100.25, 400)
print(coord)
print(type(coord))

# coord[1] = 300 # não pode alterar valor de uma tupla

# DICIONÁRIOS
# São coleções não ordenadas de pares, chave e valor.
# Muito usados para representar objetos e estruturas nomeadas

pessoa = {
  "nome": "Fulano",
  "idade": 30,
  "altura": 1.75,
  "isStudent": True
}
print(pessoa)
print(pessoa["nome"])
pessoa["idade"] = 31
print(pessoa)

# SETS

"""
São coleções ordenadas de itens únicos.
Sem elementos duplicados
São usados para operação de união, interceção, etc.
"""

numeros = {2,3,5,3,2,1}
print(numeros)


# OPERADORES

numero = 10
print(numero + 20) # soma
print(numero - 20) # subtração
print(numero * 20) # multiplicação
print(numero / 20) # divisão
print(numero // 20) # divisão inteira
print(numero % 20) # módulo
print(numero ** 20) # potência

# OPERADORES CONDICIONAIS
# OPERADORES DE COMPARAÇÃO
print(numero > 10) # maior que
print(numero < 10) # menor que
print(numero >= 10) # maior ou igual que
print(numero <= 10) # menor ou igual que
print(numero == 10) # igual a
print(numero != 10) # diferente de

# OPERADORES LÓGICOS
print(numero > 10 and numero < 20) # E
print(numero > 10 or numero < 20) # OU
print(not (numero > 10)) # NÃO


idade = 20
tem_habilitacao = True

if (idade >= 18 and tem_habilitacao):
    print("Pode dirigir")
elif (idade > 18 and not tem_habilitacao):
    print("Não pode dirigir, não tem habilitação")
else:
    print("Não pode dirigir")

# ESTRUTURA DE REPETIÇÃO

"""
Itera sobre os elementos de uma lista, tupla, string, dicionário ou range()
"""

nomes = ['Maria', 'João', 'Pedro', 'Ana']

print("\nnomes")
for nome in nomes:
    print(nome)

print("\nrange(5)")
for i in range(5):
    print(i)

print("\nrange(1, 6)")
for i in range(1, 6):
    print(i)

print("\nrange(1, 6, 2)")
for i in range(1, 6, 2):
    print(i)

print("\nrange(6, 1, -1)")
for i in range(6, 1, -1):
    print(i)

# Use enumarate para iterar sobre os elementos de uma lista, tupla, string, dicionário ou range()
print("\nenumerate(nomes)")
for i, nome in enumerate(nomes):
    print(i, nome)


# Estrutura de Repetição | Match Case
"""
Alternativa moderna ao switch
Estrutura introduzida no python 3.10 que funciona como uma switch, com suporte a padrões
"""

status_code = 404

match status_code:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Internal Server Error")
    case _:
        print("Unknown status code")


# Estrutura de Repetição | Break & Continue
"""
Break faz com que o loop pare imediatamente
Continue faz com que o loop pare imediatamente
"""
print("\nBreak")
for i in range(7):
    if i == 5:
        break
    print(i)

print("\nContinue")
for i in range(7):
    if i == 5:
        continue
    print(i)


# Estrutura de Repetição | Loop while
"""
Repete um bloco de código enquanto uma condição for verdadeira
"""
print("\nwhile (index < 18)")
index = 15
print("index inicial", index)
while (index < 18):
    print("index", index)
    index += 1

print("\nwhile (index > 18)")
index = 23
print("index inicial", index)
while (index > 18):
    print("index", index)
    index -= 1

print("\nDigite a sua senha: 2")
senha = ""
while senha != "2":
  senha = input("Digite a senha: ")
  if senha != "2":
    print("Senha incorreta, tente novamente!")

print("Senha correta")


# FUNÇÕES

"""
Bloco de código reutilizável que realiza uma tarefa específica
São declaradas usando a palavra-chave def
"""

def saudacao(nome):
    print("Olá", nome)

print("\nsaudacao(nome)")
saudacao("Fulano")

# FUNÇÕES | Retorno
"""
Retorna um valor para o chamador
São declaradas usando a palavra-chave def
"""

def somar(a, b):
    return a + b

print("\nsomar(a, b)")
resultado = somar(10, 20)
print(resultado)

# FUNÇÕES | Parametros Dinâmicos (args)

"""
Descrição: Parametros dinamicos sao parametros que podem receber qualquer numero de argumentos
Usa-se * para desempacotar argumentos de uma tupla ou lista
"""

def soma_varios_parametros(*args):
  soma = 0
  for numero in args:
    soma += numero
  return soma

resultado = soma_varios_parametros(10, 20, 30, 40, 50)
print("args | soma_varios_parametros(10, 20, 30, 40, 50)")
print(resultado)

# FUNÇÕES | Parametros Dinâmicos (kwargs)

"""
Descrição: Parametros dinamicos sao parametros que podem receber qualquer numero de argumentos nomeados
Usa-se ** para desempacotar argumentos de um dicionario
"""

def mostrar_info(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

kwargs = {"nome": "Fulano", "idade": 20, "cidade": "São Paulo"}
print("\nmostrar_info(**kwargs) chamada desempacotando os argumentos")
print(type(kwargs))
print(str(kwargs))
mostrar_info(**kwargs)

# FUNÇÕES | Docstring

"""
Docstring é uma string que é definida logo após a definição de uma função
Serve para documentar o que a função faz
"""

def saudacao(nome):
    """
    Docs String da função saudação: Saudacao de boas vindas
    """
    print("Olá", nome)

print("\nsaudacao(nome).__doc__")
print(saudacao.__doc__)

# Funções | Lambda

# Ex. sem lambda
def quadrado(x):
    return x ** 2

print("\nex. sem lambda | def quadrado(x): return x ** 2")
print(quadrado(10))

# Ex. com lambda
quadrado = lambda x: x ** 2
print("\nex. com lambda | quadrado = lambda x: x ** 2")
print(quadrado(10))

# FUNÇÕES | Lambda
"""
Lambda é uma função anônima que pode ter qualquer número de argumentos, mas apenas uma expressão.
São declaradas usando a palavra-chave lambda
"""

somar = lambda a, b: a + b
print("\nsomar(a, b)")
print(somar(10, 20))

# LAMBDA | Filter
"""
Filter é uma função que cria uma nova lista com os elementos de uma lista que satisfazem uma condição.
São declaradas usando a palavra-chave lambda
"""

idades = [10, 20, 30, 40, 50]
print("\nfilter | idades = [10, 20, 30, 40, 50]")
print(list(filter(lambda x: x > 18, idades)))

# LAMBDA | Map
"""
Mapeia os elementos de uma lista para uma nova lista.
São declaradas usando a palavra-chave lambda
"""

numeros = [1, 2, 3, 4, 5]
print("\nmap | numeros = [1, 2, 3, 4, 5]")
print(list(map(lambda x: x * 2, numeros)))

# LAMBDA | Reduce
"""
Reduce é uma função que aplica uma função acumuladora aos elementos de uma lista.
São declaradas usando a palavra-chave lambda
"""

from functools import reduce

numeros = [1, 2, 3, 4, 5]
print("\nreduce | numeros = [1, 2, 3, 4, 5]")
print(reduce(lambda x, y: x + y, numeros))

# FUNÇÃO | Funções Anônimas
"""
Funções anônimas são funções que não têm um nome.
São declaradas usando a palavra-chave lambda
"""

somar = lambda a, b: a + b
print("\nfunções anônimas | lambda")
print(somar(10, 20))

# FUNÇÃO | Funções Anônimas | Filter
"""
Filter é uma função que cria uma nova lista com os elementos de uma lista que satisfazem uma condição.
São declaradas usando a palavra-chave lambda
"""

idades = [10, 20, 30, 40, 50]
print("\nfunções anônimas | filter")
print(list(filter(lambda x: x > 18, idades)))

# FUNÇÃO | Funções Anônimas | Map
"""
Mapeia os elementos de uma lista para uma nova lista.
São declaradas usando a palavra-chave lambda
"""

numeros = [1, 2, 3, 4, 5]
print("\nfunções anônimas | map")
print(list(map(lambda x: x * 2, numeros)))

# FUNÇÃO | Funções Anônimas | Reduce
"""
Reduce é uma função que aplica uma função acumuladora aos elementos de uma lista.
São declaradas usando a palavra-chave lambda
"""

from functools import reduce

numeros = [1, 2, 3, 4, 5]
print("\nfunções anônimas | reduce")
print(reduce(lambda x, y: x + y, numeros))

# FUNÇÃO | Função Retornando Função | Closures
"""
Funções que retornam funções
"""
def criar_saudacao(saudacao):
    def saudacao(nome):
        print(saudacao, nome)
    return saudacao

saudacao = criar_saudacao("Olá")
print("\nfunções | função retornando função | closures")
saudacao("Fulano")

# FUNÇÃO | Função Retornando Função | Closures
"""
Funções que retornam funções
"""

def criar_saudacao(saudacao):
    def saudacao(nome):
        print(saudacao, nome)
    return saudacao

saudacao = criar_saudacao("Olá")
print("\nfunções | função retornando função | closures")
saudacao("Fulano")

# FUNÇÃO | Função Retornando Função | Closures
"""
Funções que retornam funções
"""

def criar_saudacao(saudacao):
    def saudacao(nome):
        print(saudacao, nome)
    return saudacao

saudacao = criar_saudacao("Olá")
print("\nfunções | função retornando função | closures")
saudacao("Fulano")
