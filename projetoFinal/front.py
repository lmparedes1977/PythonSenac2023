import tkinter as tk
from tkinter import messagebox
import time
import json


def recebe_retorno():
    with open('retorno.json', encoding='utf-8') as arq:
        retorno = json.load(arq)
        print(retorno['msg'])
        if 'OK' in retorno['msg']:
            messagebox.showinfo("Sucesso", retorno['msg'])
        else:
            messagebox.showerror("Falha", retorno['msg'])
    limpar_retorno()


def salva_entrada():
    cpf = str_entrada.get()
    entrada = {'cpf': cpf}
    with open('entrada.json', 'w') as arq:
        arq.write(json.dumps(entrada))
    str_entrada.set("")


def limpar_retorno():
    retorno = {'msg': ''}
    with open('retorno.json', 'w') as arq:
        arq.write(json.dumps(retorno))
    pass


def cpf_io():
    salva_entrada()
    time.sleep(0.75)
    recebe_retorno()


root = tk.Tk()
imagem = tk.PhotoImage(file='fundo.png')
imagem = imagem.subsample(1)
root.title('SENAC TECH')
root.geometry('600x475')
root.resizable(width=False, height=False)
root.iconbitmap('senac.ico')
str_entrada = tk.StringVar()
fundo = tk.Label(root, image=imagem, )

label = tk.Label(root, text='CPF VALIDATOR TABAJARA',
                 font=("Arial", 20), bg='orange')
entry = tk.Entry(root, font=("Arial Bold", 30),
                 width=13, textvariable=str_entrada)
btn_validar = tk.Button(root, text='VALIDAR',
                        command=cpf_io, font=('Arial', 20), bg='light blue')
btn_fechar = tk.Button(root, text='FECHAR',
                       command=root.destroy, bg='red', font=('Arial', 15))
fundo.place(x=0, relheight=1., relwidth=1.)
label.pack(pady=50)
entry.pack()
btn_validar.pack(pady=30)
btn_fechar.pack(side='bottom', pady=20)
root.mainloop()
