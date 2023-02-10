#EXERCÍCIO PARA PRÁTICA DE FUNÇÕES
#O PROGRAMA RECEBE VALORES NUMÉRICOS DO USUÁRIO, MULTIPLICA ELES 
#E RETORNA SE SÃO PARES OU IMPARES

def recebe_entrada_usuario(*args):
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

def entrar_numeros():
    while True:
        i=0
        entrada_int=[]
        entrada_string=[]


        entrada=input('Insira os números que deseja multiplicar: Formato [x,x,x...]: ')

        i=0
        indice=0


        while i<len(entrada):



            if entrada[i]==',':

                if entrada[i]==entrada[i-1] and entrada[i]==entrada[i+1]:
                    print('Insira valores válidos!') 
                    break


                entrada_string.append(entrada[indice:i])
                indice=i+1
            else:
               try:
                verifica_int=int(entrada[i])
                verifica_float=float(entrada[i])
               except:
                print('Insira valores válidos!') 
                break


            if i==(len(entrada)-1):
                k=len(entrada)-1
                while True:
                    k-=1
                    if entrada[k]==',':
                        entrada_string.append(entrada[k+1:len(entrada)])



            i+=1

    def transforma_int(entrada_int,entrada_string):

    for valor in entrada_string:
        entrada_int.append(int(valor))

        resultado=recebe_entrada_usuario(*entrada_int)

        print(f'O resultado da multiplicação é: {resultado}')
        par_e_impar(*entrada_int)    


def par_e_impar(*args):
    for numero in args:
        if numero%2==0:
            print(f'O {numero} é par')
        else:
            print(f'O {numero} é ímpar')





entrar_numeros()
