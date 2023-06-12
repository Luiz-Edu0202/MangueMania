import PySimpleGUI as sg
import os



os.system("cls")
layout = [[sg.Text("Escolha uma Opção")],
        [sg.Button("Login"),sg.Button("Cadastro")]]


window = sg.Window("MangueMania", layout)


while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()