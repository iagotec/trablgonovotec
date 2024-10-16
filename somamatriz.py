matriz = [
[1,2,3],
[4,5,6],
[7,8,9]
]


#soma de toda a matriz
somatotal=0
for i in range(len(matriz)):
    
    for j in range(len(matriz[i])):
        somatotal+= matriz[i][j]
print(f'soma total da matriz: {somatotal}\n')



#soma das colunas e linhas
soma_linhas = []
for i in range(len(matriz)):
    soma = 0
    for b in range(len(matriz[i])):
        soma += matriz[i][b]
    soma_linhas.append(soma)
print(f'soma das linhas: {soma_linhas}\n')

soma_linhas = []
for i in range(len(matriz)):
    soma = 0
    for b in range(len(matriz[i])):
        soma += matriz[b][i]
    soma_linhas.append(soma)
print(f'soma das colunas: {soma_linhas}\n')

#matriztransposta
listamatriz = []
for i in range(len(matriz[0])):  
    linha = []
    for j in range(len(matriz)):  
        linha.append(matriz[j][i])  
    listamatriz.append(linha)


for linha in listamatriz:
    print(linha)


