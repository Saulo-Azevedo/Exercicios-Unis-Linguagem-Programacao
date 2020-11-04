#!usr/bin/env python
# -*- coding: latin-1 -*-

import sys
# Faça um programa que leia 3 números inteiros e mostre o menor deles.

try:
    #input com 3 valores para avaliacao do menor e maior
    primeiro = int(input("Digite o primeiro valor: "))
    segundo = int(input("Digite o segundo valor: "))
    terceiro = int(input("Digite o terceiro valor: "))
except ValueError:
    print("Voce so pode digitar numeros tente novamente")
    sys.exit(1)

# Verificação de qual será o maior numero
maior = primeiro
if segundo > primeiro and segundo > terceiro:
    maior  = segundo
if terceiro > primeiro and terceiro > segundo:
    maior = terceiro

# Verificacao de qual será o menor numero 
menor = primeiro
if segundo < primeiro and segundo < terceiro:
    menor = segundo
if terceiro < primeiro and terceiro < segundo:
    menor = terceiro

print("Menor valor foi: ", menor)
print("Maior valor foi: ", maior)