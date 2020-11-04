#!/usr/bin/env python
# -*- coding: latin-1 -*-

'''
Implementar uma função que retorne verdadeiro se o número for primo (falso caso contrário). Testar de 1 a 100.

'''

import sys
# Função que verifica se o numero e primo ( de 0 - 100)
def numero_primo(n):
    tot = 0

    for c in range(1, 100):

        if num % c == 0:
            print('\033[33m', end='')
            tot +=1
        else:
            print('\033[31m', end='')
        print('{} '.format(c), end='')
    print('\n\033[mO numero {} foi divisivel {} vezes'.format(num, tot))

    if tot == 2:
        print('primo')    
    else:
        print('nao e primo')


# Usando try/exception  na vericação de possiveis erros
try:
    #input com valor a ser veriricado
    num = int(input(" Digite um numero de 0 a 100 e veja se ele e primo : \n"))    
    # condição do if solicitada ( ser 0 a 100)
    if num  <= 100:
        print(" Lista de numeros", numero_primo(num))
    else:
        print(" valor acima de 100 nao sao aceitos, tente novamente")
except ValueError:
    print("ERRO ! - Caracteres nao sao permitidos - Informe um NUMERO entre 0 e 100 e veja se ele e primo")
    sys.exit(1) 