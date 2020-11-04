#!/usr/bin/env python
# -*- coding: latin-1 -*-
 
# Faça um programa que leia a idade de uma pessoa expressa em dias e mostre-a expressa em anos, meses e dias.

from datetime import date
import sys

#Abaixo recebemos a data autal com ano, mes e dia.
data_atual = date.today()
data_em_texto = "{}/{}/{}".format(data_atual.day, data_atual.month,
data_atual.year)

ano_atual = int (data_atual.year)

# Aplicação separa se o usuario sabe quantos dias de vida tem, caso não saiba ele é direcionado a informar sua data de aniversario.
perg = input("Voce sabe quantos dias ja viveu?\n")
if perg == 'sim':
    quant_dias = int (input("Informe aqui a quantidade de dias: "))
    total_mes = quant_dias / 365 * 12
    total_ano = quant_dias / 365
    print("Voce tem: ", total_ano, " anos!")
    print ("Isso equivale a: ", int(total_mes), "Meses" ," e ", quant_dias, "Dias")
        
else:

    try:
        data = input("Informe sua data de aniversario [sem caracteres ou espaco]: ")    

        # dividimos a data recebida para gerar o calculo 
        dia = (int (data [:2]))
        mes = (int (data [2:4]))
        ano = (int (data [4:8]))

        tot_dias = (ano_atual - ano) * 365 
        tot_mes =  (ano_atual - ano) * 12
        tot_ano = (ano_atual - ano)

        print("Voce tem: ", tot_ano, " anos!")
        print ("Isso equivale a: ", tot_mes, "Meses" ," e ", tot_dias, "Dias")
    except ValueError:
        print("Erro tentar novamente, informar uma data sem caracteres ou espacos")
        sys.exit(1)