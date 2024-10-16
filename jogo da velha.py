import PySimpleGUI as sg
#vitoria
def vitoria_linhas():
    vitória = [
     #vitoria linhas
     [0,1,2],
     [3,4,5],
     [6,7,8],
    
     
]
    for v in vitória:
        if matriz_invisível[v[0]] == matriz_invisível[v[1]]==matriz_invisível[v[2]]!=0:
            return True
        
    return False


    
    
#vitoria diagonal
def vitoria_diagonal():
    vitória_diag=[
    [0,4,8],
    [2,4,6],
    ]   
    for b in vitória_diag:
        if matriz_invisível[b[0]] == matriz_invisível[b[1]]==matriz_invisível[b[2]]!=0:
            return True
        
    return False




#vitória colunas
def vitoria_colunas():       
    vitória_colm=[
     [0,3,6],
     [1,4,7],
     [2,5,8], 
    ]
    for o in vitória_colm:
        if matriz_invisível[o[0]] == matriz_invisível[o[1]]==matriz_invisível[o[2]]!=0:
            return True
        
    return False





#empate
def empatee():
    for e in matriz_invisível:
        if e == 0:  
            return False  
    return True  



#game
usuario_x= 'X'
jogadas=[]


#matriz invisível
matriz_invisível = [0]*9




              

#colocar os 9 botões na matriz
layout=[]
cont = 0
layout.append([sg.Push(),sg.Text("Jogo da Velha ", key="vez_jgdr"),sg.Push()])

layout.append([sg.Text(" ", key="vez_jgdr")])
for b in range(3):
    linha=[]
      
    for c in range(3):
        cont+=1
        linha.append(sg.Button('', size=(6, 3), key = cont))          
    layout.append(linha) 
layout.append([sg.Button('Reiniciar'), sg.Button('Sair')])
    

   

window=sg.Window('jogo da velha', layout)

  
while True:
    event,values= window.read()
    print(cont)
    if event == sg.WIN_CLOSED or event == 'Sair':
            break
    
    #reiniciar
    if event == 'Reiniciar':
        usuario_x= 'X'
        jogadas=[]
        matriz_invisível=[0]*9
        window['vez_jgdr'].update(f'É a vez do: {usuario_x}')
        for i in range(1, 10):
            window[i].update('') 
        continue





    #puxar função vitoria
    if vitoria_linhas() :
        sg.popup(f'Vitória do {usuario_x} em linha!')
        usuario_x= 'X'
        jogadas=[]
        matriz_invisível=[0]*9
        window['vez_jgdr'].update(f'É a vez do: {usuario_x}')
        for i in range(1, 10):
            window[i].update('') 
        continue

    #puxar função vitoria
    if vitoria_colunas() :
        sg.popup(f'Vitória do {usuario_x} em coluna!')
        usuario_x= 'X'
        jogadas=[]
        matriz_invisível=[0]*9
        window['vez_jgdr'].update(f'É a vez do: {usuario_x}')
        for i in range(1, 10):
            window[i].update('') 
        continue

    #puxar função vitoria
    if vitoria_diagonal() :
        sg.popup(f'Vitória do {usuario_x} em diagonal!')
        usuario_x= 'X'
        jogadas=[]
        matriz_invisível=[0]*9
        window['vez_jgdr'].update(f'É a vez do: {usuario_x}')
        for i in range(1, 10):
            window[i].update('') 
        continue

    # puxar função empate
    if empatee():
        sg.popup('Empate!')
        usuario_x= 'X'
        jogadas=[]
        matriz_invisível=[0]*9
        window['vez_jgdr'].update(f'É a vez do: {usuario_x}')
        for i in range(1, 10):
            window[i].update('') 
        continue



    #sem repetições
    if event in jogadas:

        continue
    
    
    window[event].update(usuario_x)
    jogadas.append(event)
    
    



    #atualiza matriz invisivel
    index = int(event)-1
    matriz_invisível[index] = usuario_x

    
         
    #puxar de novo função para validar de novo
    if vitoria_linhas():
        sg.popup(f'Vitória do {usuario_x} em linhas!')
        usuario_x= 'X'
        jogadas=[]
        matriz_invisível=[0]*9
        window['vez_jgdr'].update(f'É a vez do: {usuario_x}')
        for i in range(1, 10):
            window[i].update('') 
        continue

    if vitoria_diagonal():
        sg.popup(f'Vitória do {usuario_x} em diagonal!')
        usuario_x= 'X'
        jogadas=[]
        matriz_invisível=[0]*9
        window['vez_jgdr'].update(f'É a vez do: {usuario_x}')
        for i in range(1, 10):
            window[i].update('') 
        continue

    if vitoria_colunas():
        sg.popup(f'Vitória do {usuario_x} em colunas !')
        usuario_x= 'X'
        jogadas=[]
        matriz_invisível=[0]*9
        window['vez_jgdr'].update(f'É a vez do: {usuario_x}')
        for i in range(1, 10):
            window[i].update('') 
        continue


    #puxar de novo função para validar de novo
    if empatee():
        sg.popup('Empate!')
        usuario_x= 'X'
        jogadas=[]
        matriz_invisível=[0]*9
        window['vez_jgdr'].update(f'É a vez do: {usuario_x}')
        for i in range(1, 10):
            window[i].update('') 
        continue
         
       


    
    
    #alternar entre X e O
    usuario_x = 'O' if usuario_x == 'X' else 'X'
    window['vez_jgdr'].update(f'É a vez do: {usuario_x}')



    


    print(matriz_invisível)
       
    print(jogadas)   
window.close()