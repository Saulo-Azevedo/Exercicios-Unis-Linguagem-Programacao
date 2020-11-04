#!/usr/bin/env python
# -*- coding: latin-1 -*-

import sys
'''
Elaborar um programa que lê 3 valores a,b,c e verifica se eles formam ou não um triângulo. Supor que os valores lidos são inteiros e positivos. Caso os valores formem um triângulo, calcular e escrever a área deste triângulo. Se não formam triângulo escrever os valores lidos. (Se a > b + c não formam triângulo algum, se a é o maior).

'''
# tratamento caso aconteca do usuario digitar algo errado
try:
    # input com os valores dos lados de cada triangulo
    a = float(input("Informe a medida do lado 1:"))
    b = float(input("Informe a medida do lado 2:"))
    c = float(input("Informe a medida do lado 1:"))

except ValueError:
    print("Informe numeros somente para o lado 1 , lado 2 e lado 3!")
    sys.exit(1)

# validação se com os valores informados podemos formam um triangulo!
if a < b + c and b < a + c and c < a + b:
    print("Os lados formam um triangulo", end="")

    # validação triangulo equilatero - onde todos os lados são iguais.
    if a == b and b == c:
        print(" Equilatero! Onde todos os lados sao iguais.")

    # validação triangulo escaleno - onde todos os lados são diferentes.    
    elif a != b and b != c and c != a: 
        print(" Escaleno! Onde todos os lados sao diferentes.")

    # aqui como não foi evidenciado nenhuma da opcoes de triangulo acima, ele informará como isosceles - onde dois lados são iguais.
    else:        
        print(" Isosceles! Onde dois lados sao iguais.")

else    :
    print("Nao se pode formar um triangulo com dados informados ")

