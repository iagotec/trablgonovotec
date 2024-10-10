import PySimpleGUI as sg

def vitoria():
    vitória = [
     #vitoria linhas
     [0,1,2],
     [3,4,5],
     [6,7,8],
     #vitória colunas
     [0,3,6],
     [1,4,7],
     [2,5,8],
     #vitoria diagonal
     [0,4,8],
     [2,4,6]
     
]
    for v in vitória:
        if matriz_invisível[v[0]] == matriz_invisível[v[1]]==matriz_invisível[v[2]]!=0:
            return True
        
    return False
        


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
    

    if event == 'Reiniciar':
        usuario_x= 'X'
        jogadas=[]
        matriz_invisível=[0]*9
        window['vez_jgdr'].update(f'É a vez do: {usuario_x}')
        for i in range(1, 10):
            window[i].update('') 
        continue






    if vitoria():
        sg.popup(f'Vitória do {usuario_x}!')
        usuario_x= 'X'
        jogadas=[]
        matriz_invisível=[0]*9
        window['vez_jgdr'].update(f'É a vez do: {usuario_x}')
        for i in range(1, 10):
            window[i].update('') 
        continue

# verificar empate
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

    
         
    
    if vitoria():
        sg.popup(f'Vitória do {usuario_x}!')
        usuario_x= 'X'
        jogadas=[]
        matriz_invisível=[0]*9
        window['vez_jgdr'].update(f'É a vez do: {usuario_x}')
        for i in range(1, 10):
            window[i].update('') 
        continue

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