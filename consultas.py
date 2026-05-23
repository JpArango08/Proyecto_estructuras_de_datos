from arbol_json import GeneralTree
from lista_docs import LinkedList
from json_control import JsonController
import json

class Consultas:

    def __init__(self):
        self.data = LinkedList()

    def eq(self):
        ...

    def ne(self):
        ...

    def gt(self):
        ...

    def gte(self):
        ...

    def lt(self):
        ...

    def lte(self):
        ...

    def load(self, nombre_archivo: str):
        JsonController.json_a_arbol(nombre_archivo, self.data)



    def find(self, buscar: dict):
        ...
    

