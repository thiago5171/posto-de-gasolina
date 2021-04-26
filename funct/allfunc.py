

def msg():
    
    print("=-="*18)
    print(">>>>>>>  POSTO DE GASOLINA IPIRANGA  <<<<<<<")
    print("=-="*18)

    print("[1] Cadastrar novo usuário")
    print("[2] Ver lista de usuários")  
    print("[4] Deletar usuario")
    print("[5] ver opções de abastecimento")
    print("[6] Realizar abastecimento")
    print("[7] Opções do ADM")
    print("[8] SAIR")


def choose(op):
    if op == 1 :
        client = list()

        file = open("clinetes.txt","rt")
        for linha in file.readlines():
            if ("\n" == linha) :
                del(linha)
            elif ("\n" in linha):
                del(linha[:-2])
            else:
                linha.replace("\n","")
                client.append(linha)
                print(linha)
        file.close()

        cadastrar(client)
       

        file = open("clinetes.txt","wt")
        for i in client:
            
            file.write(f"{i} |")
        file.write("\n")
        file.close()
    elif op == 2 :
        print("")
    elif op == 3 :
        print("")
    elif op == 4 :
        print("")
    elif op == 5 :
        print("")
    elif op == 6 :
        print("")
    



def cadastrar(client):
    a=int((len(client)/3)+1)
    
    nome=input("Digite seu nome: ")
    cpf=input("digite seu cpf com a seguinte estrutura 123.456.789-00: ")
   
    client.append(a)
    client.append(nome)
    client.append(cpf)
    

