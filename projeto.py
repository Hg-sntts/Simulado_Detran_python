from PIL import Image
import base64
import PySimpleGUI as sg
import perguntas

#função pra retornar a imagem no formato base64
def retornarBase64(image):
    with open(f"C:\\Users\\hugoj\\Documents\\github\\perguntasRespostas\\imagens\\{image}.png", "rb") as image_file:
        return base64.b64encode(image_file.read())

# Define uma cor e texto
pontos = 0
sg.theme('DarkAmber')
sizetxt = 65

# Botão de próximo:
proximo = retornarBase64('prox')
# Botão de cancelar:
sair = retornarBase64('cancel')

pergunta_atual = 0
# Tudo que tiver dentro da janela
layout =[   
            [sg.Text(perguntas.perguntas[pergunta_atual]['pergunta'], font=('Consolas', 20), text_color='white', size=(sizetxt, None))],
            [sg.Canvas(size=(1100,2), background_color='white')],
            [sg.Canvas(size=(0,10))],
            [sg.Radio(f"A) {perguntas.perguntas[pergunta_atual]['opcoes'][0]}", font=('Calibri', 15), group_id='fala', size=(sizetxt, None))],
            [sg.Radio(f"B) {perguntas.perguntas[pergunta_atual]['opcoes'][1]}", font=('Calibri', 15), group_id='fala', size=(sizetxt, None))],
            [sg.Radio(f"C) {perguntas.perguntas[pergunta_atual]['opcoes'][2]}", font=('Calibri', 15), group_id='fala', size=(sizetxt, None))],
            [sg.Radio(f"D) {perguntas.perguntas[pergunta_atual]['opcoes'][3]}", font=('Calibri', 15), group_id='fala', size=(sizetxt, None))],
            [sg.Text('', key='msg')],
            [sg.Button('', image_data=proximo, button_color=(sg.theme_background_color(),sg.theme_background_color()), border_width=0, key='Proximo'),
            sg.Button('', image_data=sair, button_color=(sg.theme_background_color(),sg.theme_background_color()), border_width=0, key='Cancelar')]
        ]

# Cria a Janela
janela = sg.Window('Janela teste', layout, size=(1100,500))

# Loop pra processar os "eventos" e pegar os valores inseridos na janela
while True:
    event, values = janela.read()
    #se o usuário fechar ou cancelar
    if event == sg.WIN_CLOSED or event == 'Cancelar':
        break

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
                sg.popup('Fim do jogo!', font=('Calibri', 15))
                break

        layout =[   
            [sg.Text(perguntas.perguntas[pergunta_atual]['pergunta'], font=('Consolas', 20), text_color='white', size=(sizetxt, None))],
            [sg.Canvas(size=(1100,2), background_color='white')],
            [sg.Canvas(size=(0,10))],
            [sg.Radio(f"A) {perguntas.perguntas[pergunta_atual]['opcoes'][0]}", font=('Calibri', 15), group_id='fala', size=(sizetxt, None))],
            [sg.Radio(f"B) {perguntas.perguntas[pergunta_atual]['opcoes'][1]}", font=('Calibri', 15), group_id='fala', size=(sizetxt, None))],
            [sg.Radio(f"C) {perguntas.perguntas[pergunta_atual]['opcoes'][2]}", font=('Calibri', 15), group_id='fala', size=(sizetxt, None))],
            [sg.Radio(f"D) {perguntas.perguntas[pergunta_atual]['opcoes'][3]}", font=('Calibri', 15), group_id='fala', size=(sizetxt, None))],
            [sg.Text('', key='msg')],
            [sg.Button('', image_data=proximo, button_color=(sg.theme_background_color(),sg.theme_background_color()), border_width=0, key='Proximo'),
            sg.Button('', image_data=sair, button_color=(sg.theme_background_color(),sg.theme_background_color()), border_width=0, key='Cancelar')]
            ]
        janela.close()
        janela = sg.Window('Janela teste', layout, size=(1100,500))
        
        continue

janela.close()
