import time

 
def abastecer(pfloat,totalL,totalR):
    exibir(preco)
    opcao=litros=0
    sn=""
    while sn!= "S":
        opcao= int(input("\n\nDigite o número correspondente ao do combustivel que deseja: "))
        real=float(input("Digite quantos reais deseja abastecer: "))
        litros=real/pfloat[opcao-1]
        print(f"\n\nR${real:.2f} irá te fornecer {litros:.2f} litros\n")
        sn=input("Caso deseje realizar o abastecimento com os valores inserido digite [S] \ncaso deseja adicionar valores diferentes digite [N]: ").upper()
     
    totalL+=litros
    totalR+= real
    
    

    file=open("real.txt","wt")
    file.write(f"{totalR}")
    file.close()

    file=open("litrosT.txt","wt")
    file.write(f"{totalL}")
    file.close()

    file=open("dinheiro_indv.txt","at")
    file. write(f"{real}\n")
    file.close()

    file=open("abast_indv.txt","at")
    file. write(f"{litros:.2f}\n")
    file.close()



    
def choose(op): 
    global preco#define  a lista preco como global para que ela seja sempre alterada fora escopo das  funcoes
    preco=list()
    global pfloat
    pfloat= list()
    
    t1=t2=0

    global totalL
    global totalR
    #----------------------------
    
    file=open("real.txt","rt")
    for i in  file.readlines():
        aux=float(i)
        t2= aux
    file.close()
    #----------------------------
    file=open("litrosT.txt","rt")
    for i in  file.readlines():
        aux=float(i)
        t1= aux
    file.close()
    #----------------------------
    totalR=t2
    totalL=t1

    #esse programa serve para que todo o conteudo no arquivo txt esteja nessa lista
    #----------------------------
    file = open("preco.txt","rt")
    for linha in file.readlines():
       preco.append(linha)
    file.close()
    #----------------------------

    transform(preco,pfloat)#TRANSFORMAR OS PREÇOS DE STRINGS PARA FLOAT 
    
    #Inicio da escolha
    if op == 1 :#EXIBIR OS PREÇOS DOS COMBUSTIVEIS
        exibir(preco)
        time.sleep(2)
    elif op == 2 :#REALIZAR ABASTECIMENTOS
        abastecer(pfloat,totalL,totalR)
        #concluido()
        
        
    elif op == 3 :# ATUALIZAR O PRECO DOS COMBUSTIVEIS
       
        alterar(preco)
       #processando()
        #concluido()
        
    elif op == 4 :# GERAR SALDO TOTAL ARRECADADO NO DIA
        print("")
    elif op == 5 :# SAIR DO PROGRAMA
        print("\n"*130)
        print(">>>>>>  Sistema finalizado com sucesso  <<<<<")
        print("\n"*5)


def transform(preco,pfloat):
    c=aux=0
    for c, i in enumerate(preco):
        if c == len(preco):
            aux=float(i)
            pfloat.append(aux)
        else:
            aux=float(i[:-2])
            pfloat.append(aux)
        

    


def msg():
    
    print("=-="*16)
    print(">>>>>>>  POSTO DE GASOLINA IPIRANGA  <<<<<<<")
    print("=-="*16)

    print("[1] ver opções de abastecimento")
    print("[2] Realizar abastecimento")  
    print("[3] Alterar preço ")
    print("[4] ver total arrecado")
    print("[5] SAIR")


def exibir(preco):
    
   
    print( '=-=-=-=-=-=-=-=-=-=-=-=-===-=-=-=-==-=')
    print(f' 1-Diesel               R${preco[0]}')
    print( '=-=-=-=-=-=-=-=-=-=-=-=-===-=-=-=-==-=')
    print(f' 2-Gasolina comum       R${preco[1]}')
    print( '=-=-=-=-=-=-=-=-=-=-=-=-===-=-=-=-==-=')
    print(f' 3-Etanol               R${preco[2]}')
    print( '=-=-=-=-=-=-=-=-=-=-=-=-===-=-=-=-==-=')
    print(f' 4-Etanol aditivado     R${preco[3]}')
    print( '=-=-=-=-=-=-=-=-=-=-=-=-===-=-=-=-==-=')
    
    


def alterar(preco):
    exibir(preco)
    
    opt=int(input("digite a opção que deseja alterar: "))
    new=input("digite o novo preço de alteração: ")
    preco[opt-1]=new

    file=open("preco.txt","wt")
    for i in range(0,5):
        file.write("")
    for i2,i in enumerate(preco):
        if i2==opt-1:
            file.write(f"{i}\n")

        
        else:
            file.write(f"{i}")
        
    file.close()

   
    
def processando():
    print("\nRealizando operação...\n")
    time.sleep(2)

def concluido():
    print("\n"*130)
    print("Operação realizada com sucesso")
    time.sleep(3)
    print("\n"*130)
