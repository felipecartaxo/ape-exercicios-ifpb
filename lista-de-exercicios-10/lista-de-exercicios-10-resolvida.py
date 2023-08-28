# -*- coding: utf-8 -*-
"""APE 2022.1 - Lista Resolvida - Vetor (Complementar).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tHmr7S8_RE_8J2_OW4hrM3RKJ6D8XSO-

**IFPB - CAMPUS JOÃO PESSOA    
CURSO: SISTEMAS PARA INTERNET     
DISCIPLINA: ALGORITMOS E PROGRAMAÇÃO ESTRUTURADA     
PROFESSORES: CANDIDO EGYPTO / EDEMBERG ROCHA**

# LISTA DE EXERCÍCIOS (RESOLVIDA) - VETOR (COMPLEMENTAR)

##Questão 1

Escreva um programa que leia um vetor contendo N elementos inteiros (N será lido), calcule e exiba:
*	A quantidade de elementos pares;
*	A quantidade de elementos ímpares;
*	A soma de todos os elementos;
*	A média dos elementos do vetor.
"""

#inicialização das variáveis
cont_par = 0
cont_imp = 0
soma = 0

#leitura do valor de N
n = int(input('Digite o valor de N: '))

#criação do vetor com valores nulos
vetor = [None]*n

#leitura do vetor
print('\nDigite os elementos do vetor:')
for i in range(n):
    vetor[i] = int(input())

#cálculo da quantidade de pares e ímpares
for e in vetor:
    if e % 2 == 0:
        cont_par += 1
    else:
        cont_imp += 1

#cálculo da soma dos elementos
for e in vetor:
    soma += e

#cálculo da média
media = soma / n

#exibição dos resultados
print(f'\nQuantidade de elementos pares: {cont_par}')
print(f'Quantidade de elementos ímpares: {cont_imp}')
print(f'Soma de todos os elementos: {soma}')
print(f'Média dos elementos: {media:.0f}')

"""##Questão 2

Dados dois vetores A e B contendo N elementos inteiros cada (N, A e B serão lidos), gerar e exibir um vetor C (de tamanho N*2) cujos elementos sejam a intercalação dos elementos de A e B.      
Ex: N = 3, A = [18, 12, 20], B = [15, 10, 7], C = [18, 15, 12, 10, 20, 7]
"""

#leitura do valor de N
n = int(input('Digite o valor de N: '))

#inicialização dos vetores A, B e C
a = [None]*n
b = [None]*n
c = [None]*(n*2)

#leitura do vetor A
print('\nDigite os elementos do vetor A:')
for i in range(n):
    a[i] = int(input('A['+str(i)+']: '))

#leitura do vetor B
print('\nDigite os elementos do vetor B:')
for i in range(n):
    b[i] = int(input('B['+str(i)+']: '))

#geração do vetor C
for i in range(n):
    c[i*2] = a[i]
    c[i*2+1] = b[i]

#impressão dos vetores A, B e C
print()
print('A = ',a)
print('B = ',b)
print('C = ',c)

"""##Questão 3

Escreva um programa para ler 6 números. Após a leitura dos números, verifique, para cada um deles, se é distinto, ou seja, não possui repetição.
"""

n = 6
numeros = [None]*n

for i in range(n):
    numeros[i] = int(input(str(i+1) + 'º número: '))

print()

for i in range(n):
    
    existe = False
    for j in range(n):
        if numeros[i] == numeros[j] and i != j:
            existe = True
            break
    
    if existe:
        print(numeros[i],'repete')
    else:
        print(numeros[i],'não repete')

"""##Questão 4

Escreva um programa para ler 6 números distintos, ou seja, não podem repetir.    
Exiba os números lidos.
"""

n = 6
cont = 0
numeros = [None]*n

print(f'Digite {n} números distintos')

for i in range(n):

    while True:
        
        x = int(input())

        existe = False
        for j in range(i):
            if x == numeros[j]:
                existe = True
                break
        if existe:
            print('Número já existente. Digite novamente')
            continue

        numeros[i] = x
        cont += 1
        break

print(f'\nNúmeros válidos: {numeros}')

"""##Questão 5

Faça um programa para ler as 8 dezenas apostadas por 20 apostadores e verificar se a aposta é válida (cada dezena está entre [1, 80] e não pode haver repetição.       
O programa deverá calcular e exibir a quantidade de números acertados em cada aposta.      
Atenção! As dezenas sorteadas são: 06, 07, 13, 14 e 26.
"""

na = 3  #Número de apostadores (testando para apenas 3 apostadores ao invés de 20)

nda = 8  #Número de dezenas apostadas por cada apostador
vda = [None]*nda  #Vetor que irá conter as dezenas apostadas por um apostador

vds = [6,7,13,14,26]  #Vetor que contém as dezenas sorteadas
nds = len(vds) #Número de dezenas sorteadas

for i in range(na):

    #lendo as dezenas de um apostador
    print(f'\nDezenas do Apostador {i+1}:')
    for j in range(nda):
        vda[j] = int(input())

    #verificando se a aposta é válida
    valida = True
    for j in range(nda):
        #verificando se a dezena está entre 1 e 80
        if vda[j] < 1 or vda[j] > 80:
            valida = False
            break
        #verificando se há dezena repetida
        repetida = False
        for k in range(nda):
            if vda[j] == vda[k] and j != k:
                repetida = True
                break
        if repetida:
            valida = False

    #contando a quantidade de acertos se a aposta for válida 
    if valida:
        cont = 0
        for j in range(nda):
            for k in range(nds):
                if vda[j] == vds[k]:
                    cont += 1
        print(f'Número de acertos: {cont}')
    else:
        print('Aposta inválida')

"""##Questão 6

O Brasil possui 26 estados e 1 distrito federal, totalizando 27 unidades federativas.     
Escreva um programa para armazene, em um vetor, a sigla de todas as unidades federativas.     
O programa deverá obter de vários usuários qual é a unidade federativa ele acha mais interessante, informando a respectiva sigla.     
O programa encerra quando for digitada uma sigla inexistente.     
Ao final, o programa deverá exibir qual foi a sigla mais votada (considere possibilidade de empate).
"""

uf = ['AC','AL','AM','AP','BA','CE','DF','ES','GO','MA','MG','MS','MT','PA','PB','PE','PI','PR','RJ','RN','RO','RR','RS','SC','SE','SP','TO']
n = len(uf)
cont = [0]*n

while True:
    voto = input('Digite a UF de sua preferência: ').upper()
    for i in range(n):
        if uf[i] == voto:
            cont[i] += 1
            break
    else:
        break    

maior = cont[0]
for i in range(1,n):
    if cont[i] > maior:
        maior = cont[i]

print('\nUF mais votada:')
for i in range(n):
    if cont[i] == maior:
        print(f'{uf[i]} com {cont[i]} votos')