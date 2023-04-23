import base64
import PySimpleGUI as sg
import perguntas
import sys
import sqlite3

pergunta_atual = 0

# Banco de dados
dados = sqlite3.connect('usuarios.db')
cursor = dados.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (nome TEXT, idade TEXT, pontuacao INTEGER)''')
dados.commit()

#função pra retornar a imagem no formato base64
def retornarBase64(image):
    with open(f"imagens\\{image}.png", "rb") as image_file:
        return base64.b64encode(image_file.read())

# Define uma cor e texto
pontos = 0
sg.theme('DarkBlue')
sizetxt = 65

# Botão de próximo e sair:
proximo = retornarBase64('prox')
sair = retornarBase64('cancel')

# Janela de cadastro para exibir os acertos no fim do questionario
layout_login= [
    [sg.Text('Nome:'), sg.Input(key='User')],
    [sg.Text('Idade:'), sg.Input(key='Age')],
    [sg.Button('Registrar'), sg.Button('Sair')]
]

window = sg.Window('Cadastro', layout_login)
while True:
    event, values = window.read()
    #se o usuário fechar ou cancelar
    if event == 'Registrar':
        if values['User'] == '':
            sg.popup('Insira seu nome!')
            continue
        elif values['Age'] == '':
            sg.popup('Insira sua idade!')
            continue
        nome = values['User']
        idade = values['Age']
        cursor.execute("INSERT INTO usuarios (nome, idade, pontuacao) VALUES(?, ?, ?)", (values['User'], values['Age'], 0))
        dados.commit()
        sg.popup('Cadastrado com sucesso!')
        break
    if event == sg.WIN_CLOSED or 'Sair':
        sys.exit()
window.close()

# Tudo que tiver dentro da janela

layout =[   
            [[sg.Text(perguntas.perguntas[pergunta_atual]['pergunta'], font=('Consolas', 20), text_color='white', size=(sizetxt, 5)), sg.Text(f'Pergunta de número {pergunta_atual+1} / 30', text_color='white')]],
            [sg.Canvas(size=(1100,2), background_color='white')],
            [sg.Canvas(size=(0,10))],
            [sg.Radio(f"A) {perguntas.perguntas[pergunta_atual]['opcoes'][0]}", font=('Calibri', 15), group_id='fala', size=(sizetxt, None))],
            [sg.Radio(f"B) {perguntas.perguntas[pergunta_atual]['opcoes'][1]}", font=('Calibri', 15), group_id='fala', size=(sizetxt, None))],
            [sg.Radio(f"C) {perguntas.perguntas[pergunta_atual]['opcoes'][2]}", font=('Calibri', 15), group_id='fala', size=(sizetxt, None))],
            [sg.Radio(f"D) {perguntas.perguntas[pergunta_atual]['opcoes'][3]}", font=('Calibri', 15), group_id='fala', size=(sizetxt, None))],
            [sg.Canvas(size=(0,70))],
            [[sg.Button('', image_data=proximo, button_color=(sg.theme_background_color(),sg.theme_background_color()), border_width=0, key='Proximo'),
            sg.Canvas(size=(900,2)), sg.Button('', image_data=sair, button_color=(sg.theme_background_color(),sg.theme_background_color()), border_width=0, key='Cancelar')]]
        ]

# Cria a Janela
janela = sg.Window('Prova do DETRAN', layout, size=(1280,500))

# Loop pra processar os "eventos" e pegar os valores inseridos na janela
while True:
    event, values = janela.read()
    #se o usuário fechar ou cancelar
    if event == sg.WIN_CLOSED or event == 'Cancelar':
        break
    if not any (values.values()):
        sg.popup('Escolha uma alternativa!')
        continue

    if event == 'Proximo':
        if values[0]:
            if perguntas.perguntas[pergunta_atual]['resp'] == perguntas.perguntas[pergunta_atual]['opcoes'][0]:
                pontos += 1
       
        elif values[1]:
            if perguntas.perguntas[pergunta_atual]['resp'] == perguntas.perguntas[pergunta_atual]['opcoes'][1]:
                pontos += 1

        elif values[2]:
            if perguntas.perguntas[pergunta_atual]['resp'] == perguntas.perguntas[pergunta_atual]['opcoes'][2]:
                pontos += 1                
        
        elif values[3]:
            if perguntas.perguntas[pergunta_atual]['resp'] == perguntas.perguntas[pergunta_atual]['opcoes'][3]:
                pontos += 1

        print(pontos)

        pergunta_atual += 1

        if pergunta_atual == len(perguntas.perguntas):
                sg.popup('Você chegou no fim do teste. Carregando resultados...', font=('Calibri', 15))
                break
        # Aplicação dos pontos que o usuarios fez ao finalizar o questionario
        # Caso o aplicativo seja fechado antes, sua pontuação ainda sera contabilizada
        cursor.execute("UPDATE usuarios SET pontuacao = ? WHERE nome =? AND idade =?", (pontos, nome, idade))
        dados.commit()


        layout =[   
            [[sg.Text(perguntas.perguntas[pergunta_atual]['pergunta'], font=('Consolas', 20), text_color='white', size=(sizetxt, 5)), sg.Text(f'Pergunta de número {pergunta_atual+1} / 30', text_color='white')]],
            [sg.Canvas(size=(1100,2), background_color='white')],
            [sg.Canvas(size=(0,10))],
            [sg.Radio(f"A) {perguntas.perguntas[pergunta_atual]['opcoes'][0]}", font=('Calibri', 15), group_id='fala', size=(sizetxt, None))],
            [sg.Radio(f"B) {perguntas.perguntas[pergunta_atual]['opcoes'][1]}", font=('Calibri', 15), group_id='fala', size=(sizetxt, None))],
            [sg.Radio(f"C) {perguntas.perguntas[pergunta_atual]['opcoes'][2]}", font=('Calibri', 15), group_id='fala', size=(sizetxt, None))],
            [sg.Radio(f"D) {perguntas.perguntas[pergunta_atual]['opcoes'][3]}", font=('Calibri', 15), group_id='fala', size=(sizetxt, None))],
            [sg.Canvas(size=(0,70))],
            [[sg.Button('', image_data=proximo, button_color=(sg.theme_background_color(),sg.theme_background_color()), border_width=0, key='Proximo'),
            sg.Canvas(size=(900,2)), sg.Button('', image_data=sair, button_color=(sg.theme_background_color(),sg.theme_background_color()), border_width=0, key='Cancelar')]]
            ]

        janela.close()
        janela = sg.Window('Janela teste', layout, size=(1280,500))
        
        continue

janela.close()

if pontos >= 21:
    layoutResultado = [
        [[sg.Canvas(size=(100,2), background_color=None), sg.Text('Parabéns! Você foi aprovado', font=('Consolas', 20), text_color='white', size=(sizetxt, 5))]],
        [[sg.Canvas(size=(170,2), background_color=None), sg.Text(f'Sua pontuação foi de: ', font=('Consolas', 20), text_color='white')]],
        [[sg.Canvas(size=(220,2), background_color=None), sg.Text(f'{int(pontos/30*100)}%', font=('Consolas', 50), text_color='green')]],
        [sg.Canvas(size=(0,80), background_color=None)],
        [[sg.Canvas(size=(230,2)), sg.Button('', image_data=sair, button_color=(sg.theme_background_color(),sg.theme_background_color()), border_width=0, key='Cancelar')]]
]
else:
    layoutResultado = [
        [[sg.Canvas(size=(100,2), background_color=None), sg.Text('Infelizmente você foi reprovado!', font=('Consolas', 20), text_color='white', size=(sizetxt, 5))]],
        [[sg.Canvas(size=(170,2), background_color=None), sg.Text(f'Sua pontuação foi de: ', font=('Consolas', 20), text_color='white')]],
        [[sg.Canvas(size=(220,2), background_color=None), sg.Text(f'{int(pontos/30*100)}%', font=('Consolas', 50), text_color='red')]],
        [sg.Canvas(size=(0,80), background_color=None)],
        [[sg.Canvas(size=(230,2)), sg.Button('', image_data=sair, button_color=(sg.theme_background_color(),sg.theme_background_color()), border_width=0, key='Cancelar')]]
]

janela2 = sg.Window('RESULTADO', layoutResultado, size=(700,500))

while True:
    event, values = janela2.read()
    #se o usuário fechar ou cancelar
    if event == sg.WIN_CLOSED or event == 'Cancelar':
        break
janela2.close()

# Janela que exibe os acertos de quem realizou o questionario
cursor.execute("SELECT * FROM usuarios")
data = cursor.fetchall()

layoutDados = [[sg.Table(values=data,
                     headings=["Nome", "Idade", "Acertos"],
                     justification='center',
                     auto_size_columns=False,
                     num_rows=min(25, len(data)))],
          [sg.Button('Fechar')]]
window = sg.Window('Pontuacao dos usuarios', layoutDados)
while True:
    event ,values = window.read()
    if event == sg.WIN_CLOSED or event == 'Fechar':
        break
window.close()
cursor.close()


