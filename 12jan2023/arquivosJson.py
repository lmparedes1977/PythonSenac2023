import json


# pessoa = {
#     'nome': 'Leozão',
#     'idade': 45
# }

# with open('pessoa.json', 'w', encoding='utf-8') as arq:
#     arq.write((json.dumps(pessoa, ensure_ascii=False)))






# data_JSON =  """
# {
# 	"size": "Medium",
# 	"price": 15.67,
# 	"toppings": ["Mushrooms", "Extra Cheese", "Pepperoni", "Basil"],
# 	"client": {
# 		"name": "Jane Doe",
# 		"phone": "455-344-234",
# 		"email": "janedoe@email.com"
# 	}
# }
# """

# dicio_python = json.loads(data_JSON)

# for chave, valor in dicio_python.items():    
#     if type(valor) == dict:
#         for key, value in valor.items():
#             print(f'    {chave} {key} : {value}')
#     else:
#         print(f'{chave} : {valor}')        






# Dicionário em Python
# client = {
#     "name": "Leozão",
#     "age": 56,
#     "id": "45355",
#     "eye_color": "green",
#     "wears_glasses": False
# }

# # Obter uma string formatada em JSON
# client_JSON = json.dumps(client, indent=2)

# print(client_JSON)





# with open('orders.json') as arq:
#     ordens = json.load(arq)

# print(ordens)    






# with open('pessoa.json', encoding='utf-8') as arq:
#     ordens = json.load(arq)

# for chave, valor in ordens.items():
#     print(chave, valor)    





# pessoa = {
#     "nome": "Leozão",
#     "idade": 45
# }
# pss_str = str(pessoa)
# print(pss_str)

# with open('pessoa.json', 'w', encoding='latin-1') as arq:
#     json.dump(pessoa, arq, indent=2)