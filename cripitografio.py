import PySimpleGUI as sg
sg.theme('NeonBlue1')

def cripitografar():

    layout=[
        [sg.Text('Digite o texto e clique em "OK": '), sg.InputText(key ='-entrada-')],
        [sg.Button('OK'),sg.Button('CANCELAR'), sg.Button('DESCRIPITOGRAFAR')]
    ]

        
    window = sg.Window('CRIPITOGRAFIA',layout) 

    while True:
        event,values = window.read()


        if event == sg.WIN_CLOSED:
            break
        if event =='CANCELAR':
            window.close()
            inicio()


        if event=='OK':
            nome=values['-entrada-']
            crip=[]
            alfabeto= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
            for a in nome.lower():
                if a in alfabeto:
                    valor = alfabeto.index(a)+1
                    crip.append(valor)
            sg.popup(crip)
            return nome

def DESCRIPITOGRAFAR():
    layout=[
            [sg.Text('Digite o texto e clique em "OK": '), sg.InputText(key ='-entrada-')],
            [sg.Button('OK'),sg.Button('CANCELAR'), sg.Button('CRIPITOGRAFAR')]
            ]

            
    window = sg.Window('DESCRIPITOGRAFIA',layout) 

    while True:
        event,values = window.read()


        if event == sg.WIN_CLOSED:
            break
        if event =='CANCELAR':
            window.close()
            inicio()


        if event=='OK':
            nome=values['-entrada-']
            crip=[]
            alfabeto= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
            for a in alfabeto:
                if a in nome.lower():
                    valor = alfabeto.index(a)+1
                    crip.append(valor)
            sg.popup(crip)
            return nome   

def inicio():

    layout=[
        [sg.Push(),sg.Text("BEM VINDO!!!"),sg.Push()],
        [sg.Button('CRIPITOGRAFAR'), sg.Button('DESCRIPITOGRAFAR')]
    ]

        
    window = sg.Window('CRIPITOGRAFIA',layout) 

    while True:
        event,values = window.read()


        if event == sg.WIN_CLOSED:
            break
        if event =='CRIPITOGRAFAR':
            window.close()
            cripitografar()

        if event =='DESCRIPITOGRAFAR':
            window.close()
            DESCRIPITOGRAFAR()
        
        if event =='CRIPITOGRAFAR':
            window.close()
            cripitografar()
            
inicio()  
    
