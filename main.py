import time
from funct.allfunc import choose, cadastrar, msg
    


#programa principal
global client
client  = list()
file = open("clinetes.txt","rt")
for linha in file.readlines():
    if ("\n" == linha) :
         del(linha)
    elif ("\n" in linha):
        del(linha[:-2])
    else:
        client.append(linha)
        print(linha)

file.close()
a=int((len(client)/3)+1)
print(client)



op=0
while op != 8:
    msg()
    op = int(input("Digite o número correspondente a opção da tabela:  "))
    choose(op)
    print("\nRealizando operação...\n")
    #time.sleep(2)

