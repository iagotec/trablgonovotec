import random
matriz = [
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0]
]
listamatriz=[]
for i in range(len(matriz[0])):
    linha=[]
    for a in range(len(matriz)):
        numero_aleatorio=random.randint(1,99)        
        linha.append(numero_aleatorio)
    listamatriz.append(linha)
   
for linha in listamatriz:
    
    print(linha, end='')
    print('')


#2
maiornumero=0
for i in range(4):
    valor=int(listamatriz[i][2])
    if valor>maiornumero:
        maiornumero= valor



print(maiornumero)


#3
soma=0

for k in range(4):
    soma+= listamatriz[k][k]
print(f'soma da diagonal principal é: {soma}')


   
    
    

