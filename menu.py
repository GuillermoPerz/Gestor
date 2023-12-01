import os

import helpers
import database as db

def iniciar():
    '''Inicia el menu'''

    while True:

        print("/////////////////////////////")
        print("     Bienvenido al Gestor    ")
        print("/////////////////////////////")
        print("[1] Listar los clientes      ")
        print("[2] Buscar un cliente        ")
        print("[3] Añadir o crear un cliente")
        print("[4] Modificar un cliente     ")
        print("[5] Borrar un cliente        ")
        print("[6] Cerrar gestor            ")
        print("/////////////////////////////")

        opcion = input("> ")
        helpers.limpiar_pantalla()

        if opcion == '1':

            '''Opcion 1 nos permite ver los clientes que tenemos listados'''

            print('Listando los clientes...\n')
            for cliente in db.Clientes.lista:
                print(cliente)

        if opcion == '2':

            '''Opcion 2 nos permite buscar los clientes que tenemos en la DB'''

            print('Buscando los clientes...\n')
            dni = helpers.leer_texto(3,3,"DNI (2 int y 1 char)").upper()
            cliente = db.Clientes.buscar(dni)
            print(cliente) if cliente else print("cliente no encontrado")

        if opcion == '3':

            '''Opcion 3 nos permite añadir nuevos clientes a la DB'''

            print('Añadiendo los clientes...\n')
            dni = None
            while True:
                dni = helpers.leer_texto(3,3,"DNI (2 int y 1 char)").upper()
                if helpers.dni_valido(dni, db.Clientes.lista):
                    break
                '''Hasta que el DNI no sea correcto no se rompe el bucle while'''
            nombre = helpers.leer_texto(2,30,"Nombre (2 a 30 chars)").capitalize()
            apellido = helpers.leer_texto(2,30,"Apellido (2 a 30 chars)").capitalize()
            db.Clientes.crear(dni, nombre, apellido)
            print("Cliente añadido correctamente.")

        if opcion == '4':

            '''Opcion 4 nos permite modificar nombre y/o apellido de los clientes de nuestra DB'''

            print('Modificando los clientes...\n')
            dni = helpers.leer_texto(3,3,"DNI (2 int y 1 char)").upper()
            cliente = db.Clientes.buscar(dni)
            if cliente:
                nombre = helpers.leer_texto(2,30, f"Nombre (2 a 30 chars) [{cliente.nombre}]").capitalize()
                apellido = helpers.leer_texto(2,30, f"Apellido (2 a 30 chars) [{cliente.apellido}]").capitalize()
                db.Clientes.modificar(cliente.dni, nombre, apellido)
                print("Cliente creado correctamente.")
            else:
                print("Cliente no encontrado.")

        if opcion == '5':

            '''Opcion 5 nos permite eliminar clientes de nuestra DB'''

            print('Borrando el cliente...\n')
            dni = helpers.leer_texto(3,3,"DNI (2 int y 1 char)").upper()
            print("Cliente borrado correctamente") if db.Clientes.borrar(dni) else print("Cliente no encontrado.")

        if opcion == '6':

            '''Opcion 6 nos da la opcion de cerrar el gestor'''

            print('Cerrando el gestor...\n')
            break

        input("\nPresiona enter para continuar...")