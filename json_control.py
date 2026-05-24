from arbol_json import GeneralTree
from lista_docs import LinkedList
import json
class JsonController:
    def agregar_nodos(self, elemento, padre, arbol):
        for clave, valor in elemento.items():
            if isinstance(valor, dict):
                arbol.insert(padre, {clave: None})
                self.agregar_nodos(valor, clave, arbol) 
            else:
                arbol.insert(padre, {clave: valor})

    def json_a_arbol(self,nombre_archivo: str, data: LinkedList):
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            json_info = json.load(archivo)

        for elemento in json_info:
            arbol = GeneralTree()
            doc_id = f"doc_{data.size}"
            arbol.insert(None, {"doc": doc_id})
            self.agregar_nodos(elemento,doc_id,arbol)
            data.append(arbol)
    def arbol_a_json(self, arbol: GeneralTree):
        ...