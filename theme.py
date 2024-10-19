import PySimpleGUI as sg
sg.theme("DarkGreen4")
sg.theme_text_color("#FFFF00")
window = sg.Window(title="Profile",
                   layout=[[sg.Text("SELAMAT DATANG DI KELAS",
                                    font=("Arial",25,"italic","bold","underline"))],
                                    [sg.Text("NPM           : 2210010087 ")],
                                    [sg.Text("NAMA         : ZAINAL ABIDIN ")],
                                    [sg.Text("KELAS        : 5B NONREG BJM ")]
                   ],
                   size=(530,200),
                   font=("Times",18))
window()
window.close()