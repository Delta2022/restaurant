import PySimpleGUI as psg
import os.path

fileListColumn = [
    [
        psg.Text("Image Folder"),
        # psg.In takes input, size is how big the input is, enable_events
        # means if the button iss clicked then events change, key is name of 
        # input
        psg.In(size=(25, 1), enable_events=True, key='-FOLDER-'),
        psg.FolderBrowse(),
    ],
    [
        # Listbox just lists things in a box
        psg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
        )
    ],
]
imageViewerColomn = [
    [psg.Text("Choose an image from list on left:")],
    [psg.Text(size=(40, 1), key="-TOUT-")],
    [psg.Image(key="-IMAGE-")],
]

layout = [
    [
        psg.Column(fileListColumn),
        psg.VSeperator(),
        psg.Column(imageViewerColomn),
    ]
]

window = psg.Window("Image Viewer", layout)

while True:
    event, values = window.read()
    if event == "Exit" or event == psg.WIN_CLOSED:
        break

    if event == "-FOLDER-":
        # Take the inputed folder path into var folder
        folder = values["-FOLDER-"]
        try:
            fileList = os.listdir(folder)
        except FileNotFoundError:
            fileList = []
        
        fnames = [
            # Looks for a .png or a .gif file in a folder
            f for f in fileList if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png", ".gif"))
        ]
        # Update fnames and call it -FILE LIST-
        window["-FILE LIST-"].update(fnames)
    elif event == "-FILE LIST-":
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"] [0]
            )
            # Shows the picture's path
            window["-TOUT-"].update(filename)
            # makes the image
            window["-IMAGE-"].update(filename=filename)
        except:
            pass
# CLose window
window.close()