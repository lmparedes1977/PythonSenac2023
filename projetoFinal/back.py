from cpf import *
import time
import json

def limpa_arquivo():
    entrada = {'cpf': ''}                   
    with open('entrada.json', 'w') as arq:
        arq.write(json.dumps(entrada))

def salva_retorno(ret): 
    msg = str(ret)  
    saida = {'msg': msg }                   
    with open('retorno.json', 'w', encoding='utf-8') as arq:
        arq.write(json.dumps(saida, ensure_ascii=False))

retorno = ""
while True:
    try:
        with open('entrada.json') as arq:
            entrada = json.load(arq)
            if entrada['cpf']:
                cpf = Cpf.recebe_cpf(entrada['cpf'])
                retorno =  cpf.valida_cpf()
                print(f'{entrada["cpf"]} => {retorno}')
                salva_retorno(retorno)                
                limpa_arquivo()  
    except CpfException as e:  
        salva_retorno(e)        
        print(e)
        limpa_arquivo()

    time.sleep(0.5)    
    


