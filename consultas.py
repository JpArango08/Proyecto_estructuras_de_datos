from arbol_json import GeneralTree
from lista_docs import ListaDocs
from json_control import JsonController
from typing import Any, Optional


class Consultas:

    def __init__(self):
        self.data = ListaDocs()
        self.ctrl= JsonController()
    def load(self, nombre_archivo: str) -> None:
        self.ctrl.json_a_arbol(nombre_archivo, self.data)

    def _eq(self, valor_doc: Any, valor_consulta: Any) -> bool:
        return valor_doc == valor_consulta

    def _ne(self, valor_doc: Any, valor_consulta: Any) -> bool:
        return valor_doc != valor_consulta

    def _gt(self, valor_doc: Any, valor_consulta: Any) -> bool:
        try:
            return valor_doc > valor_consulta
        except TypeError:
            return False

    def _gte(self, valor_doc: Any, valor_consulta: Any) -> bool:
        try:
            return valor_doc >= valor_consulta
        except TypeError:
            return False

    def _lt(self, valor_doc: Any, valor_consulta: Any) -> bool:
        try:
            return valor_doc < valor_consulta
        except TypeError:
            return False

    def _lte(self, valor_doc: Any, valor_consulta: Any) -> bool:
        try:
            return valor_doc <= valor_consulta
        except TypeError:
            return False

    def _aplicar_operador(self, valor_doc: Any, operador: str, valor_consulta: Any) -> bool:
        operadores = {
            "$eq":  self._eq,
            "$ne":  self._ne,
            "$gt":  self._gt,
            "$gte": self._gte,
            "$lt":  self._lt,
            "$lte": self._lte,
        }
        if operador not in operadores:
            raise ValueError(f"Operador no soportado: {operador}")
        return operadores[operador](valor_doc, valor_consulta)

    def _buscar_ruta(self, nodo, partes: list) -> Optional[Any]:
        if nodo is None:
            return None

        for hijo in nodo.children:
            for clave, valor in hijo.value.items():
                if clave == partes[0]:
                    if len(partes) == 1:
                        return valor
                    return self._buscar_ruta(hijo, partes[1:])

        return None

    def _cumple_condicion(self, arbol: GeneralTree, clave: str, valor: Any) -> bool:
        partes = clave.split(".")
        valor_doc = self._buscar_ruta(arbol.root, partes)

        if valor_doc is None:
            return False

        if not isinstance(valor, dict):
            return self._eq(valor_doc, valor)

        for op, val in valor.items():
            if not self._aplicar_operador(valor_doc, op, val):
                return False
        return True

    def find(self, buscar: dict) -> list:
        if self.data.head is None:
            return []

        resultados = []
        current = self.data.head

        while current is not None:
            arbol = current.value

            cumple_todo = True
            for clave, valor in buscar.items():
                if not self._cumple_condicion(arbol, clave, valor):
                    cumple_todo = False
                    break

            if cumple_todo:
                resultados.append(arbol)

            current = current.next

        return resultados
    
    def arbol_json(self, nombre_archivo: str):
        self.ctrl.arbol_a_json(self.data, nombre_archivo)
