# ================================================================
#  SOLUCIONES EJERCICIOS DE PRÁCTICA
#  Copia cada función en el archivo que corresponde
# ================================================================


# ----------------------------------------------------------------
# ARCHIVO: consultas.py  →  dentro de la clase Consultas
# ----------------------------------------------------------------

# 1. size_docs — contar documentos manualmente
def size_docs(self) -> int:
    total = 0
    current = self.data.head
    while current is not None:
        total += 1
        current = current.next
    return total


# 4. primer_documento — retorna el primer árbol sin filtro
def primer_documento(self):
    if self.data.head is None:
        return None
    return self.data.head.value


# 5. ultimo_documento — retorna el último árbol sin filtro
def ultimo_documento(self):
    if self.data.head is None:
        return None
    current = self.data.head
    while current.next is not None:
        current = current.next
    return current.value


# 7. tiene_campo — retorna documentos que tengan ese campo
def tiene_campo(self, campo: str) -> list:
    resultados = []
    current = self.data.head
    while current is not None:
        arbol = current.value
        partes = campo.split(".")
        valor = self._buscar_ruta(arbol.root, partes)
        if valor is not None:
            resultados.append(arbol)
        current = current.next
    return resultados


# 8. suma_campo — suma todos los valores numéricos de un campo
def suma_campo(self, campo: str):
    total = 0
    encontro = False
    current = self.data.head
    while current is not None:
        arbol = current.value
        partes = campo.split(".")
        valor = self._buscar_ruta(arbol.root, partes)
        if valor is not None and isinstance(valor, (int, float)):
            total += valor
            encontro = True
        current = current.next
    return total if encontro else None


# 9. promedio_campo — promedio de un campo numérico
def promedio_campo(self, campo: str):
    total = self.suma_campo(campo)
    cantidad = self.contar({campo: {"$gte": 0}})  # cuenta los que tienen el campo numérico
    if total is None or cantidad == 0:
        return None
    return total / cantidad


# ----------------------------------------------------------------
# ARCHIVO: lista_docs.py  →  dentro de la clase ListaDocs
# ----------------------------------------------------------------

# 3. esta_vacia — retorna True si no hay documentos
def esta_vacia(self) -> bool:
    return self.head is None


# 10. invertir — invierte el orden de los documentos
def invertir(self) -> None:
    anterior = None
    current = self.head
    while current is not None:
        siguiente = current.next
        current.next = anterior
        anterior = current
        current = siguiente
    self.head = anterior


# ----------------------------------------------------------------
# ARCHIVO: arbol_json.py  →  dentro de la clase GeneralTree
# ----------------------------------------------------------------

# 6. contar_hojas — retorna cuántos nodos hoja tiene el árbol
def contar_hojas(self) -> int:
    return self._contar_hojas(self.root)

def _contar_hojas(self, nodo) -> int:
    if nodo is None:
        return 0
    if nodo.children.head is None:
        return 1
    total = 0
    for hijo in nodo.children:
        total += self._contar_hojas(hijo)
    return total


# 12. son_iguales — compara dos árboles en estructura y valores
def son_iguales(self, otro) -> bool:
    return self._comparar_nodos(self.root, otro.root)

def _comparar_nodos(self, nodo1, nodo2) -> bool:
    if nodo1 is None and nodo2 is None:
        return True
    if nodo1 is None or nodo2 is None:
        return False
    if nodo1.value != nodo2.value:
        return False
    current1 = nodo1.children.head
    current2 = nodo2.children.head
    while current1 is not None and current2 is not None:
        if not self._comparar_nodos(current1.value, current2.value):
            return False
        current1 = current1.next
        current2 = current2.next
    return current1 is None and current2 is None


# ----------------------------------------------------------------
# ARCHIVO: json_control.py  →  dentro de la clase JsonController
# ----------------------------------------------------------------

# 2. imprimir_claves — imprime las claves de los nodos hoja
def imprimir_claves(self, arbol) -> None:
    self._recorrer_hojas(arbol.root)

def _recorrer_hojas(self, nodo) -> None:
    if nodo is None:
        return
    if nodo.children.head is None:
        clave = list(nodo.value.keys())[0]
        print(clave)
        return
    for hijo in nodo.children:
        self._recorrer_hojas(hijo)


# 11. copiar_arbol — copia profunda del árbol en objetos distintos
def copiar_arbol(self, arbol):
    from arbol_json import GeneralTree
    nuevo_arbol = GeneralTree()
    if arbol.root is not None:
        self._copiar_nodo(arbol.root, None, nuevo_arbol)
    return nuevo_arbol

def _copiar_nodo(self, nodo, padre, arbol) -> None:
    clave = list(nodo.value.keys())[0]
    valor = nodo.value[clave]
    arbol.insert(padre, {clave: valor})
    for hijo in nodo.children:
        self._copiar_nodo(hijo, clave, arbol)