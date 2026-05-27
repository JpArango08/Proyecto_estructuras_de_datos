from arbol_json import GeneralTree
from lista_docs import ListaDocs
import json
class JsonController:
    def agregar_nodos(self, elemento, padre, arbol):
        for clave, valor in elemento.items():
            if isinstance(valor, dict):
                arbol.insert(padre, {clave: None})
                self.agregar_nodos(valor, clave, arbol) 
            else:
                arbol.insert(padre, {clave: valor})

    def json_a_arbol(self,nombre_archivo: str, data: ListaDocs):
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            json_info = json.load(archivo)

        for elemento in json_info:
            arbol = GeneralTree()
            arbol.insert(None, {f"doc_{data.size}": None})
            self.agregar_nodos(elemento,f"doc_{data.size}",arbol)
            data.append(arbol)
    def _obtener_clave_valor(self, diccionario):

        for clave, valor in diccionario.items():
            return clave, valor


    def _nodo_a_dict(self, nodo):

        documento = {}

        current = nodo.children.head

        while current is not None:

            hijo = current.value

            clave, valor = self._obtener_clave_valor(
                hijo.value
            )

            if hijo.children.head is not None:

                documento[clave] = self._nodo_a_dict(
                    hijo
                )

            else:

                documento[clave] = valor

            current = current.next

        return documento


    def arbol_a_json(self, lista_docs: ListaDocs, nombre_archivo: str):

        documentos = []

        current = lista_docs.head

        while current is not None:

            arbol = current.value

            if arbol.root is not None:

                documento = self._nodo_a_dict(
                    arbol.root
                )

                documentos.append(documento)

            current = current.next

        with open(nombre_archivo,"w",encoding="utf-8") as archivo:
            json.dump(documentos,archivo,indent=4,ensure_ascii=False)