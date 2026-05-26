from consultas import Consultas


def menu():

    consultas = Consultas()

    while True:

        print("\n===== MINI MOTOR DOCUMENTAL =====")
        print("1. Cargar archivo JSON")
        print("2. Buscar documentos")
        print("3. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":

            nombre = input("Nombre del archivo JSON: ")

            try:
                consultas.load(nombre)
                print("✅ Archivo cargado correctamente")
            except FileNotFoundError:
                print("❌ El archivo no existe")
            except Exception as e:
                print( f"❌ Error: {e}")

        elif opcion == "2":

            if consultas.data.head is None:
                print("⚠️ No hay documentos cargados")
                continue

            consulta_texto = input("\nIngrese la consulta: ")
            try:
                consulta = eval(consulta_texto)
                resultados = consultas.find(consulta)

                if len(resultados) == 0:
                    print("\n⚠️ No se encontraron documentos")
                else:
                    print("\n===== RESULTADOS =====")
                    for resultado in resultados:
                        print(resultado)

            except SyntaxError:
                print("❌ Consulta inválida")
            except Exception as e:
                print(f"❌ Error: {e}")

        elif opcion == "3":
            print("\n👋 Saliendo...")
            break

        else:
            print("⚠️ Opción inválida")


menu()