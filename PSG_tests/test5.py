import PySimpleGUI as sg

layout = [
    [sg.Text('No output', key='text')],
    [sg.Button('open', key='open')],
    [sg.Button('info', key='info')],
    [sg.Button('save', key='save')],
    [sg.Button('exit', key='exit')]
]

window = sg.Window('My new window', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'exit'):
        break
    elif event == 'open':
        window['text'].update('Open output')
    elif event == 'info':
        window['text'].update('Info output')
    elif event == 'save':
        window['text'].update('save output')