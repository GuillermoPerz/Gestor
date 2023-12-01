import config
import csv
import copy
import unittest
import helpers
import database as db

class TestDatabase(unittest.TestCase):

    def setUp(self):
        '''Prepara los test y crea unas estancias de cliente independientes'''
        db.Clientes.lista = [
            db.Cliente('48H', 'Manolo', 'Concha'),
            db.Cliente('15J', 'Marta', 'Lopez'),
            db.Cliente('28Z', 'Ana', 'Garcia'),
        ]

    def test_buscar_cliente(self):
        '''Test que comprueba si funciona correctamente la funcion de buscar clientes'''
        cliente_existente = db.Clientes.buscar('15J')
        cliente_inexistente = db.Clientes.buscar('22D')
        self.assertIsNotNone(cliente_existente)
        self.assertIsNone(cliente_inexistente)

    def test_crear_cliente(self):
        '''Test que comprueba si funciona correctamente la funcion de crear clientes'''
        nuevo_cliente = db.Clientes.crear('39X', 'Guillermo', 'Perez')
        self.assertEqual(len(db.Clientes.lista), 4)
        self.assertEqual(nuevo_cliente.dni, '39X')
        self.assertEqual(nuevo_cliente.nombre, 'Guillermo')
        self.assertEqual(nuevo_cliente.apellido, 'Perez')


    def test_modificar_cliente(self):
        '''Test que comprueba si funciona correctamente la funcion de modificar clientes'''
        cliente_a_modificar = copy.copy(db.Clientes.buscar('48H'))
        cliente_modificado = db.Clientes.modificar('48H', 'Manuel', 'Concha')
        self.assertEqual(cliente_a_modificar.nombre, 'Manolo')
        self.assertEqual(cliente_modificado.nombre, 'Manuel')

    def test_borrar_cliente(self):
        '''Test que comprueba si funciona correctamente la funcion de borrar clientes'''
        cliente_borrado = db.Clientes.borrar('15J')
        cliente_rebuscado = db.Clientes.buscar('15J')
        self.assertEqual(cliente_borrado.dni, '15J')
        self.assertIsNone(cliente_rebuscado)

    def test_dni_valido(self):
        '''Test que comprueba si funciona correctamente la funcion de validacion DNIs'''
        self.assertTrue(helpers.dni_valido('00A', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('12345X', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('F23', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('28Z', db.Clientes.lista))

    def test_escritura_csv(self):
        db.Clientes.borrar('48H')
        db.Clientes.borrar('15J')
        db.Clientes.modificar('28Z', 'Mariana', 'Garcia')

        dni, nombre, apellido = None, None, None
        with open(config.DATABASE_PATH, newline = '\n') as fichero:
            reader = csv.reader(fichero, delimiter=';')
            dni, nombre, apellido = next(reader)

        self.assertEqual(dni, '28Z')
        self.assertEqual(nombre, 'Mariana')
        self.assertEqual(apellido, 'Garcia')