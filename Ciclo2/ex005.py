#!/usr/bin/env python
# -*- coding: latin-1 -*-

'''
Escreva uma função que:
a) Receba uma frase como parâmetro.
b) Retorne uma nova frase com cada palavra com as letras invertidas.
'''
# Função definida para receber uma frase como paramentro e devolver as letras invertidas
def nova(frase):
    # invertendo a frase
    string = frase[::-1]
    print('A frase que voce digitou invertida fica: {}'.format(string))
    
# input com  a frase 
frase = str(input('Digite uma frase: \n'))
print(nova(frase))