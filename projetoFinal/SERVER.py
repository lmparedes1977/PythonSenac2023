from cpf import *
import time
import json

def limpa_arquivo():
    """Apaga registro em arquivo JSON para não haver redundância de resposta"""
    entrada = {'cpf': ''}                   
    with open('entrada.json', 'w') as arq:
        arq.write(json.dumps(entrada))

def salva_retorno(ret): 
    """Registra retorno de validação de CPF em arquivo JSON."""
    msg = str(ret)  
    saida = {'msg': msg }                   
    with open('retorno.json', 'w', encoding='utf-8') as arq:
        arq.write(json.dumps(saida, ensure_ascii=False))

entrada = ""
while True:
    try:        
        with open('entrada.json') as arq:
            entrada = json.load(arq)   # var entrada recebe JSON
            if entrada['cpf']:
                cpf = Cpf.recebe_cpf(entrada['cpf'])
                retorno =  cpf.valida_cpf()
                print(f'{entrada["cpf"]} => {retorno}')   # impressão de validação em console                
                salva_retorno(retorno)                                        
                limpa_arquivo()
                cpf.__del__()                          
    except CpfException as e:  
        salva_retorno(e)        
        print(f'{entrada["cpf"]} => {e}')  # impressão de excessão em console
        limpa_arquivo()

    time.sleep(0.5)    
    


