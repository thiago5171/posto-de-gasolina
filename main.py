import time
from funct.allfunc import choose,  msg, exibir, processando, concluido, transform, abastecer
    


#programa principal
op=0
while op != 5:
    msg()
    op = int(input("Digite o número correspondente a opção da tabela:  "))
    choose(op )
    


"""
preços padroes  

2.66
3.90
3.88
5.99

"""