import PySimpleGUI as sg
sg.theme("DarkGrey12")
sg.theme_text_color("#458B74")
window = sg.Window(title="Profile",
                   layout=[[sg.Text("SELAMAT DATANG DI KELAS",
                                    font=("Arial",25,"italic","bold","underline"))],
                           [sg.Text("NPM   : 2210010087 ")],
                           [sg.Text("Nama  : Zainal Abidin ")],
                           [sg.Text("Kelas : 5B NonReg Banjarmasin ")]
                           ],
                   size=(510,200),
                   font=("Times New Roman", 18))
window()
window.close()