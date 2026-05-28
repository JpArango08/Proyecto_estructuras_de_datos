#Eliminar por nombre de archivo
        elif opcion == "5": 
            eliminar = input("Nombre del archivo a eliminar: ")
            print(consultas.data)
            antes = consultas.data.size
            consultas.eliminar_doc(eliminar)
            if consultas.data.size < antes: 
                print("Documento eliminado correctamente")
            else: 
                print("No se encontro el documento")
            print(consultas.data)
        else:
            print("Opción inválida")

#