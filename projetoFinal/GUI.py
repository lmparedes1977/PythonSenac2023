import tkinter as tk
from tkinter import messagebox
import time
import json


def recebe_retorno(log):
    """Recebe retorno de validação do back end"""    
    with open('retorno.json', encoding='utf-8') as arq:
        retorno = json.load(arq)        
        if retorno['msg']:
            print(f'{log} -> {retorno["msg"]}')
            if 'OK' in retorno['msg']:
                messagebox.showinfo("Sucesso", retorno['msg'])
            else:
                messagebox.showerror("Falha", retorno['msg'])                
    limpar_retorno()


def salva_entrada():
    """Salva entrada do usuario em JSON e zera valor do objeto StringVar"""
    cpf = str_entrada.get()
    entrada = {'cpf': cpf}    
    log = entrada['cpf']
    with open('entrada.json', 'w') as arq:
        arq.write(json.dumps(entrada))
    str_entrada.set("")
    return log


def limpar_retorno():
    "Apaga registro do arquivo JSON de retorno de validação"
    retorno = {'msg': ''}
    with open('retorno.json', 'w') as arq:
        arq.write(json.dumps(retorno))
    

def cpf_io():
    """Gerencia o ciclo de entrada e saida da validação de cpf"""
    log = salva_entrada()  # variável que copia entrada para imprimir log no console 
    time.sleep(0.7)
    recebe_retorno(log)


root = tk.Tk()
imagem = tk.PhotoImage(file='fundo.png')   # arquivo do pano de fundo da GUI
imagem = imagem.subsample(1)
root.title('SENAC TECH') 
root.geometry('600x400')
root.resizable(width=False, height=False)
root.iconbitmap('senac.ico')        
fundo = tk.Label(root, image=imagem, )
label = tk.Label(root, text='CPF VALIDATOR TABAJARA',
                font=("Arial", 30), fg='white', background='#ff6a11')
str_entrada = tk.StringVar()  # objeto StringVar que recebe entrada do usuário                    
entry = tk.Entry(root, font=("Arial Bold", 30),
                width=13, textvariable=str_entrada)
btn_validar = tk.Button(root, text='VALIDAR',
                        command=cpf_io, font=('Arial', 20), bg='light blue')
btn_fechar = tk.Button(root, text='FECHAR',
                    command=root.destroy, bg='red', font=('Arial', 15))
fundo.place(x=0, relheight=1., relwidth=1.)
label.pack(pady=10)
entry.pack()
btn_validar.pack(pady=20)
btn_fechar.pack(side='bottom', pady=25)
root.mainloop()
