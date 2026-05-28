# ================================================================
#  FUNCIONES PARA EL EXAMEN — CORREGIDAS SIN __iter__
#  Copia cada bloque en el archivo que corresponde
# ================================================================


# ----------------------------------------------------------------
# ARCHIVO: lista_docs.py  →  dentro de la clase ListaDocs
# ----------------------------------------------------------------

def eliminar_por_nombre(self, nombre: str) -> None:
    if self.head is None:
        return
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
    return self._contar(self.root)

def _contar(self, nodo) -> int:
    if nodo is None:
        return 0
    total = 1
    current = nodo.children.head
    while current is not None:
        total += self._contar(current.value)
        current = current.next
    return total

def profundidad(self) -> int:
    if self.root is None:
        return -1
    return self._profundidad(self.root)

def _profundidad(self, nodo) -> int:
    if nodo.children.head is None:
        return 0
    max_prof = 0
    current = nodo.children.head
    while current is not None:
        prof = self._profundidad(current.value)
        if prof > max_prof:
            max_prof = prof
        current = current.next
    return 1 + max_prof

def contiene(self, clave: str) -> bool:
    return self._find(self.root, clave) is not None

def claves_hoja(self) -> list:
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
    current = nodo.children.head
    while current is not None:
        self._recolectar_hojas(current.value, resultado)
        current = current.next

def insertar_unico(self, padre, valor: dict) -> None:
    nueva_clave = list(valor.keys())[0]
    nodo_padre = self._find(self.root, padre)
    if nodo_padre is None:
        print(f"No se encontró el padre '{padre}'.")
        return
    current = nodo_padre.children.head
    while current is not None:
        if list(current.value.value.keys())[0] == nueva_clave:
            print(f"Ya existe un nodo con clave '{nueva_clave}' en ese nivel.")
            return
        current = current.next
    from arbol_json import GeneralNode
    nodo_padre.children.append(GeneralNode(valor))

def bfs(self) -> None:
    if self.root is None:
        return
    from lista_enlazada import LinkedList
    cola = LinkedList()
    cola.append(self.root)
    while cola.size > 0:
        nodo = cola.head.value
        cola.delete_at_pos(0)
        print(repr(nodo))
        current = nodo.children.head
        while current is not None:
            cola.append(current.value)
            current = current.next

def actualizar_valor(self, clave: str, nuevo_valor) -> None:
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
    resultados = self.find(buscar)
    for arbol in resultados:
        for clave, nuevo_valor in cambios.items():
            arbol.actualizar_valor(clave, nuevo_valor)

def existe(self, buscar: dict) -> bool:
    return self.find_one(buscar) is not None

def max_valor(self, campo: str):
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