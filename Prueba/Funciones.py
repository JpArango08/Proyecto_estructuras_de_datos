# ================================================================
#  FUNCIONES PARA EL EXAMEN
#  Copia cada bloque en el archivo que corresponde
# ================================================================


# ----------------------------------------------------------------
# ARCHIVO: lista_docs.py  →  dentro de la clase ListaDocs
# ----------------------------------------------------------------

def eliminar_por_nombre(self, nombre: str) -> None:
    """Elimina el documento cuyo root tenga el nombre dado (ej: 'doc_0')."""
    if self.head is None:
        return

    # caso especial: es el primero de la lista
    if list(self.head.value.root.value.keys())[0] == nombre:
        self.head = self.head.next
        self.size -= 1
        return

    current = self.head
    while current.next is not None:
        clave = list(current.next.value.root.value.keys())[0]
        if clave == nombre:
            current.next = current.next.next
            self.size -= 1
            return
        current = current.next


# ----------------------------------------------------------------
# ARCHIVO: arbol_json.py  →  dentro de la clase GeneralTree
# ----------------------------------------------------------------

def _buscar_padre(self, actual, clave: str):
    """Retorna el nodo padre del nodo hoja con esa clave, o None si no existe."""
    hijo = actual.children.head
    while hijo is not None:
        clave_hijo = list(hijo.value.value.keys())[0]
        if clave_hijo == clave and hijo.value.children.head is None:
            return actual
        resultado = self._buscar_padre(hijo.value, clave)
        if resultado:
            return resultado
        hijo = hijo.next
    return None

def eliminar_hoja(self, clave: str) -> None:
    """Elimina un nodo hoja por su clave. Si tiene hijos no lo elimina."""
    padre = self._buscar_padre(self.root, clave)
    if padre is None:
        print(f"No se encontró '{clave}' como nodo hoja.")
        return
    current = padre.children.head
    pos = 0
    while current is not None:
        if list(current.value.value.keys())[0] == clave:
            padre.children.delete_at_pos(pos)
            return
        current = current.next
        pos += 1

def contar_nodos(self) -> int:
    """Retorna el total de nodos del árbol incluyendo la raíz."""
    return self._contar(self.root)

def _contar(self, nodo) -> int:
    if nodo is None:
        return 0
    total = 1
    for hijo in nodo.children:
        total += self._contar(hijo)
    return total

def profundidad(self) -> int:
    """Retorna la altura del árbol. Árbol vacío retorna -1, solo raíz retorna 0."""
    if self.root is None:
        return -1
    return self._profundidad(self.root)

def _profundidad(self, nodo) -> int:
    if nodo.children.head is None:
        return 0
    max_prof = 0
    for hijo in nodo.children:
        prof = self._profundidad(hijo)
        if prof > max_prof:
            max_prof = prof
    return 1 + max_prof

def contiene(self, clave: str) -> bool:
    """Retorna True si existe algún nodo con esa clave en el árbol."""
    return self._find(self.root, clave) is not None

def claves_hoja(self) -> list:
    """Retorna una lista con las claves de todos los nodos hoja del árbol."""
    resultado = []
    self._recolectar_hojas(self.root, resultado)
    return resultado

def _recolectar_hojas(self, nodo, resultado: list) -> None:
    if nodo is None:
        return
    if nodo.children.head is None:
        clave = list(nodo.value.keys())[0]
        resultado.append(clave)
        return
    for hijo in nodo.children:
        self._recolectar_hojas(hijo, resultado)

def insertar_unico(self, padre, valor: dict) -> None:
    """Insert que verifica que no exista ya un nodo con esa clave en el mismo nivel."""
    nueva_clave = list(valor.keys())[0]
    nodo_padre = self._find(self.root, padre)
    if nodo_padre is None:
        print(f"No se encontró el padre '{padre}'.")
        return
    for hijo in nodo_padre.children:
        if list(hijo.value.keys())[0] == nueva_clave:
            print(f"Ya existe un nodo con clave '{nueva_clave}' en ese nivel.")
            return
    from arbol_json import GeneralNode
    nodo_padre.children.append(GeneralNode(valor))

def bfs(self) -> None:
    """Recorre el árbol nivel por nivel (anchura) usando LinkedList como cola."""
    if self.root is None:
        return
    from lista_enlazada import LinkedList
    cola = LinkedList()
    cola.append(self.root)
    while cola.size > 0:
        nodo = cola.head.value
        cola.delete_at_pos(0)
        print(repr(nodo))
        for hijo in nodo.children:
            cola.append(hijo)

def actualizar_valor(self, clave: str, nuevo_valor) -> None:
    """Actualiza el valor de un nodo hoja. Si tiene hijos no lo modifica."""
    nodo = self._find(self.root, clave)
    if nodo is None:
        print(f"No se encontró el nodo con clave '{clave}'.")
        return
    if nodo.children.head is not None:
        print(f"El nodo '{clave}' no es hoja, no se puede actualizar.")
        return
    nodo.value[clave] = nuevo_valor


# ----------------------------------------------------------------
# ARCHIVO: consultas.py  →  dentro de la clase Consultas
# ----------------------------------------------------------------

def contar(self, buscar: dict) -> int:
    """Retorna cuántos documentos cumplen el filtro dado."""
    if self.data.head is None:
        return 0
    total = 0
    current = self.data.head
    while current is not None:
        arbol = current.value
        cumple_todo = True
        for clave, valor in buscar.items():
            if not self._cumple_condicion(arbol, clave, valor):
                cumple_todo = False
                break
        if cumple_todo:
            total += 1
        current = current.next
    return total

def find_one(self, buscar: dict):
    """Retorna el primer documento que cumpla el filtro, o None si no hay ninguno."""
    if self.data.head is None:
        return None
    current = self.data.head
    while current is not None:
        arbol = current.value
        cumple_todo = True
        for clave, valor in buscar.items():
            if not self._cumple_condicion(arbol, clave, valor):
                cumple_todo = False
                break
        if cumple_todo:
            return arbol
        current = current.next
    return None

def eliminar(self, buscar: dict) -> None:
    """Elimina todos los documentos que cumplan el filtro."""
    if self.data.head is None:
        return
    pos = 0
    current = self.data.head
    while current is not None:
        arbol = current.value
        cumple_todo = True
        for clave, valor in buscar.items():
            if not self._cumple_condicion(arbol, clave, valor):
                cumple_todo = False
                break
        siguiente = current.next
        if cumple_todo:
            self.data.delete_at_pos(pos)
        else:
            pos += 1
        current = siguiente

def actualizar(self, buscar: dict, cambios: dict) -> None:
    """Actualiza los campos indicados en todos los documentos que cumplan el filtro."""
    resultados = self.find(buscar)
    for arbol in resultados:
        for clave, nuevo_valor in cambios.items():
            arbol.actualizar_valor(clave, nuevo_valor)

def existe(self, buscar: dict) -> bool:
    """Retorna True si existe al menos un documento que cumpla el filtro."""
    return self.find_one(buscar) is not None

def max_valor(self, campo: str):
    """Retorna el valor máximo de un campo numérico en toda la colección."""
    maximo = None
    current = self.data.head
    while current is not None:
        arbol = current.value
        partes = campo.split(".")
        valor = self._buscar_ruta(arbol.root, partes)
        if valor is not None and isinstance(valor, (int, float)):
            if maximo is None or valor > maximo:
                maximo = valor
        current = current.next
    return maximo

def min_valor(self, campo: str):
    """Retorna el valor mínimo de un campo numérico en toda la colección."""
    minimo = None
    current = self.data.head
    while current is not None:
        arbol = current.value
        partes = campo.split(".")
        valor = self._buscar_ruta(arbol.root, partes)
        if valor is not None and isinstance(valor, (int, float)):
            if minimo is None or valor < minimo:
                minimo = valor
        current = current.next
    return minimo

def distinct(self, campo: str) -> list:
    """Retorna todos los valores únicos de un campo en la colección."""
    vistos = []
    current = self.data.head
    while current is not None:
        arbol = current.value
        partes = campo.split(".")
        valor = self._buscar_ruta(arbol.root, partes)
        if valor is not None and valor not in vistos:
            vistos.append(valor)
        current = current.next
    return vistos