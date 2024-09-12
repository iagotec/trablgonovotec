import PySimpleGUI as sg
import os
sg.theme('NeonBlue1')

def calculo():
    erro=''
    aa=''
    lista=[]
    layout = [
        [sg.Text("Nome completo do aluno")],
        [sg.InputText(key='nome_usuario')],
        [sg.Text('Primeira nota')],
        [sg.InputText(key='nota1')],
        [sg.Text('Segunda nota')],
        [sg.InputText(key='nota2')],        
        [sg.Button('Calcular'), sg.Button('Voltar'),sg.Button('finalizar')]
    ]

    window = sg.Window('Média dos alunos', layout)
   

    while True:
        event, values = window.read()
        

        if event == sg.WIN_CLOSED:
            break
        if event =='Voltar':
            window.close()
            login()
            
                

       
        
        if event == 'Calcular':
            n1 = values['nota1']
            n2 = values['nota2']
            nome = values['nome_usuario']
            if nome=='' or n1=='' or n2=='':
                sg.popup('Preencha todos os campos. ')
                erro='esta errado'

            elif not nome.replace(" ","").isalpha():
                sg.popup('digite um nome váildo.')
                window['nome_usuario'].update('')
                erro='esta errado'
            elif len(nome) < 6:
                sg.popup('Digite  6 ou mais caracteres.')
                window['nome_usuario'].update('')
                erro='esta errado'

            elif not n1.replace(".", "").isdigit() or not n2.replace(".", "").isdigit():
                sg.popup('Erro,apenas numeros são permitidos.')
                window['nota1'].update('')
                window['nota2'].update('')
                erro='esta errado'
            else:
                try:
                    n1 = float(n1)
                    n2 = float(n2)
                    erro=''

                    if n1 <= 10 and n2 <= 10:
                        media = (n1 + n2) / 2
                        erro=''

                        if media < 5:
                            aproveitamento = 'F'
                        elif 5 <= media <= 5.9:
                            aproveitamento = 'E'
                        elif 6 <= media <= 6.9:
                            aproveitamento = 'D'
                        elif 7 <= media <= 7.9:
                            aproveitamento = 'C '
                        elif 8 <= media <= 8.9:
                            aproveitamento = 'B '
                        elif 9 <= media <= 10:
                            aproveitamento = 'A '
                        if media >= 6:
                            situação='Aprovado'
                        else:
                            situação=""

                        
                        sg.popup('resultado guardado.Para ver clique em: finalizar')
                        window['nome_usuario'].update(f'')
                        window['nota1'].update(f'')
                        window['nota2'].update(f'')


                        
                    else:
                        sg.popup('Erro, apenas numeros menores que 10 são permitidos.')
                        window['nota1'].update('')
                        window['nota2'].update('')
                        erro='esta errado'


                except ValueError:
                    sg.popup('Erro,numeros invalidos.')               
                    window['nome_usuario'].update('')
                    window['nota1'].update('')
                    window['nota2'].update('')           
            if erro=='':
                lista.append({'nome':nome, 'media':media,'aproveitamento':aproveitamento})
                
            aa=''
            for i in lista:
                aa+=f"aluno: {i['nome']}, media: {i['media']}, aproveitamento: {i['aproveitamento']}\n"    
                

        if event=='finalizar':
            if aa =='':
                sg.popup('Não há alunos cadastrados')
            else:
                sg.popup(aa)

            
        







                

    window.close()


def cadastro():
    layout = [
        [sg.Text("nome do professor")],
        [sg.InputText(key='nome_professor')],
        [sg.Text("Email")],
        [sg.InputText(key='Email')],
        [sg.Text('CPF')],
        [sg.InputText(key='CPF_prof')],
        [sg.Text('Senha')],
        [sg.InputText(password_char='*', key='senha')],
        [sg.Text('Confirmar senha')],
        [sg.InputText(password_char='*', key='confirmar_senha')],
        [sg.Button('Confirmar')],
        [sg.Text('Se você já tem cadastro, clique em:'), sg.Button('Voltar')],
    ]

    window = sg.Window('Faça seu cadastro, Professor(a)', layout)
    erro=''
    while True:
        event, values = window.read()
        

        if event == sg.WIN_CLOSED:
            break
        if event == 'Voltar':
            window.close()
            login()

        if event == 'Confirmar':
            nome=values['nome_professor']
            CPF=values['CPF_prof']
            
            if nome == "" or values['Email'] == "" or values['CPF_prof']  == "" or values['senha'] == "" or values['confirmar_senha'] == "":
                sg.popup('ERRO: CAMPOS VAZIOS!')
                

            elif nome.replace(" ","").isalpha()==False:
                sg.popup('Erro,um nome não contem numeros ou simbolos')
                window['nome_professor'].update('')
            
            elif len(nome) <6  or len(values['Email'])<6:
                sg.popup('Erro: nome ou Email iválido, pois tem menos de 6 caracteres')

                
            elif   CPF.replace(" ", "").replace("-","").isdigit():
                sg.popup('digite um CPF válido')
                window['CPF_prof'].update('')               
                erro='esta errado'

            elif len(CPF) != 11:
                sg.popup('Digite Um CPF  válido')               
                erro='esta errado'
                window['CPF_prof'].update('')
                        

            elif values['senha'] != values['confirmar_senha']:
                sg.popup('Erro: As senhas não coincidem!')
                window['senha'].update('')
                window['confirmar_senha'].update('')

            elif len(values['senha']) <6 or len(values['confirmar_senha']) <6 :
                sg.popup('Erro,senha tem que ter 6 ou mais caracteres')

            
                
                
            else:                 
                dado_coletado = values['nome_professor']
                with open('dados_login.txt', 'a') as file:
                    file.write(f'{values['CPF_prof']},{values['senha']}\n')
                sg.popup(f'Você fez seu cadastro com sucesso: {dado_coletado}')
                window.close()
                login()

    window.close()

def login():
    layout = [
        [sg.Text("CPF do professor(a)")],
        [sg.InputText(key='CPF_prof')],
        [sg.Text('Senha')],
        [sg.InputText(password_char='*', key='senha')],
        [sg.Button('Ok'), sg.Button('Cancelar'),sg.Button('Cadastre-se')]
       
    ]

    window = sg.Window('Login', layout)
    erro=''
    while True:
        event, values = window.read()
        

        if event == sg.WIN_CLOSED or event == 'Cancelar':
            break
        

        if event == 'Ok':
            
            CPF=values['CPF_prof']

            if CPF == "" or values['senha'] == "":
                sg.popup('ERRO: CAMPOS VAZIOS!')
                erro='esta errado'

            
        
            elif not  CPF.replace(" ", "").replace("-","").isdigit():
                sg.popup('digite um CPF válido')
                window['CPF_prof'].update('')               
                erro='esta errado'

            elif len(CPF) != 11:
                sg.popup('Digite Um CPF  válido')               
                erro='esta errado'
                window['CPF_prof'].update('')
                        
            elif len(values['senha']) <6 :
                sg.popup('Erro,senha tem que ter 6 ou mais caracteres')
            else :
                erro=''
                if os.path.exists('dados_login.txt') :
                    with open('dados_login.txt', 'r') as file:
                        for line in file:
                            CPF_f,senha_arquivo = line.strip().split(',')
                    if senha_arquivo==values['senha'] and CPF_f==values['CPF_prof']:
                        window.close()
                        calculo()
                        break
                    else:
                        sg.popup('login não encontrado')
                        window['CPF_prof'].update('')
                        window['senha'].update('')
                else:
                    sg.popup('login não encontrado')
                    window['CPF_prof'].update('')
                    window['senha'].update('')
                


        if event == 'Cadastre-se':
            window.close()
            cadastro()
       

    window.close()
print('A')
login()