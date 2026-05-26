from lista_docs import ListaDocs
from json_control import JsonController
import json
from consultas import Consultas

# Crear datos.json



c = Consultas()
c.load("datos.json")

print(c.data)

