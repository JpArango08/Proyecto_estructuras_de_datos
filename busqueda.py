from consultas import Consultas

c = Consultas()
c.load("datos.json")

print("=" * 50)
print("1. VALOR SIMPLE")
print("=" * 50)
resultado = c.find({"ciudad": "Bogotá"})
for arbol in resultado:
    print(arbol)

print("=" * 50)
print("2. OPERADOR $gt")
print("=" * 50)
resultado = c.find({"edad": {"$gt": 25}})
for arbol in resultado:
    print(arbol)

print("=" * 50)
print("3. RUTA ANIDADA")
print("=" * 50)
resultado = c.find({"direccion.barrio": "Laureles"})
for arbol in resultado:
    print(arbol)

print("=" * 50)
print("4. MÚLTIPLES OPERADORES")
print("=" * 50)
resultado = c.find({"edad": {"$gte": 18, "$lte": 30}})
for arbol in resultado:
    print(arbol)

print("=" * 50)
print("5. OPERADOR $ne")
print("=" * 50)
resultado = c.find({"ciudad": {"$ne": "Bogotá"}})
for arbol in resultado:
    print(arbol)

print("=" * 50)
print("6. MÚLTIPLES CONDICIONES")
print("=" * 50)
resultado = c.find({"ciudad": "Medellín", "edad": {"$gte": 18}})
for arbol in resultado:
    print(arbol)

print("=" * 50)
print("7. SIN RESULTADOS")
print("=" * 50)
resultado = c.find({"ciudad": "Cali"})
print(f"Documentos encontrados: {len(resultado)}")

print("=" * 50)
print("8. COLECCIÓN VACÍA")
print("=" * 50)
vacia = Consultas()
print(vacia.find({"ciudad": "Medellín"}))