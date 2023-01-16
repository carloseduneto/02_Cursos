from geopy.geocoders import Nominatim
from Capitulo99_Funcoes.Funcoes_Json import lerArquivo, gravarArquivo

geolocator = Nominatim(user_agent="wazeyes") #Nome do aplicativo

location = geolocator.geocode("R. Francisca S Oliveira 50 São Sebastião do Paraíso")
print(location.address)
print((location.latitude, location.longitude))


dicionario = lerArquivo("02_Entrada.json")
lista = dicionario["endereco"]

print(lista)
# endereco = lista[0] + "," + lista[1] + " " + lista[2] + " " + lista[3]
endereco=lista[0] + "," + lista[1] + " " + lista[2] + " " + lista[3]
print(endereco)
# location = geolocator.geocode(endereco)
"""location = geolocator.geocode(endereco)
print(location.latitude)
saida = {"Coordenadas": (location.latitude, location.longitude)}
gravarArquivo(saida, "03_Saida.json")"""

