import random
from biblioteca import input_int, input_float
'''
Lista de Exercícios referentes a coleções e arquivos em python
'''

#1. Faça um programa que armazene 15 números inteiros em uma lista e depois
#permita que o usuário digite um número inteiro para ser buscado na lista, se
#for encontrado o programa deve imprimir a posição desse número na lista, caso
#contrário, deve imprimir a mensagem: "Nao encontrado!".
def q1():
    lista = ''
    arq = open('arq1.cvs','w')
    for x in range(15)
        if x < 14:
            lista = f'{random.randrange(50)};'
        else:
            lista = f'{random.randrange(50)}\n'
    arq.write = lista
    print(lista, end=' ')
    numero = int(input('Digite um número a ser buscado: '))
    try:
        posicao = lista.index(numero)
    except ValueError:
        print(f'{numero} não localizado na lista')
    else:
        print(f'Localizado na posição: {posicao}')
        
#2. Faça um programa que armazene 10 letras em uma lista e imprima uma listagem
#numerada.
def q2():
    letras = []
    cont = 0
    y = 1
    for _ in range(10):
        letras.append(chr(random.randrange(65,91)))
        cont+= 1
    for x in letras:
        print(f'{y} - {x}')
        y += 1 

#2.1 Faça um programa que peça ao usuário para informar a qtde de caracteres
# para a geração de uma senha aleatória. Ao final o programa deve exibir a
# senha sugerida. (ASCII 40-126)
def q21():
    qtde = input_int('Qtde de caracteres para a senha: ',8,20)
    senha = ''
    for _ in range(qtde):
        senha += (chr(random.randrange(40,127))) 
    print(f'Sua senha gerada é: {senha}')
#3. Construa uma programa que armazene 15 números em uma lista e imprima
#uma listagem numerada contendo o número e uma das mensagens: par ou ímpar.
def q3():
    num = []
    mod = []
    x = 0
    y = 0
    lista = ''
    for x in range(15):
        num.append(random.randrange(0,50))
        mod.append(num[x] % 2)
    for y in range(15):    
        if mod[y] == 0:
            lista += (f'{num[y]} é par\n')
        else:
            lista += (f'{num[y]} é impar\n')
    print(lista)

#4. Faça um programa que armazene 8 números em uma lista e imprima todos os
#números. Ao final, imprima o total de números múltiplos de seis.
def q4():
    x = 0
    z = 0
    num = []
    mult = []    
    lista = ''
    for x in range(8):
        num.append(random.randrange(0,100))
        mult.append(num[x]%6)
    x = 0
    for x in range(8):
        if mult[x] == 0:
            z += 1
            lista += (f'{num[x]}, ')
    x = 0
    for x in range(8):
        print(num[x])
    print(f'Quantos números são multiplos de 6? {z}\nOs números são:{lista}')