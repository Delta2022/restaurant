import PySimpleGUI as psg

layout = [[psg.Text("Hello from PySimpleGUI")], [psg.Button("OK")]]

# create window
window = psg.Window("Demo", layout)

while True:
    event, values = window.read()
    # Event changes when button pressed
    if event == "OK" or event == psg.WIN_CLOSED:
        break

window.close()