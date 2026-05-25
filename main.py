from arbol_json import GeneralTree
from lista_docs import ListaDocs

# Documentos de prueba (los del enunciado)
data = [
    {
        "id": 1,
        "nombre": "Ana",
        "edad": 25,
        "ciudad": "Medellín",
        "direccion": {
            "barrio": "Laureles",
            "codigo_postal": 50031
        }
    },
    {
        "id": 2,
        "nombre": "Carlos",
        "edad": 31,
        "ciudad": "Bogotá",
        "direccion": {
            "barrio": "Chapinero",
            "codigo_postal": 110231
        }
    }
]

coleccion = ListaDocs()

# Cargar cada doc como árbol
for doc in data:
    arbol = GeneralTree()
    arbol.load(doc)
    coleccion.append(arbol)

# ── Pruebas ──────────────────────────────────────────────────────────────────

print(f"Tamaño: {coleccion.size}")          # → 2
print("─" * 40)

# Ver cada árbol
coleccion.traverse()
print("─" * 40)

# Acceder al primer nodo directamente
primer_arbol = coleccion.head.value
print("Raíz del primer árbol:", primer_arbol.root)

# Borrar posición 0 y verificar
coleccion.delete_at_pos(0)
print(f"Tamaño tras borrar pos 0: {coleccion.size}")   # → 1
coleccion.traverse()