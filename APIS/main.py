'''Faz um programa que:

Pede um CEP - ok

Mostra o endereço ok

Pega a cidade retornada ok

Busca a temperatura da cidade

Mostra tudo organizado

'''
import requests
import json
while 1:
    local = input('Insira seu cep: ')
    if len(local) == 8:
        break



url = f"https://cep.awesomeapi.com.br/json/{local}"

endereco = requests.get(url)
endereco_dic = endereco.json()

#print(endereco_dic)
fulladd = f"{endereco_dic['address']}, {endereco_dic['district']}, {endereco_dic['city']}, {endereco_dic['state']}"
lat = endereco_dic['lat']
lon = endereco_dic['lng']
chave = "2ba270850ef7add26dfc699c57745666"


print(f'Seu endereço é : {fulladd}')
url_clima = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={chave}&lang=pt_br&units=metric'
clima = requests.get(url_clima)

clima_dic = clima.json()

#print(clima_dic)

print(f'A temperatura em {endereco_dic['city']} está em {clima_dic['main']['temp']} graus.')
print(f"A sensação térmica é de {clima_dic['main']['feels_like']} graus")
print(f"O tempo se encontra: {clima_dic['weather'][0]['description']}")

