# -*- coding: utf-8 -*-
"""APE 2022.1 - Lista Resolvida - Comandos Básicos (complementar).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vvtwzXJ6rOHXhMIhyCu4kuOjknhzIayl

IFPB - CAMPUS JOÃO PESSOA    
CURSO: SISTEMAS PARA INTERNET     
DISCIPLINA: ALGORITMOS E PROGRAMAÇÃO ESTRUTURADA     
PROFESSORES: CANDIDO EGYPTO / EDEMBERG ROCHA

# LISTA RESOLVIDA – COMANDOS BÁSICOS (COMPLEMENTAR)

##Questão 1

A Companhia de Carros Usados João Honesto paga seus empregados um salário de R\$ 1.000,00 por mês mais uma comissão de R$ 200,00 para cada carro vendido mais 5% do valor da venda.    

Escreva um programa que leia o nome, o número de carros vendidos e o valor total das vendas de um vendedor, e calcule e exiba o seu salário.
"""

fixo = 1000.00
com = 200.00
perc = 5/100

vendedor = input('Nome do vendedor: ')
numcarros = int(input('Número de carros vendidos: '))
totvendas = float(input('Valor total das vendas: R$ '))

salario = fixo + numcarros*com + totvendas*perc

print(f'Salário: R$ {salario:.2f}')

"""##Questão 2

Escreva um programa para calcular e exibir a média ponderada de 2 notas dadas.     
Sabe-se que nota1 possui peso 6 e nota2 possui peso 4.
"""

peso1 = 6
peso2 = 4

nota1 = float(input('1ª nota: '))
nota2 = float(input('2ª nota: '))

media = (nota1*peso1 + nota2*peso2) / (peso1+peso2)

print(f'Média = {media:.1f}')

"""##Questão 3

Escreva um programa que leia duas variáveis inteiras e troque o conteúdo entre elas, mostrando o resultado.
"""

x = int(input('Entre com o valor de x: '))
y = int(input('Entre com o valor de y: '))

aux = x
x = y
y = aux

print('\nApós a troca:')
print('x =',x)
print('y =',y)

"""##Questão 4

Um motorista anota a marcação do Hodômetro do seu veículo antes e após uma viagem, bem como o número de litros de combustível gastos.    

Escreva um programa que leia os 3 dados acima, o preço do litro de combustível, a capacidade do tanque e mostre:  

a) Quilometragem rodada.   
b) Quantos quilômetros por litro faz o veículo.   
c) Autonomia do veículo.    
d) Custo da viagem
"""

km_inicial = int(input('Odômetro inicial (Km): '))
km_final = int(input('Odômetro final (Km): '))
comb_gasto = int(input('Quantidade gasta de combustível (litros): '))
preco_litro = float(input('Preço do litro do combustível (R$): '))
cap_tanque = int(input('Capacidade do tanque (litros): '))

km_rodada = km_final - km_inicial
consumo = km_rodada / comb_gasto
autonomia = consumo * cap_tanque
custo_viagem = comb_gasto * preco_litro

print(f'\nQuilometragem rodada: {km_rodada} km')
print(f'Consumo: {consumo:.1f} km/L')
print(f'Autonomia: {autonomia:.0f} km')
print(f'Custo da viagem: R$ {custo_viagem:.2f}')

"""##Questão 5

Escreva um programa que, dado um número inteiro representando uma quantidade de segundos, calcule quantas horas, minutos e segundos estão contidos nesta quantidade. 
* Ex: 7.388 segundos = 2 horas, 3 minutos e 8 segundos.
"""

n = int(input('Quantidade de segundos: '))

h = n // 3600
r = n % 3600
m = r // 60
s = r % 60

print(f'Resultado: {h:02}:{m:02}:{s:02}')

"""##Questão 6

As Ilhas Weblands formam um reino independente nos mares do Pacífico. Como é um reino recente, a sociedade é muito influenciada pela informática. A moeda oficial é o Bit; existem notas de B\$ 50, B\$ 10, B\$ 5 e B\$ 1.      

Você foi contratado(a) para ajudar na programação dos caixas automáticos de um grande banco das Ilhas Weblands.      

Os caixas eletrônicos das Ilhas Weblands operam com todos os tipos de notas disponíveis, mantendo um estoque para cada valor de cédula. Os clientes do banco utilizam os caixas eletrônicos para efetuar retiradas de um certo número inteiro de Bits.       

Sua tarefa é escrever um programa que, dado o valor de Bits desejado pelo cliente, determine o número de cada uma das notas necessário para totalizar esse valor, de modo a minimizar a quantidade de cédulas entregues.      

Exemplo:      

Para B\$ 72 seriam as seguintes notas:       
* 1 nota(s) de B\$ 50      
* 2 nota(s) de B\$ 10      
* 0 nota(s) de B\$ 5      
* 2 nota(s) de B\$ 1
"""

x = int(input("Digite o valor: B$ "))

n50 = x // 50
r = x % 50
n10 = r // 10
r = r % 10
n5 = r // 5
r = r % 5
n1 = r

print(n50,"nota(s) de B$ 50")
print(n10,"nota(s) de B$ 10")
print(n5,"nota(s) de B$ 5")
print(n1,"nota(s) de B$ 1")