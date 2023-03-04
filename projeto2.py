import PySimpleGUI as sg


# Define uma cor
pontos = 0
sg.theme('DarkAmber')

perguntas =[
    {'pergunta': 'Qual é o planeta mais próximo do Sol?', 'opcoes': ['Vênus', 'Mercúrio', 'Marte'], 'resp': 'Mercúrio'},
    {'pergunta': 'Qual é a capital do Brasil?', 'opcoes': ['São Paulo', 'Rio de Janeiro', 'Brasília'], 'resp': 'Brasília'},
    {'pergunta': 'Qual é o país mais populoso do mundo?', 'opcoes': ['China', 'Estados Unidos', 'Índia'], 'resp': 'China'},
    {'pergunta': 'Quantas rodas tem um carro popular?', 'opcoes':['1', '2', '3', '4'], 'resp': '3'},
    {'pergunta':'pergunta', 'opcoes':['a', 'b', 'c', 'd'], 'resp':'c'},
    {}
]

pergunta_atual = 0
# Tudo que tiver dentro da janela
layout =[   
            [sg.Text(perguntas[pergunta_atual]['pergunta'],   font='Consolas', text_color='white')],
            [sg.Radio(perguntas[pergunta_atual]['opcoes'][0], group_id='fala')],
            [sg.Radio(perguntas[pergunta_atual]['opcoes'][1], group_id='fala')],
            [sg.Radio(perguntas[pergunta_atual]['opcoes'][2], group_id='fala')],
            [sg.Text('', key='msg')],
            [sg.Button('Proximo'), sg.Button('Cancelar')]
        ]

# Cria a Janela
janela = sg.Window('Janela teste', layout)

# Loop pra processar os "eventos" e pegar os valores inseridos na janela
while True:
    event, values = janela.read()
    #se o usuário fechar ou cancelar
    if event == sg.WIN_CLOSED or event == 'Cancelar':
        break

    if event == 'Proximo':
        if values[0]:
            if perguntas[pergunta_atual]['resp'] != perguntas[pergunta_atual]['opcoes'][0]:
                sg.popup(f'Resposta incorreta. A resposta correta era: {perguntas[pergunta_atual]["resp"]}')
            else:
                sg.popup('Resposta correta!')
                pontos += 1

            
        elif values[1]:
            if perguntas[pergunta_atual]['resp'] != perguntas[pergunta_atual]['opcoes'][1]:
                sg.popup(f'Resposta incorreta. A resposta correta era: {perguntas[pergunta_atual]["resp"]}')
            else:
                sg.popup('Resposta correta!')
                pontos += 1

        elif values[2]:
            if perguntas[pergunta_atual]['resp'] != perguntas[pergunta_atual]['opcoes'][2]:
                sg.popup(f'Resposta incorreta. A resposta correta era: {perguntas[pergunta_atual]["resp"]}')
            else:
                sg.popup('Resposta correta!')
                pontos += 1

        pergunta_atual += 1

        if pergunta_atual == len(perguntas):
                sg.popup('Fim do jogo!')
                break

        layout =[   
            [sg.Text(perguntas[pergunta_atual]['pergunta'],   font='Consolas', text_color='white')],
            [sg.Radio(perguntas[pergunta_atual]['opcoes'][0], group_id='fala')],
            [sg.Radio(perguntas[pergunta_atual]['opcoes'][1], group_id='fala')],
            [sg.Radio(perguntas[pergunta_atual]['opcoes'][2], group_id='fala')],
            [sg.Text('', key='msg')],
            [sg.Button('Proximo'), sg.Button('Cancelar')]
        ]
        janela.close()
        janela = sg.Window('Janela teste', layout)
        
        continue
    
print(pontos)
janela.close()
