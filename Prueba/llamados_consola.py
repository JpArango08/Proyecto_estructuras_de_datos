from consultas import Consultas


def menu():

    consultas = Consultas()

    while True:

        print("\n===== MINI MOTOR DOCUMENTAL =====")
        print("1. Cargar archivo JSON")
        print("2. Buscar documentos (find)")
        print("3. Guardar árbol a JSON")
        print("4. Contar documentos por filtro")
        print("5. Buscar primer documento que cumpla filtro")
        print("6. Eliminar documentos por filtro")
        print("7. Actualizar documentos por filtro")
        print("8. Verificar si existe un documento")
        print("9. Valor máximo de un campo")
        print("10. Valor mínimo de un campo")
        print("11. Valores únicos de un campo")
        print("12. Salir")

        opcion = input("\nSeleccione una opción: ")

        if consultas.data.head is None and opcion not in ("1", "12"):
            print("No hay documentos cargados. Cargue un archivo primero.")
            continue

        if opcion == "1":
            nombre = input("Nombre del archivo JSON: ")
            try:
                consultas.load(nombre)
                print("Archivo cargado correctamente")
            except FileNotFoundError:
                print("El archivo no existe")
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == "2":
            consulta_texto = input("Ingrese la consulta (ej: {'ciudad': 'Medellín'}): ")
            try:
                consulta = eval(consulta_texto)
                resultados = consultas.find(consulta)
                if len(resultados) == 0:
                    print("No se encontraron documentos")
                else:
                    print(f"\n===== RESULTADOS ({len(resultados)}) =====")
                    for resultado in resultados:
                        print(resultado)
            except SyntaxError:
                print("Consulta inválida")
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == "3":
            nombre = input("Nombre del archivo de salida: ")
            try:
                consultas.arbol_json(nombre)
                print("Documentos guardados correctamente en formato JSON")
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == "4":
            consulta_texto = input("Ingrese el filtro (ej: {'edad': {'$gte': 18}}): ")
            try:
                consulta = eval(consulta_texto)
                total = consultas.contar(consulta)
                print(f"Documentos que cumplen el filtro: {total}")
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == "5":
            consulta_texto = input("Ingrese el filtro (ej: {'ciudad': 'Bogotá'}): ")
            try:
                consulta = eval(consulta_texto)
                resultado = consultas.find_one(consulta)
                if resultado is None:
                    print("No se encontró ningún documento")
                else:
                    print("\n===== PRIMER RESULTADO =====")
                    print(resultado)
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == "6":
            consulta_texto = input("Ingrese el filtro a eliminar (ej: {'ciudad': 'Bogotá'}): ")
            try:
                consulta = eval(consulta_texto)
                antes = consultas.data.size
                consultas.eliminar(consulta)
                eliminados = antes - consultas.data.size
                print(f"Documentos eliminados: {eliminados}")
                print(consultas.data)
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == "7":
            consulta_texto = input("Ingrese el filtro (ej: {'ciudad': 'Bogotá'}): ")
            cambios_texto = input("Ingrese los cambios (ej: {'ciudad': 'Bogotá D.C.'}): ")
            try:
                consulta = eval(consulta_texto)
                cambios = eval(cambios_texto)
                consultas.actualizar(consulta, cambios)
                print("Documentos actualizados correctamente")
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == "8":
            consulta_texto = input("Ingrese el filtro (ej: {'ciudad': 'Cali'}): ")
            try:
                consulta = eval(consulta_texto)
                resultado = consultas.existe(consulta)
                if resultado:
                    print("Sí existe al menos un documento que cumple el filtro")
                else:
                    print("No existe ningún documento que cumpla el filtro")
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == "9":
            campo = input("Nombre del campo (ej: edad): ")
            resultado = consultas.max_valor(campo)
            if resultado is None:
                print("No se encontraron valores numéricos para ese campo")
            else:
                print(f"Valor máximo de '{campo}': {resultado}")

        elif opcion == "10":
            campo = input("Nombre del campo (ej: edad): ")
            resultado = consultas.min_valor(campo)
            if resultado is None:
                print("No se encontraron valores numéricos para ese campo")
            else:
                print(f"Valor mínimo de '{campo}': {resultado}")

        elif opcion == "11":
            campo = input("Nombre del campo (ej: ciudad): ")
            resultado = consultas.distinct(campo)
            if len(resultado) == 0:
                print("No se encontraron valores para ese campo")
            else:
                print(f"Valores únicos de '{campo}': {resultado}")

        elif opcion == "12":
            print("\n👋 Saliendo...")
            break

        else:
            print("Opción inválida")

menu()