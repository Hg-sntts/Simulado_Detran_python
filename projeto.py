import PySimpleGUI as sg
import tkinter as tk
import perguntas


# Define uma cor e texto
pontos = 0
sg.theme('DarkAmber')
sizetxt = 50

# Define imagem do botão
imgbutton = b'iVBORw0KGgoAAAANSUhEUgAAAMgAAADICAYAAACtWK6eAAAVYElEQVR4nO3deZAe9X3n8fevu59rDs1IGgkQkgAFCAqYywZjgTnieLGxhYxjZBMb7Hht18bOEnazhY8tSrC19iZx2YXtZLMbp8pJbGeXkY2QCAsstsU6WIARBnFEgYRDSOiaGWk053N1f/eP3/NoZqTRT8dMRo78eVU9NTXTT/fTM9Of/p3d7cwMEZlcdLx3QOSXmQIiEqCAiAQoICIBCohIgAIiEqCAiAQoICIBCohIgAIiEqCAiAQoICIBCohIgAIiEqCAiAQoICIBCohIgAIiEqCAiAQoICIBCohIgAIiEqCAiAQoICIBCohIgAIiEqCAiAQoICIBCohIgAIiEqCAiAQoICIBCohIgAIiEqCAiAQoICIBCohIgAIiEqCAiAQoICIBCohIgAIiEqCAiAQoICIBCohIgAIiEqCAiAQoICIBCohIgAIiEqCAiAQoICIBCohIgAIiEqCAiAQoICIBCohIgAIiEqCAiAQoICIBCohIgAIiEqCAiAQoICIBCohIgAIiEqCAiAQoICIBCohIgAIiEqCAiAQoICIBCohIgAIiEqCAiAS4Y17TzHEnMZBxl8uaP46Am56wWf2DdG0eoGWwRjwN+yknkuowDO8F8lPbTlpz7bksPXteYWRxe673L989Z182frmZ485HY+68OsU5O5aPOIaAmKObiJUuBR+IZY/Ykp4RrqzUeXs9yy6oW7Qwhs56RiGD6NhTKCccB1YexEb2gZt6BcZBlkRUM6M/cWyN4+i5UsyTC2ZFP/3pB096JW2+sdtiVpLB0QXl6I7dboubwfjkfda+IeaG4Sq31DIup0TRHFgdqIMd9a7IrwQHNjqMjfRPS0DAYThcHEOcw8U5HAajA+V8zIa2XPw37472rfnWzWcPANDdHbNyZXqYjY7f3SMxVmqsWm/F7/Xz6VHLbktz0RLLgAqQkeIwLIsgclOovMmJzIGNDmEj/W56AmL+NGz4rOAyzJxFcezyJaIoIq6VX21Psj/94mmjf/6715xRPprS5PCHsVnjYHf2ljX2rr0ZX63luchqQJW0sZXoiLYlMhaQaSpBDsUMIwOwXCGO8iXytZFn5yblLzz/8cUPm3+LO1zbJLyHqyzCOTODM9fYV3qM/1uNuMiGSKmR4YhxxCgc8kvHOZyLcS529UpmI/31iksu3Jm2PLTkO9v/yKw7xjljlQUzcOgD2yzCuewP1lvnmr18v5LnOhvGMKxRYogcvRkrQSZhWWYuImqdHZVqAw/eMHv0d75xwxn9rLJofE/seJPvoS85shseHpy/Zg8PlfNcZ0PUARQO+VfLRZHDIhvaUx9J2t57b1/xwRu7X57HXS47VElycAnSaHN85hFmPTTIQ+UclzFMHUfyL/4LyInveJYg45nVaelISvWhxz9wyuB7vnXdWYO+oT+xTRIdsJJjNZEZ7qF9/HUlr3DICcq5hJGB2mhu1jvue7P0fTNgNRHYhEJjYkBW+67cs3/IF6slVtiQwiEnMEeO4b31cnHO+8/6y613sNKldE/MxNg3jUHAix6wtw06VqXDZKBpInKCc8TZyEA6GJXueNt3t1/iQ9K9/7hvBMQcL2JmFvUMZ3dnCTmX+QHK47XfIiHTd2A657KUNMolO0fTu80s5sUXrfkR/nMapcc599Zv6k/iv81GSBvjGyLTaxoa6c5BZhA3vk4LszRq6YjnuX03vXjLwv/dzIRvlNxItn69JYP1+PYsQzOo5JeWA0ZrhgPKdSOerqLEObK0bv2jdruZxdxIBuYiuolwzm7dx9Vpjgutgh2v0sPhzwpJ4xW5yYtSx6GX7X+PO3gaceQmfx1qO27cOofb78ned+DPDvX5R7o/v+oiB0M1471nFPnRB+dxXleOvZWM3PT0FsdUh62WlC664Ls7r8I5o5tofw/VYMpHLQ+uSsZxuJAqdlBJYTSFeqMMy0fQmvhlaeNnDr+8mkIugpzjoCLP4ZfXDYqx/96AkfrE9zYPxNhBoXFKyMZ9TjXz23D45YcKa2p+3w9832jj84rx2PcZY/sz2bassT95DcdOKnL+f3ve3Bxr3t/Fivt7eWZ3jTlFR23SsfCj4TJLilF/ufIx4CfQ+F9+dr213dfDS/WYBdSPT0AGarCwDS7tgpMKgMELe+HZvTCSQXviD97MoL0AC4qwewT21HxpM/6AywxOaYVZCWwZhHIGuRhOa/W/WPOgb64zUIU3hv17SvHY58xvgdk5P1/09SGo2cEhyQxa87Cw5Kf4bxmGamPDi9v8JUGvDvlgnNoKhXH7GrlG+DO/HBpViDrsGPWl4Alnim2Q2EFfOeOaRUXuWz6X0bpx/dpeNu6uMqcYUZ9aSDLifJRklW0fPT0+52vXnjLsAM79O1vWV+NnaQVzM9xz5YCywR+eD7ef4w+g8TbvgS9uhB/1wuw89JThw0vhr98KX9oAX3sNuvJjpU7sfGi+95vwoZNh2TrYNASLO+Cx98LcSf4nWQYPb4U7noV/GoFZOdhdhm9dCZ9ZDBh8Yj3cs9MHplmaJQ56K/BfLoPPnwmVKlz5ILw8Ci6GR98HZwFL74eBCJ69ARYfwajSczvhnT+GUn7/ZO4TxzQ00pMI+kYzrlxYYO3yLmqZsXxdLz/fWWVuMZpSSWJmlhSKrispX/7iLQs3JAD1Gm+1HLgKKczcwGDsYE8VPns+3LEUNu6Cu1+C7WX/R7hqAdz+G/D9K+FdD8PL5Yl1+tCxc+AyM8g72DUIf/4KJLG/GqBmcOlJcN1psLQdrvoRVMyfvfdvw8GKhXDP9onbrGcwqwTLF+x/20H7YI0FzuBrm2Bezi8bTeHyBXDdSfDDV+CZgbGq2LZBX5qdcOGYJvUM5pYifvpmheXrelm7fC73X9/Fivv7eGJHZUohcY40y7Uk1WrlbYAPyHA9O2+mK70OX7VoK8Bnfx2274MPrIfdKRQbu/LIVvjHYfjuJfCFpfA7Tx379buGb6/sHIS7noFczv8sAqqb4O4r4A+WwHvmw/d2+J/HzlebXhqGaxbCyc/CoPkziHMwVPcH+ZkleHUYTi9MEsxxv++3N/tAJhGUy/B7sQ/I6lfgnm1QLPh/fi721UPl49DqGXQVI362vcLydX2svX4u918/lxXr+tiwozKF6pavfI9mLAWIYiAXRadbun/pjEkNWhKYm4c9I7Cr4qs37Ql05mFBG/xkK3znFXh+EFriserNscrFcFILLGiBBSVY2AKtEfxkl28HzCuMO3M3zvz3bIHOFrhstm/oR84HqJzBb58OW/fChj0QJeF++dkFmF/0n9FS8r8nQEceWkv+5/OL0JlTOI5ELYO5xYjHd1RYvraXzOD+FV28c0GBvtGM5FjO+WbO0pQk4vQYiAyop8xutBJnLCCG74XqK8PP++C8U+DLF8D8HAzXYeco7K1BpQafewL+20u+h2gq1Q4H1FPYNQLbG6+tw1B28MFF/qB/tMdXdYzGwR7DY9thTwYfXuxLPeca1asirDgF1m2B/iO4yjk131aqm1+/Gaa08X1z2VRPAr9KahnMKUY8ubPK+9f2UkuNtdd3cdXCInvK2dGPkzgclpGmdBiQZEA5oxBx4DzGGeAgb/Clp+HX3wm3Xwi3nw+/2AMbdsNju+GpPiinvmSZ0kc537ZY0AHfuIz9Z5d6BhfMg0s74FPrYeMQzC/AcG3sLL5rCB7YDR86zVezyuZLkmULYH4Cq9+A3503tf2TY1dvlCRP76rxb9b08uAHunhgxVzet7aXx3dUac25oxtxN6NqVjBmsEE+mcyglMArffBbj8BHz4AVi+DiLv/6/d+AvlH4H5vhay9BMTn2Is7hu1+7WuHWpZPtDJzfBXN2+/GP8Z8TG/zgNbj5HXDFXFjXAzXgQ2dA3wBs3Ae/n6B60XGUNUrei+bn6ChEPN9bZftwSi5yU6p1JBFQjKhUoHlniBlVTSGOYO8I/NEm+OaLsKgNzp8NV58CHzkd/vPFMCeBL7xw7CPNmfm2xku7YfljUMgBjT/q/Ba47Ty49S0wy8Gtz00cg2hJ4LEdMGywcjH8YAd0tsKKk2HtZqilMMUCTqYgcdBTzvjcBW1846pONu6qsuL+PvZVsqMvPQCcI+9cpTlDgiRmb2NocEbPgZlBRwEWtTQa6wUoRLB1CO59Hf7dz+AdD8OrZfj0OXB60TeMzfyO5qNDjG479k8/GH/2cPiDedsIvDniv+4chSd3wac2wGsVuOlMWFSYWIrkY9gzBA/2wLWnQUcEF8731asfbAWSsYE+mVlJBD2jGbde6MPx+I4q16/rY6ia0XYs4TAMFxHH7HNAlAK1LHvdxY3FMyR2MFiD5WfCz6+Da+dCT9U3xEsxzCn4ke8XdsMDuyDJQ1ejh6mv7A/eRS2+0RwfMI8pH8OSNqhVfEM/dmNBiRrTV5qvlgROKsFIDbaVoZD3XazZAaPmDlj9mu+KvbgT3rsQdu6Dp/r9503brFI5YrGDnpGM2y5u4+tXdvLY9gof/LtehusZpcQdW2eHc+bimHrG6/sHBVuT6IX+Gf4HG760eKrHH2CfWwr/ZydsH/XduQ7oS6GtCG+fDdUKbBuF9hz8Yz8MGVy7GBZs9gOLrbEvOfrL8M7T4NwWePZN2Fn122/WHusp9JYhn/rQRA4qdbjoFLig3Y/HbGsMVDb/JM220uM7fW/Vp86Bi0+G//UPMJj5QUeZOc2qT2854w/f2s4fX9HBT9+ssPKBPsqpUYqPMRxA80gpRWyGRkCSHE+7GjROxjMiM38Gf2YXfPsN+PRi+H/Xwp+9DD/f4xvBp7X74Fw6C77+C9hS8WMFbw7At1+D/7AE1l0Df/wP8M/DvnS45Cz40lv8pZDffAlqzs+HcvherLmt8O+X+vGQ5sTH+a3w6bNgVgRf3gx7Uz+omDE2Gp6PoWcY1u2EW34NqjVYsw1acn5UfP+o+QF/6sON9qvgOXrOQe9oxu1va+crl3fw6LYKH36gj0pmFKcUDjAjjmsj5HO2ERoBuaqV5+7rYXuWm9nJihnQFsEXn4TRKnz2TLj7sgPelMLXN8F/fQk6cn4kuj2GrzwNReD3lsDfzp+4yr4y/McNcO9OPwhXaQzuOQendsA3337wvmwZgM//Av7nFr9Ob9m3YxxjExsTgzVb4JZT4bnd8NwQtOVhuDGz2B3QgVCI/D4eSuLGzoZyZCIHA1Xj85e08+VlHfz4jQofebCP+jSEA8hcUohcrbztPafGm14EXPPKqdN/aN8ZzfMJG6HODHb/OnxVZ6AOZ8yCt3fBkla/bPsQ/P1ueGXYj4M0D1SHL4GGUji7Ay6fDycX/Dr/vA829PjqWEd+rEGfRHBupy9ZDpzNW67BPw36fehodEfVzZdg8/Kwud/PKI4M4hjO74SeEXh91M/vqhksmQVzcvDiXl9SAZzT6QPyfD+kjIWnWXKd1AKLSvDaAPRNMiv5hDSFyYqxg/5KxifPbeW//+ZsHt5S5mMP7aGeGYWphwOg7kodSamy7ztvfObUT9Jt8f6AvOU++60e45G0SuZmeLp78yxabl4P0ugSiiPfYC9NMsWkuc5I3a+3f4Zt5BvehWjiOsbY9RkHipwfPU/cxOtOKqk/+EvJxD/IcN2XGIVoLLDlxvUnLePGapqf1zLJ6cbhR4Erme+YmOy6lhPSFALigEpmnN2Z8NFzWvnq04MMVafQID+IZVGuGJ2cq73ruVtO+YkPCOYwWP8o8cd6eKqW5wLKjfvuzjDXSGbzAGtO9wj97s2eqyNZJ1SVmawXqlllOnBZ1Ch+ssO8t/l5h+rhco317DC/4wllCgFprE4lNcqp0Z6LiKNp60FMybdEhdrQs9s+s/ASBxn+eHTGaqJrrnH19iT9kyg6fld8mk2cr5QewYGTHcU6zQuhJnsdan8mW5bZweMek703tG04shOATGRAIXbMLkREblpv2kAUJ66z5P7EOZf6m8i5xv1IV5KxyqLNN8T3JOXsZ5SIMY74ISMiM8k4spPnkW/QUoptcb7Sv+GFm09dzapVESv9zawbZZwzzsU557J5rdFtUZ2aRf5xONO1DyK/nMwsiomzWu3kUnybcy7l3HP39+GMVQJXupRui595n9vYbtwVtxKBShE5wRlpXJoVt9nInRtvXvCU77Qae0TbxPZG8+bVN2Kn/ZB7K0Xdn1em2RQb6dPKrEbb7FypvHfNG5869bfdaqIDH802cQ+dM24kcw57TwcfL1R5glYSrPFsEJEThX/8Qa5UHdzwkaWFjzsH/mZxoccfgA/JKtxfvNvte2vr0IpilSdp2x8StUnkXzkzzOq0dialdOTxK+a1rPjqFfMGWcWkzys8dJeuHsEm/xKOZxXLLDWIotbZrpAO33/dwuTmv3j3nH2hR7CFxzwaK5qZO+s+vjxkfD5zRJRJ8eMlCoocneMSEMvIzCi0xhFp1p7wldc+Me+OzCAUjsbuHm7begy0TKOZC4hh5g/8XCF2+RL5rPp0V2vuP226sf3R5gySqT0GmnEb6Lb4+Rvcj//tHJa11bk1IXvVtRJTIvZ3giAF6hhpY/xEL71m7mVmQApWJ8tSwzmK7XHU0hHnktzLHXn3uduXzb58043tj9Jt/raBhwkHHO1ZvzGxEeCT91n7hpgbhqvcUsu4nBJFc2B1oA52UH+ACL4EGRnGRvb4+7NOA3MRLoohyeOSPM45XHVkNJfPPdZeKPzNymX5e+861Y0A0N09YZzjCHb36HeHbv8sQ/BF0LJHbEnPCFdWMi6tp1xQz1gUQ2c9o5DpcgcZz4FVy1h1eFqqWBFkSewqqbn+JI62xrlkU0su/8Sirvjvf3yVe21/46Lb4gPHOI5wd4+RmeNOYiAb38iJgJuesFn9g3RtHqBlsKYnVckBpvEWMO150qWdjJx0Dj1/Nc8NTmhtr1oVwdURd16dHkl1ajLOdIdkkUNSN61IgAIiEqCAiAQoICIBCohIgAIiEqCAiAQoICIBCohIgAIiEqCAiAQoICIBCohIgAIiEqCAiAQoICIBCohIgAIiEqCAiAQoICIBCohIgAIiEqCAiAQoICIBCohIgAIiEqCAiAQoICIBCohIgAIiEqCAiAQoICIBCohIgAIiEqCAiAQoICIBCohIgAIiEqCAiAQoICIBCohIgAIiEqCAiAQoICIBCohIgAIiEqCAiAQoICIBCohIgAIiEqCAiAQoICIBCohIgAIiEqCAiAQoICIBCohIgAIiEqCAiAQoICIBCohIgAIiEqCAiAQoICIBCohIgAIiEqCAiAQoICIBCohIgAIiEqCAiAQoICIBCohIgAIiEqCAiAT8f0LP7BsB8eyyAAAAAElFTkSuQmCC'


pergunta_atual = 0
# Tudo que tiver dentro da janela
layout =[   
            [sg.Text(perguntas.perguntas[pergunta_atual]['pergunta'], font=('Consolas', 20), text_color='white', size=(50, None))],
            [sg.Radio(f"A) {perguntas.perguntas[pergunta_atual]['opcoes'][0]}", font=('Calibri', 15), group_id='fala', size=(sizetxt, None))],
            [sg.Radio(f"B) {perguntas.perguntas[pergunta_atual]['opcoes'][1]}", font=('Calibri', 15), group_id='fala', size=(sizetxt, None))],
            [sg.Radio(f"C) {perguntas.perguntas[pergunta_atual]['opcoes'][2]}", font=('Calibri', 15), group_id='fala', size=(sizetxt, None))],
            [sg.Radio(f"D) {perguntas.perguntas[pergunta_atual]['opcoes'][3]}", font=('Calibri', 15), group_id='fala', size=(sizetxt, None))],
            [sg.Text('', key='msg')],
            [sg.Button('   '), sg.Button('Cancelar')]
        ]

# Cria a Janela
janela = sg.Window('Janela teste', layout)

# Loop pra processar os "eventos" e pegar os valores inseridos na janela
while True:
    event, values = janela.read()
    #se o usuário fechar ou cancelar
    if event == sg.WIN_CLOSED or event == 'Cancelar':
        break

    if event == '   ':
        if values[0]:
            if perguntas.perguntas[pergunta_atual]['resp'] != perguntas.perguntas[pergunta_atual]['opcoes'][0]:
                sg.popup(f'Resposta incorreta. A resposta correta era: {perguntas.perguntas[pergunta_atual]["resp"]}')
            else:
                sg.popup('Resposta correta!')
                pontos += 1

            
        elif values[1]:
            if perguntas.perguntas[pergunta_atual]['resp'] != perguntas.perguntas[pergunta_atual]['opcoes'][1]:
                sg.popup(f'Resposta incorreta. A resposta correta era: {perguntas.perguntas[pergunta_atual]["resp"]}')
            else:
                sg.popup('Resposta correta!')
                pontos += 1

        elif values[2]:
            if perguntas.perguntas[pergunta_atual]['resp'] != perguntas.perguntas[pergunta_atual]['opcoes'][2]:
                sg.popup(f'Resposta incorreta. A resposta correta era: {perguntas.perguntas[pergunta_atual]["resp"]}')
            else:
                sg.popup('Resposta correta!')
                pontos += 1
        
        elif values[3]:
            if perguntas.perguntas[pergunta_atual]['resp'] != perguntas.perguntas[pergunta_atual]['opcoes'][3]:
                sg.popup(f'Resposta incorreta. A resposta correta era: {perguntas.perguntas[pergunta_atual]["resp"]}')
            else:
                sg.popup('Resposta correta!')
                pontos += 1

        pergunta_atual += 1

        if pergunta_atual == len(perguntas.perguntas):
                sg.popup('Fim do jogo!')
                break

        layout =[   
            [sg.Text(perguntas.perguntas[pergunta_atual]['pergunta'], font=('Consolas', 20), text_color='white', size=(50, None))],
            [sg.Radio(f"A) {perguntas.perguntas[pergunta_atual]['opcoes'][0]}", font=('Calibri', 15), group_id='fala', size=(sizetxt, None))],
            [sg.Radio(f"B) {perguntas.perguntas[pergunta_atual]['opcoes'][1]}", font=('Calibri', 15), group_id='fala', size=(sizetxt, None))],
            [sg.Radio(f"C) {perguntas.perguntas[pergunta_atual]['opcoes'][2]}", font=('Calibri', 15), group_id='fala', size=(sizetxt, None))],
            [sg.Radio(f"D) {perguntas.perguntas[pergunta_atual]['opcoes'][3]}", font=('Calibri', 15), group_id='fala', size=(sizetxt, None))],
            [sg.Text('', key='msg')],
            [sg.Button('   ', image_data=imgbutton, button_color=(sg.theme_background_color(),sg.theme_background_color()), border_width=0), sg.Button('Cancelar')]
        ]
        janela.close()
        janela = sg.Window('Janela teste', layout)
        
        continue

janela.close()