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
    lista = []
    for _ in range(15):
        lista.append(random.randrange(100))
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

#5. Faça um programa que armazene as notas das provas 1 e 2 de 15 alunos. Calcule
#e armazene a média arredondada. Armazene também a situação do aluno: 1-
#Aprovado ou 2-Reprovado. Ao final o programa deve imprimir uma listagem
#contendo as notas, a média e a situação de cada aluno em formato tabulado.
#Utilize quantas listas forem necessárias para armazenar os dados.
def q5():
    nomes = ['Pedro','Lucas','Breno','Eduardo','Jorge','Cacio']
    n1 = [8.4,5.6,4.6,7,10,2.6]
    n2 = [5.8,3,8,4,6,8.3]
    x = 0
    boletim = ''
    for x in range(6):
        if ((n1[x]+n2[x])/2) >= 6:
            boletim += (f'{nomes[x]}\t{n1[x]}\t{n2[x]}\t APROVADO\n')
        else:
            boletim += (f'{nomes[x]}\t{n1[x]}\t{n2[x]}\t REPROVADO\n')
    print(boletim)
    
#6. Construa um programa que permita armazenar o salário de 20 pessoas. Calcular
#e armazenar o novo salário sabendo-se que o reajuste foi de 8%. Imprimir uma
#listagem numerada com o salário e o novo salário. Declare quantas listas forem
#necessárias.
def q6():
    sal = []
    nomes = ['Pedro','Lucas','Breno','Eduardo','Jorge','Cacio','Tiago','Otavio','Leon','Zelia']
    holerite = ''
    for _ in range(10):
        sal.append(random.randrange(1500,3000))
    for x in range(10):
        holerite += (f'{nomes[x]}\t\t{sal[x]}\t\t{sal[x]*0.08+sal[x]}\n')
    print(f'Nome:\t\tSalário Ant.\tSalário At.\n')
    print(holerite)
#7. Crie um programa que leia o preço de compra e o preço de venda de 100 mercadorias
#(utilize listas). Ao final, o programa deverá imprimir quantas mercadorias
#proporcionam:
#• lucro < 10%
#• 10% <= lucro <= 20%
#• lucro > 20%
def q7():
    pcompra = []
    pvenda = []
    nomes = ['Pedro','Lucas','Breno','Eduardo','Jorge','Cacio','Tiago','Otavio','Leon','Zelia']
    lista10 = ''
    lista20 = ''
    lista99 = ''
    for _ in range(10):
        pcompra.append(random.randrange(100,1000))
    for x in range(10):
        pvenda.append(pcompra[x]+random.randrange(200,500))
    for x in range(10):
        lucro = (pvenda[x]*100/pcompra[x])-100
        if lucro < 10:
            lista10 += (f"{nomes[x]} teve lucro de {"{:.2f}".format(lucro)}%\n")
        elif lucro >= 20:
            lista20 += (f"{nomes[x]} teve lucro de {"{:.2f}".format(lucro)}%\n")
        elif lucro > 20:
            lista99 += (f"{nomes[x]} teve lucro de {"{:.2f}".format(lucro)}%\n")
    print(f'COMPRA\tVENDA')
    for x in range(10):
        print(f'{pcompra[x]}\t{pvenda[x]}')
    print(lista10)
    print(lista20)
    print(lista99)   

#8. Construa um programa que armazene o código, a quantidade, o valor de compra
#e o valor de venda de 30 produtos. A listagem pode ser de todos os produtos ou
#somente de um ao se digitar o código. Utilize dicionário como estrutura de dados.
def q8():
    cod = []
    pcompra = []
    pvenda = []
    dic = dict()
    nomes = ['Pedro','Lucas','Breno','Eduardo','Jorge','Cacio','Tiago','Otavio','Leon','Zelia']
    cod = [5166,6516,6598,8417,8245,6829,7985,5218,1258,4268]
    lista = ''
    for x in range(10):
        pcompra.append(random.randrange(100,1000))
        pvenda.append(pcompra[x]+random.randrange(200,500))
        lista += (f'{cod[x]}\t{nomes[x]}\t{pcompra[x]}\t{pvenda[x]}\n')
        dic[cod[x]] = (f'{nomes[x]}\t{pcompra[x]}\t{pvenda[x]}')
    esc = input(f'Você deseja pesquisar o seu produto ? s/n\n')
    if esc == 's':
        resp = input_int(f'Digite o código do produto: ',0,9999)
        print(f'Nome\tCompra\tVenda')
        print(dic[resp])
    elif esc == 'n':
        print(f'Código\tNome\tCompra\tVenda')
        print(lista)
    else:
        print(f'Comando Invalido')
    
    

#9. Faça um programa que leia dois conjuntos de números inteiros, tendo
#cada um 10 elementos. Ao final o programa deve listar os elementos comuns aos
#conjuntos.

#10. Faça um programa que leia uma lista com 10 elementos e obtenha outra lista resultado
#cujos valores são os fatoriais da lista original.
#Imprimir o maior e o menor, sem ordenar, o percentual de números pares e a
#média dos elementos da lista.

#11. Imprimir o maior e o menor, sem ordenar, o percentual de números pares e a
#média dos elementos da lista.

#12. Crie um programa para gerenciar um sistema de reservas de mesas em uma casa
#de espetáculo. A casa possui 30 mesas de 5 lugares cada. O programa deverá
#permitir que o usuário escolha o código de uma mesa (1 a 30) e forneça a
#quantidade de lugares desejados. O programa deverá informar se foi possível
#realizar a reserva e atualizar a reserva. Se não for possível, o programa deverá
#emitir uma mensagem. O programa deve terminar quando o usuário digitar
#o código 0 (zero) para uma mesa ou quando todos os 150 lugares estiverem
#ocupados.

#13. Construa um programa que realize as reservas de passagens áreas de uma companhia.
#O programa deve permitir cadastrar o número de 10 voos e definir a
#quantidade de lugares disponíveis para cada um. Após o cadastro, leia vários
#pedidos de reserva, constituídos do número da carteira de identidade do cliente e
#do número do voo desejado. Para cada cliente, verificar se há possibilidade no
#voo desejado. Em caso afirmativo, imprimir o número da identidade do cliente e
#o número do voo, atualizando o número de lugares disponíveis. Caso contrário,
#avisar ao cliente a inexistência de lugares. A leitura do número 0 (zero) para o voo
#desejado indica o término da leitura de reservas.

#14. Faça um programa que armazene 50 números inteiros em uma lista. O programa
#deve gerar e imprimir uma segunda lista em que cada elemento é o quadrado do
#elemento da primeira lista.

#15. Faça um programa que leia e armazene vários números, até digitar o número
#0. Imprimir quantos números iguais ao último número foram lidos. O limite de
#números é 100.

#16. Crie um programa para ler um conjunto de 100 números reais e informe:
#• quantos números lidos são iguais a 30
#• quantos são maior que a média
#• quantos são iguais a média

#17. Faça um programa que leia um conjunto de 30 valores inteiros, armazene-os em
#um vetor e os imprima ao contrário da ordem de leitura.

#18. Faça um programa que permita entrar com 20 valores numéricos,
# em que podem existir vários elementos repetidos. Gere
#uma lista ordenada que terá apenas os elementos não repetidos.

#19. Suponha uma estrutura de 30 elementos contendo: código e telefone. Faça
#um programa que permita buscar pelo código e imprimir o telefone.

#20. Faça um programa que leia a matrícula e a média de 100 alunos. Ordene da maior
#para a menor nota e imprima uma relação contendo todas as matrículas e médias.

questao = int(input('Questão a ser executada: '))
eval(f'q{questao}()')