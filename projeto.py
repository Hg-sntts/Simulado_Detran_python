import PySimpleGUI as sg
import tkinter as tk
import perguntas


# Define uma cor e texto
pontos = 0
sg.theme('DarkAmber')
sizetxt = 50

# Botão de próximo:
imgbuttonprox = b'iVBORw0KGgoAAAANSUhEUgAAAMgAAAAvCAMAAACRx3WWAAAAAXNSR0IB2cksfwAAAAlwSFlzAAALEwAACxMBAJqcGAAAApdQTFRFAAAA6v8A6v8A6v8A6v8A6v8A6v8A6v8A6v8A6v8A6v8A5v8E6f4B5v0HucsQnqsSmqcOlqIKtMYL5f0H6f8B5v8D6v8A6v8A6P4C6f8B2vkXc34hbHMeZ3ElQEMrLS0tKioqGBgYLTAZWmMXXmUQaXUW2/gV6v8A6P8Cv9ALgpAhMjUvHyMbeocWvtAI6f4B6v8Aus0TV1slTVYYu9EQ6v8A6v8BPUIwZ28PjpoLMDge6v8A0OUNVVsnm6gJGB4hRUoWzuIKVFoo3vEBREkW5v0G5/4E1OcHVlsjRUcnu8oLf4gZOToqRksT0eUE5/wE6P4CmKgaxtcIo7ERnK4T5v0C6v8AREsvi5YWP0ce6v8C6P4B6v8A6f8B6f4CNzwwUVQlQlIo6P4BscYZXGEiXWIijJYXaG4fc3scutIV0eUGu8sLdHwc3vIDaW8fmKMUr74Ol6MU6v8A2u8IXGMnx9gI0uUFo7ARgIkZ3/MDT1YW2/AH6v8A6v8AtMYRNjowIyohr8AL6v8Aq7kPWmAQpLIIQEMT3fACw9QErr0OJSYW6v8ArLwQLjAuGRscpbMJ6v8A6v8AuMsROkAvLDMft8sM6v8A6v8A6P4EanIiXGMT6v8AeYUgdIIV6v8A6v8AzeIO0ugM6v8A5/0DdoIiiJ8h6P4CW2gvZXYj5f0D6v8A5/4D0OMD6v8A5v8ElKEYnKkJi5cO6P0C5/0De4gicHwW6P4D6v8AipcO5/4DTFcyT18l6f4DanIhXmUS6f8C6v8AwdYScXsgZXApMDEuKysrQEcXvtMN6v8A6v8A6P4C4vwLrr4RorYdl7Eqka4uj60tiqgoiqgnkKsjnLAVxNYF5/wB6P4C6v8A6v8A6v8A6v8A6v8AhEbIawAAAN10Uk5TAGGhqrHm/+edXk+O+P/////////2jE6E////////////////////aav/////////hv////+H//////+D/////////////8j//////////8iq/////46p//////+K8f/////O////////////////////wf///////////77z//////L///////////3//////u3/////6K7///+Y//+QWf//Up7//7b//6cG//9lgP///7aY////WP+Y////////fP////////9rbK7///////////////+tY6O1+87ggOxmAAAErUlEQVR4nO3Z52PbRBQAcEPKQYCyhw4CQhBImSmjJlBWGQU5YlkMsYqAngmR5JhhxWZDalZL2dSsslfDKC1Qyt577/XHcEuKLKkx1tnqF78v0Tgr76d77yQnmUw3upFubLBhz4yNQJqx8YyeTXrbrNh0s83xlWdusWVnY6utg7HNtvh3brf9Dm107ChBuNPOfbvsKnc2dlOCsfse/XvuBaHUNsnALGnvffbtsIGFEon99j9gcNZAWxyzB6UDD0qFEQdRlIMPkQbbIZkDs32HpuTgkKHDGiSH92fhbGHHXHjEkWkxOGQIgKMaJEcfMw/OEXbMPDY9B4McB8IS5fgT4FwxyPwTT2olETU3rAlDhkBUcvIppwo5TpNObyUPLQ90EYfXIzGSM6QzBRxnSdmzW8lDB4aQw1u1YiTnnHve+ckhFyy4sKU8VFPM4S+/MZKL4MWJHQPSJaFfpC0kobIdk+4EegIVhrkE8cN4vDeOOKdGa/5VtEsLI2oYEie5TEr8NOmR+kIQxF7nRgtkx2I7ecTO2Q49VSTbYyBHj+mkZ9g4vGcAv/RKfFO7nJ7MqSFIjKRf6kkKueLKqyKQMkLIcME4hVQQKo4BQCUV4NqqaleBTfKr0oMIVPEUmJhfQQwCVP+GUEgZWEUZ6cBRQ5Co5Oprrk0Kue76GyIQS2Z5mgTCBSV6xqVlY1ZpTjYYpWna9GPcagBvplxQohCDfpZcIxeGRCQ33nRzUgiYCDk8CFueOMSkZaPznEm2rO4qWMNGT0GKFijSDd0gV9AcwJumzEY0NMWi0JOxBtoPMQIQPBc0V56SSedCVnG1OMAMQQwVjGqy6lQ1eoWiJ/X4DRDllkZJJyAuubEcMkZSYhqeNU/NYck1QOjoEp4tCjH85ucXDkFuxZDbOggxbwdlWj35HA66jfx7K/OG1lza6WEIbi+bfEJvDmGOOzoEYWFpsr/8loNTNVVkuHUAikJw49A9qykk7BCALF5yZwTiGoZRYaVPSwvfYZWm7YRKywIWX4oaIbivS7IP8YqvGIFEHEvvujsp5J5774stLR6sRwz2nljlTwicEp0iUj+Wt5I1QFSkeRAE8vxaY2xupnEo9z/wYFLIsvpDzSF4eSKJ+e+LOu5kurAiPNrRohDvw2Tb5euaNsruwzQO5eH6sqSQR6RHm0M4Qa06JpsJ+mA06ECdl846IUWQ1+TAwGkcymPS8qSQx+ET/wPCpwS/nIyPjIyDqkmP0TuMf+A9uwDAeCEWggVOYeFwHpS1ICTOoTwJn0oKyTwNn2kO8VrBLJE1TFfZIfYFyyD9HnhpjEBku4zPud7xaRzPwucSOzK9UvZ5uYVASb6PaMh/i5fX7Xgh++KK5JBM72TkUdLRoDm/FONQapMvCzgymVcWvJo6ZGWM4zVplZAjs2J1/fW0IcrKiOONN1eLFBaJNbCe4pwo8fFWHa4RdGDJWjjx9nqFvFMbXCvuwNW1avLd99Yj5P0PJj8UrSseyyH86ONPPu2847Mo4/MvIPyyPQwcX30NpW++nfju+x86Gz/+9HMgfvm1Vqv99vsf7XPg+POvv/8R+49gwvhX4O+L3ehGN7rRjfTjPzUjV78g1ECiAAAAAElFTkSuQmCC'
# Botão de cancelar:
imgbuttoncancel = b'iVBORw0KGgoAAAANSUhEUgAAAMgAAAAvCAMAAACRx3WWAAAAAXNSR0IB2cksfwAAAAlwSFlzAAALEwAACxMBAJqcGAAAAo5QTFRFAAAA6v8A6v8A6v8A6v8A6v8A6v8A6v8A6v8A6v8A6v8A5v8E6f4B5v0HucsQnqsSmqcOlqIKtMYL5f0H6f8B5v8D6v8A6v8A6P4C6f8B2vkXc34hbHMeZ3ElQEMrLS0tKioqGBgYLTAZWmMXXmUQaXUW2/gV6v8A6P8Cv9ALgpAhMjUvHyMbeocWvtAI6f4B6v8Aus0TV1slTVYYu9EQ6v8A6v8BPUIwZ28PjpoLMDge6v8A0OUNVVsnm6gJGB4hRUoWzuIKVFoo3vEBREkW5v0G5/4E1OcHVlsjRksT0eUE5/wE6P4CmKganK4T5v0C6v8AREsvP0ce6v8C6P4B6v8A6f8B6f4CNzwwRUcnc3scjJYXf4gZUVQlXGEiOToqQlIo6P4BscYZu8oLdHwc0uUFxtcIu8sL0eUGXWIiaW8fi5YWx9gIutIV3vIDmKMU3/MDo7ER6v8A2u8IXGMnT1YW2/AH6v8A6v8AtMYRNjowr74OIyohr8AL6v8Aq7kPWmAQpLIIgIkZQEMT3fACw9QEJSYW6v8ArLwQLjAuGRscpbMJ6v8A6v8AuMsROkAvLDMft8sM6v8A6v8A6P4EanIio7ARXGMT6v8AeYUgdIIV6v8A6v8AzeIO0ugM6v8A5/0DdoIiiJ8h6P4CW2gvZXYj5f0D6v8A5/4D0OMD6v8A5v8ElKEYnKkJi5cO6P0C5/0De4gicHwW6P4D6v8AipcO5/4DTFcyT18l6f4DanIhXmUS6f8C6v8AwdYScXsgZXApMDEuKysrQEcXvtMN6v8A6v8A6P4C4vwLrr4RorYdl7Eqka4uj60tiqgoiqgnkKsjnLAVxNYF5/wB6P4C6v8A6v8A6v8A6v8A6v8A129QGQAAANp0Uk5TAGGhqrHm/+edXk+O+P/////////2jE6E////////////////////aav/////////hv////+H//////+D/////////////8j/////yKr//46p/////4rx/////////////87/////////////////////wf////++8///////8v///////////f/////+7f/////orv////+Y//+QWf//Up7//7b//6cG//9lgP///7aY////WP+Y////////fP////////9rbK7///////////////+tY6O1+87TrOP7AAAEi0lEQVR4nO3Z53/bRBgHcEPKAwHKHncQEIJAykwZNYUy27L3KMVxFAGxassysc0GA6ndUmjZ1JRR9mqAlhYoZe+99/pvON2wTsMBJFl549+rq33yPV/pkU6fNJXqpptks9nmPdO2gCSz5bSerXpjVmy9zbbkl6dvt31ns8OOcnbamay5y667xejYHWG8x559e+2tdDb7qHL23a9//wMwRrFJBmagAw86uMMGFtWXQw49bHDGQCyOmYPo8CMSYQRBVPXIo9BgHJJZON13dEIODpl9jEtybH8az4zsmIOPOz4pBofMBjjBJTnxpJPxrMiO6XOTczDIPPBK1Pmn4DnRIKeednqCjtYV8UnOOPOsSI6z0TlJOsQ9EiA5F50XwXE+Sl8wBZAgyYUXXbwgPOSShZdKq2SGssOaGI9k+EgTI31EcyYOafQrFs2erynyTzlz6QzxY2p7yWX48tCOAXSFs7Y2Sl+AcuxfBizin+ehoNOBCXl5YtH+ioV8bvEveUpQ4COLTSkUXZAgyZUo9G7Sg/ocxxhYpqLlWNEaWSYjIFCWIdpYRUzMQ9W0o3khGXK4JiD2nHIFii5IgKQf9YSFXHX1NWJpvcBW4ilDlZdPT7vpQMhEU8zKgyWGbgipHqpiaLGDC26IX3LtddeHhdxw401i6ZxYmKVSUSoFUW2NNReDyBPbQgzQjTEXRAHwQHySm2+5NSwExltL11wXpEiqrfJPSLUWvToMkpcmtoNo5PAyv9s4RPdD1MWenbEOMUAq4pagqZIOL/JTb1dbstuJQQD0f4XY50CDmgxpsF9zQdQlbkksEHbCeHQwbNuYLqrV7OYSEGeeeGp5IaQxaXsxSGGUBEp6AGQpOfi2DkJytJV4c9DTbjdXECRv2fFA2LW0oMEgNOykKAGOZfFCDJA2tBIMk01smDUH6x8DTAaRe7BNa9UgSw4fYjuRJQ73QbyOCJDb71guFq+KnVBhuwBLplUteXwWaa01aWIwRHcdziA5GPVCfI4Vd94VFnL3PfeK1c3WVmyvXaMdk6fNwastwyJaa5GX1B7S4A1Xow3Kb3Z+ISdxqPfd/0BYyMrmg1JRq8TQ4N2jURyvVjeA1SpNDIaUeJdm6OEcYnmeWn6H+lBzZVjIw+iRFkQnr0fZkaFV9iOqJJckqjU5xJlIvhrN2snRhxMdZkn9RuvworOPsEsyiUN9FK0OC3kMP644Eoucc6hY5HZptJqkLJ32Mj/pfGLD89IoHsVl8W7DXgLEzs5eeSZxqE/gJ8NCUk/hpxUpuul6F2+fzH+d6M0kjmfws6EdqV6Ufi5cRSHT3vF8+oU14SGp3onx5CEvBjjU+sRLERyp1MsL1yYOWRfgeAWtj+RIrdnQfDVpiLrO53jt9Q1RGsvORtxM8JqowXmjiTdGdBDJJjz+5pRC3qoPboruIN21fuLtd6YQ8u57E+9H7Sue1Rh/8OFHH3fe8Ymf8elnGH8eD4Pkiy8x+urr8W++/a6z+f6HH6X89HO9Xv/l19/ic5D8/seff/2f//+LLX9H+PtiN9100003yecfQHhcd0kqbckAAAAASUVORK5CYII='

pergunta_atual = 0
# Tudo que tiver dentro da janela
layout =[   
            [sg.Text(perguntas.perguntas[pergunta_atual]['pergunta'], font=('Consolas', 20), text_color='white', size=(sizetxt, None))],
            [sg.Canvas(size=(750,2), background_color='white')],
            [sg.Canvas(size=(0,10))],
            [sg.Radio(f"A) {perguntas.perguntas[pergunta_atual]['opcoes'][0]}", font=('Calibri', 15), group_id='fala', size=(sizetxt, None))],
            [sg.Radio(f"B) {perguntas.perguntas[pergunta_atual]['opcoes'][1]}", font=('Calibri', 15), group_id='fala', size=(sizetxt, None))],
            [sg.Radio(f"C) {perguntas.perguntas[pergunta_atual]['opcoes'][2]}", font=('Calibri', 15), group_id='fala', size=(sizetxt, None))],
            [sg.Radio(f"D) {perguntas.perguntas[pergunta_atual]['opcoes'][3]}", font=('Calibri', 15), group_id='fala', size=(sizetxt, None))],
            [sg.Text('', key='msg')],
            [sg.Button('', image_data=imgbuttonprox, button_color=(sg.theme_background_color(),sg.theme_background_color()), border_width=0, key='Proximo'),
            sg.Button('', image_data=imgbuttoncancel, button_color=(sg.theme_background_color(),sg.theme_background_color()), border_width=0, key='Cancelar')]
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
            if perguntas.perguntas[pergunta_atual]['resp'] != perguntas.perguntas[pergunta_atual]['opcoes'][0]:
             ()
            else:
                pontos += 1

        elif values[1]:
            if perguntas.perguntas[pergunta_atual]['resp'] != perguntas.perguntas[pergunta_atual]['opcoes'][1]:
             ()
            else:
                pontos += 1

        elif values[2]:
            if perguntas.perguntas[pergunta_atual]['resp'] != perguntas.perguntas[pergunta_atual]['opcoes'][2]:
             ()
            else:
                pontos += 1
        
        elif values[3]:
            if perguntas.perguntas[pergunta_atual]['resp'] != perguntas.perguntas[pergunta_atual]['opcoes'][3]:
             ()
            else:
                pontos += 1

        pergunta_atual += 1

        if pergunta_atual == len(perguntas.perguntas):
                sg.popup('Fim do jogo!', font=('Calibri', 15))
                break

        layout =[   
            [sg.Text(perguntas.perguntas[pergunta_atual]['pergunta'], font=('Consolas', 20), text_color='white', size=(sizetxt, None))],
            [sg.Canvas(size=(750,2), background_color='white')],
            [sg.Canvas(size=(0,10))],
            [sg.Radio(f"A) {perguntas.perguntas[pergunta_atual]['opcoes'][0]}", font=('Calibri', 15), group_id='fala', size=(sizetxt, None))],
            [sg.Radio(f"B) {perguntas.perguntas[pergunta_atual]['opcoes'][1]}", font=('Calibri', 15), group_id='fala', size=(sizetxt, None))],
            [sg.Radio(f"C) {perguntas.perguntas[pergunta_atual]['opcoes'][2]}", font=('Calibri', 15), group_id='fala', size=(sizetxt, None))],
            [sg.Radio(f"D) {perguntas.perguntas[pergunta_atual]['opcoes'][3]}", font=('Calibri', 15), group_id='fala', size=(sizetxt, None))],
            [sg.Text('', key='msg')],
            [sg.Button('', image_data=imgbuttonprox, button_color=(sg.theme_background_color(),sg.theme_background_color()), border_width=0, key='Proximo'),
            sg.Button('', image_data=imgbuttoncancel, button_color=(sg.theme_background_color(),sg.theme_background_color()), border_width=0, key='Cancelar')]
            ]
        janela.close()
        janela = sg.Window('Janela teste', layout)
        continue

janela.close()
