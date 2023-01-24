import tkinter as tk

root = tk.Tk()
root.title('Python Labs')
root.geometry('500x400')



def boas_vindas():
    msg = tk.Label(root, text="Seja Bem-Vindo", font='Arial', bg='yellow')
    msg.pack()


def fecha_com_button():
    btn = tk.Button(root, text='FECHAR JANELA', bg='light green',
                    font='Arial', command=root.destroy)
    btn.pack()


def exibe_entrada():
    lbl.config(text=entr.get())


lbl = tk.Label(root, font='Arial', foreground='blue')
entr = tk.Entry(root)


def recebe_e_exibe():
    entr.pack()
    lbl.pack()

    btn = tk.Button(root, text='FECHAR JANELA', bg='gray',
                    font='Arial', command=exibe_entrada)

    btn.pack()


def contagem_regressiva


# boas_vindas()
# fecha_com_button()
# recebe_e_exibe()
root.mainloop()
