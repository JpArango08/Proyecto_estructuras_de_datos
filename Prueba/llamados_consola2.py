from consultas import Consultas


def menu():

    consultas = Consultas()

    while True:

        print("\n===== MINI MOTOR DOCUMENTAL =====")
        print("1. Cargar archivo JSON")
        print("2. Buscar documentos")
        print("3. Cargar árbol a JSON")
        print("4. Cantidad de documentos")
        print("5. Primer documento")
        print("6. Último documento")
        print("7. Documentos que tienen un campo")
        print("8. Suma de un campo numérico")
        print("9. Promedio de un campo numérico")
        print("10. Invertir colección")
        print("11. Eliminar documento por nombre")
        print("12. Salir")

        opcion = input("\nSeleccione una opción: ")

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
            if consultas.data.head is None:
                print("No hay documentos cargados")
                continue
            consulta_texto = input("\nIngrese la consulta: ")
            try:
                consulta = eval(consulta_texto)
                resultados = consultas.find(consulta)
                if len(resultados) == 0:
                    print("\nNo se encontraron documentos")
                else:
                    print("\n===== RESULTADOS =====")
                    for resultado in resultados:
                        print(resultado)
            except SyntaxError:
                print("Consulta inválida")
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == "3":
            nombre = input("Nombre del archivo JSON: ")
            try:
                consultas.arbol_json(nombre)
                print("Documentos pasados correctamente a formato JSON")
            except FileNotFoundError:
                print("El archivo no existe, necesitas tener uno creado")
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == "4":
            if consultas.data.head is None:
                print("No hay documentos cargados")
                continue
            print(f"Total de documentos: {consultas.size_docs()}")

        elif opcion == "5":
            if consultas.data.head is None:
                print("No hay documentos cargados")
                continue
            print("\n===== PRIMER DOCUMENTO =====")
            print(consultas.primer_documento())

        elif opcion == "6":
            if consultas.data.head is None:
                print("No hay documentos cargados")
                continue
            print("\n===== ÚLTIMO DOCUMENTO =====")
            print(consultas.ultimo_documento())

        elif opcion == "7":
            if consultas.data.head is None:
                print("No hay documentos cargados")
                continue
            campo = input("Nombre del campo a buscar: ")
            resultados = consultas.tiene_campo(campo)
            if len(resultados) == 0:
                print("No se encontraron documentos con ese campo")
            else:
                print(f"\n===== DOCUMENTOS CON CAMPO '{campo}' =====")
                for resultado in resultados:
                    print(resultado)

        elif opcion == "8":
            if consultas.data.head is None:
                print("No hay documentos cargados")
                continue
            campo = input("Nombre del campo numérico: ")
            resultado = consultas.suma_campo(campo)
            if resultado is None:
                print("No se encontraron valores numéricos para ese campo")
            else:
                print(f"Suma de '{campo}': {resultado}")

        elif opcion == "9":
            if consultas.data.head is None:
                print("No hay documentos cargados")
                continue
            campo = input("Nombre del campo numérico: ")
            resultado = consultas.promedio_campo(campo)
            if resultado is None:
                print("No se encontraron valores numéricos para ese campo")
            else:
                print(f"Promedio de '{campo}': {resultado}")

        elif opcion == "10":
            if consultas.data.head is None:
                print("No hay documentos cargados")
                continue
            consultas.data.invertir()
            print("Colección invertida correctamente")
            print(consultas.data)

        elif opcion == "11":
            if consultas.data.head is None:
                print("No hay documentos cargados")
                continue
            print("Documentos disponibles:")
            current = consultas.data.head
            while current is not None:
                nombre = list(current.value.root.value.keys())[0]
                print(f"  → {nombre}")
                current = current.next
            eliminar = input("Nombre del documento a eliminar: ")
            antes = consultas.data.size
            consultas.eliminar_doc(eliminar)
            if consultas.data.size < antes:
                print("Documento eliminado correctamente")
            else:
                print("No se encontró el documento")
            print(consultas.data)

        elif opcion == "12":
            print("\n👋 Saliendo...")
            break

        else:
            print("Opción inválida")

menu()