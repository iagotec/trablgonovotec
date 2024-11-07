import sqlite3
import PySimpleGUI as sg
import random

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('presencas_escola.db')
cursor = conn.cursor()

# Deletar a tabela se já existir
cursor.execute('DROP TABLE IF EXISTS presencas')

# Criar tabela se não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS presencas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sala TEXT NOT NULL,
    semana INTEGER NOT NULL,
    alunos_presentes INTEGER NOT NULL,
    total_alunos INTEGER NOT NULL
)
''')
conn.commit()

# Função para adicionar presenças ao banco de dados
def adicionar_presencas(sala, semana, alunos_presentes, total_alunos):
    cursor.execute('''
    INSERT INTO presencas (sala, semana, alunos_presentes, total_alunos) 
    VALUES (?, ?, ?, ?)
    ''', (sala, semana, alunos_presentes, total_alunos))
    conn.commit()

# Função para calcular e exibir desempenho mensal
def calcular_desempenho():
    cursor.execute('''
    SELECT sala, SUM(alunos_presentes), SUM(total_alunos)
    FROM presencas 
    GROUP BY sala
    ''')
    
    resultados = cursor.fetchall()
    desempenho_texto = ""

    for sala, total_presentes, total_alunos in resultados:
        porcentagem = (total_presentes / total_alunos) * 100
        cor = determinar_cor(porcentagem)
        desempenho_texto += f'Sala: {sala}, Total de Alunos Presentes: {total_presentes}, Desempenho: {cor}\n'

    return desempenho_texto

# Função para determinar a cor do desempenho
def determinar_cor(porcentagem):
    if porcentagem > 75:
        return "Verde"
    elif porcentagem >= 50:
        return "Amarelo"
    else:
        return "Vermelho"

# Função para determinar a sala vencedora ao final do mês
def determinar_vencedor():
    cursor.execute('''
    SELECT sala, SUM(alunos_presentes) 
    FROM presencas 
    GROUP BY sala
    ''')
    
    resultados = cursor.fetchall()

    melhor_sala = ""
    melhor_total = 0
    
    for sala, total in resultados:
        if total > melhor_total:
            melhor_total = total
            melhor_sala = sala

    # Definindo os prêmios
    premios = ["Um dia de folga", "Um lanche especial", "Um certificado de reconhecimento", "Um troféu"]
    premio = random.choice(premios)

    return melhor_sala, melhor_total, premio

# Layout da janela
layout = [
    [sg.Text('Quantas salas deseja adicionar?'), sg.InputText(key='-NUM_SALAS-')],
    [sg.Button('Iniciar Cadastro Salas'), sg.Button('Determinar Vencedor'), sg.Button('Sair')],
    [sg.Text('', size=(60, 1), key='-RESULTADO-')],
    [sg.Text('', size=(60, 1), key='-PREMIO-')]
]

# Criar a janela
window = sg.Window('Controle de Presença', layout)

# Loop de eventos
while True:
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED or event == 'Sair':
        break
    
    if event == 'Iniciar Cadastro Salas':
        try:
            num_salas = int(values['-NUM_SALAS-'])
            for i in range(num_salas):
                sala = sg.popup_get_text(f'Nome da Sala {i + 1}:')
                total_alunos = sg.popup_get_text(f'Total de Alunos na Sala {sala}:')
                
                # Entrada das presenças da semana de uma só vez
                alunos_presentes = []
                for semana in range(1, 5):  # Semanas 1 a 4
                    presente_semana = sg.popup_get_text(f'Quantos alunos estiveram presentes na Semana {semana} da Sala {sala}?')
                    alunos_presentes.append(int(presente_semana))
                    adicionar_presencas(sala, semana, int(presente_semana), int(total_alunos))

            sg.popup('Cadastro de Salas finalizado!')
            desempenho_texto = calcular_desempenho()
            window['-RESULTADO-'].update(desempenho_texto)

        except ValueError:
            sg.popup('Por favor, insira um número válido.')

    if event == 'Determinar Vencedor':
        sala_vencedora, total_vencedor, premio = determinar_vencedor()
        if sala_vencedora:
            sg.popup(f'A sala vencedora é: {sala_vencedora} com um total de {total_vencedor} alunos presentes.\nPrêmio: {premio}')
        else:
            sg.popup('Nenhuma sala cadastrada.')

# Fecha a conexão ao final
conn.close()
