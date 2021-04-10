"""
LAMBDAS - Python
Funções lambda são funções anônimas, o que é nada mais nada menos do que funções sem nome com a intenção de serem usadas apenas uma vez (o que não é uma regra).
Elas podem ter um ou vários argumentos separados por virgula e depois do ":" você define o retorno daquela expressão, o retorno pode ser qualquer expressão ou até mesmo outra função.

Sintaxe de uma função lambda:
lambda <arguments> : <return expression>

Abaixo fiz alguns exemplos utilizando lambda:
"""

#Exemplo simples usando lambda:
soma = lambda x,y: x + y
print(soma(5,3)) #Resultado: 8

print((lambda x,y: x + y)(2,3)) #Resultado: 5

#Exemplo um pouco menos simples de Tabuada com lambda
tabuada = lambda num: str('\n').join([f'{num} x {x} = {num*x}' for x in range(1,11)])
print(tabuada(2))
#ou
print((lambda num: str('\n').join([f'{num} x {x} = {num*x}' for x in range(1,11)]))(2))
"""
Resultado de ambas tabuadas seria:
            2 x 1 = 2
            2 x 2 = 4
            2 x 3 = 6
            2 x 4 = 8
            2 x 5 = 10
            2 x 6 = 12
            2 x 7 = 14
            2 x 8 = 16
            2 x 9 = 18
            2 x 10 = 20
"""
#Como seria em uma função normal:
def funcao_tabuada(num):
    lista = []
    for x in range(1,11):
        lista.append(f'{num} x {x} = {num*x}')
    return print(str('\n').join(lista))
funcao_tabuada(5)
"""
Resultado:
            5 x 1 = 5
            5 x 2 = 10
            5 x 3 = 15
            5 x 4 = 20
            5 x 5 = 25
            5 x 6 = 30
            5 x 7 = 35
            5 x 8 = 40
            5 x 9 = 45
            5 x 10 = 50
"""