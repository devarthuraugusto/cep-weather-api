import requests
import json
cotacoes = requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL')
cotacoes_dic = cotacoes.json()
#print(cotacoes_dic)

print(f"O Real vale {cotacoes_dic['USDBRL']['bid']} dólares.")
print(f"O Bitcoin vale {cotacoes_dic['BTCBRL']['bid']} reais.")
print(f"O Euro vale {cotacoes_dic["EURBRL"]['bid']} reais.\n")

print(f"A máxima do real foi {cotacoes_dic['USDBRL']['high']} reais. Já a mínima foi {cotacoes_dic['USDBRL']['low']} reais.")