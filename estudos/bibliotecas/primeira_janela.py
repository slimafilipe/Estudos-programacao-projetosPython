from tkinter import *

janelaPrincipal = Tcl()
texto = Label(master = janelaPrincipal, text = "Minha janela exibida")
texto.place(x = 50, y = 100)
janelaPrincipal.mainloop()