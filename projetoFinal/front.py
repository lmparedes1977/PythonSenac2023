import tkinter as tk
from tkinter import messagebox
import time
import json


def recebe_retorno():
    with open('retorno.json', encoding='utf-8') as arq:
        retorno = json.load(arq)
        if 'OK' in retorno['msg']:
            messagebox.showinfo("Validação", retorno['msg'])    
        else:
            messagebox.showerror("Validação", retorno['msg'])

def salva_entrada(): 
    cpf = entry.get()      
    entrada = {'cpf': cpf }                   
    with open('entrada.json', 'w') as arq:
        arq.write(json.dumps(entrada))

def limpar_retorno():
    retorno = {'msg': ''}                  
    with open('retorno.json', 'w') as arq:
        arq.write(json.dumps(retorno))
    pass        

def cpf_io():
    salva_entrada()
    time.sleep(0.75)
    recebe_retorno()    
    limpar_retorno()
 

root = tk.Tk()
root.title('SENAC TECH')
root.geometry('500x500')
root.resizable(width=False, height=False)
root.iconbitmap('senac.ico')
label = tk.Label(root, text='TESTADOR DE CPFs SENAC')
entry = tk.Entry(root)
btn_validar = tk.Button(root, text='VALIDAR', command=cpf_io)
btn_fechar = tk.Button(root, text='FECHAR', command=root.destroy)
label.pack()
entry.pack()
btn_validar.pack()
btn_fechar.pack()
root.mainloop()
