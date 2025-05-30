'''
Exercícios sobre os comandos básicos em Python
'''

#1. Faça um programa que imprima o seu nome.
def q01():
    print('João Paulo')

#2. Faça um programa que imprima o produto dos valores 30 e 27.
def prod():
    print(30*27)
#3. Faça um programa que imprima a média aritmética entre os números 5, 8, 12.
def media():
    print((5+8+12)/3)
#4. Faça um programa que leia e imprima um número inteiro.
def leia():
    print(int(input('Digite uma número inteiro')))
#5. Faça um programa que leia dois números reais e os imprima.

def midia():
    a = float(input('Digite um número pertecente ao grupo real'))
    b = float(input('Digite um número pertecente ao grupo real, novamente'))
    print(a)
    print(b)
#6. Faça um programa que leia um número inteiro e imprima o seu
#   antecessor e o seu sucessor.
def ssor():
    x = int(input('Digite uma número inteiro'))
    a = x - 1
    s = x +1
    print('seu antecessor:'+ a +'seu sucessor'+s)
#7. Faça um programa que leia o nome o endereço e o telefone de
#   um cliente e ao final, imprima esses dados.
def lista():
    nome: input('Digite seu nome:')
    end: input('Digite seu endereço:')
    num: int(input('Digite seu número de telefone, apenas números:'))
    print('nome:'+ nome)
    print('end:'+ end)
    print('num:'+ num)

#8. Faça um programa que leia dois números inteiros e imprima a
#   subtração deles.
def sub():
    a = int(input('Digite um número inteiro'))
    b = int(input('Digite um número inteiro, novamente'))
    print(f'A subtração resultante é {a-b}')

#9. Faça um programa que leia um número real e imprima ¼ deste número.
def umq():
    x = float(input('Digite um número real'))
    x = x/4
    print(f'O resuldado é:{x}')
#10. Faça um programa que leia três números reais e calcule a
#    média aritmética destes números. Ao final, o programa deve
#    imprimir o resultado do cálculo.
def mreal():
    a = float(input('Digite um número pertecente ao grupo real'))
    b = float(input('Digite um número pertecente ao grupo real, novamente'))
    c = float(input('Digite um número pertecente ao grupo real, novamente'))
    print(f'A média é: {(a+b+c)/3}')
#11. Faça um programa que leia dois números reais e calcule as
#    quatro operações básicas entre estes dois números, adição,
#    subtração,multiplicação e divisão. Ao final, o programa
#    deve imprimir os resultados dos cálculos.
def oper():
    a = float(input('Digite um número: '))
    b = float(input('Digite um número, novamente: '))
    print(f' Adição: {a+b}\n subtração: {a-b}\n Multiplicação: {a*b}\n Divisão: {a/b} ')
    #12. Faça um programa que leia um número real e calcule o
#    quadrado deste número. Ao final, o programa deve
#    imprimir o resultado do cálculo.
def quad():
    x = float(input('Digite um número real'))
    x = x^2
    print(f'O resuldado é:{x}')
#13. Faça um programa que leia o saldo de uma conta poupança e
#    imprima o novo saldo, considerando um reajuste de 2%.

#14. Faça um programa que leia a base e a altura de um retângulo
#    e imprima o perímetro (base*2 + altura*2) e a área (base * altura).    

#15. Faça um programa que leia o valor de um produto, o percentual
#    do desconto desejado e imprima o valor do desconto e o valor
#    do produto subtraindo o desconto.

#16. Faça um programa que calcule o reajuste do salário de um
#    funcionário. Para isso, o programa deverá ler o salário atual
#    do funcionário e ler o percentual de reajuste. Ao final imprimir
#    o valor do novo salário.

#17. Faça um programa que calcule a conversão entre graus centígrados
#    e Fahrenheit. Para isso, leia o valor em centígrados e calcule
#    com base na fórmula a seguir. Após calcular o programa deve
#    imprimir o resultado da conversão.
#    F = (9 x C + 160) / 5

#18. Faça um programa que calcule a quantidade de litros de combustível
#    consumidos em uma viagem, sabendo-se que o carro tem autonomia de
#    12 km por litro de combustível. O programa deverá ler o tempo
#    decorrido na viagem e a velocidade média e aplicar as fórmulas:
#    D = T x V       L = D / 12
#    Em que:
#    • D = Distância percorrida em horas
#    • T = Tempo
#    • V = Velocidade média
#    • L = Litros de combustível consumidos
#    Ao final, o programa deverá imprimir a distância percorrida e a
#    quantidade de litros consumidos na viagem.

#19. Faça um programa que calcule o valor de uma prestação em atraso.
#    Para isso, o programa deve ler o valor da prestação vencida, a
#    taxa periódica de juros e o período de atraso. Ao final, o
#    programa deve imprimir o valor da prestação atrasada, o período
#    de atraso, os juros que serão cobrados pelo período de atraso, o
#    valor da prestação acrescido dos juros. Considere juros simples.

#20. Faça um programa que efetue a apresentação do valor da conversão
#    em real (R$) de um valor lido em dólar (US$). Para isso, será
#    necessário também ler o valor da cotação do dólar.