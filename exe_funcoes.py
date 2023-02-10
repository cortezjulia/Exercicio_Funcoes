
#EXERCÍCIO PARA PRÁTICA DE FUNÇÕES
#O PROGRAMA RECEBE VALORES NUMÉRICOS DO USUÁRIO, MULTIPLICA ELES 
#E RETORNA SE SÃO PARES OU IMPARES

import os

def insere_num(quantidade_numeros):
   
    while True:
        flag=0
        numeros=[]
        i=0
        while i<quantidade_numeros:
            num_digitado=input('Insira um número: ')
            try:
                num_digitado_float=float(num_digitado)
                numeros.append(num_digitado_float)
                flag+=1
            except:
                print('Insira um número!')
                break
            i+=1
        if flag==quantidade_numeros:
            break
    return numeros

def multiplica(*args):
    multiplicacao=0  
    ini=0
    for numero in args:
        print(numero)
        if ini==0:
            multiplicacao=numero
            ini=1
        else:    
            multiplicacao=multiplicacao*numero
    return multiplicacao 


def par_e_impar(*args):
    for numero in args:
        if numero%2==0:
            print(f'O {numero} é par')
        else:
            print(f'O {numero} é ímpar')
    



while True:
    os.system('cls')
    recebe_numeros=[]
    qnt=input('Digite quantos números você quer inserir: ')
    try:
        qnt_int=int(qnt)
    except:
        print('Apenas números!')
        continue

    recebe_numeros=insere_num(qnt_int)
    result_multi=multiplica(*recebe_numeros)
    os.system('cls')
    par_e_impar(*recebe_numeros)
    print(f'O resultado da multiplicação é: {result_multi}')
   
   





