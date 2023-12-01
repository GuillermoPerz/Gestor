import csv
import config

class Cliente:
    def __init__(self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f"({self.dni}) {self.nombre} {self.apellido})"
    
class Clientes:

    lista = []
    with open(config.DATABASE_PATH, newline='\n') as fichero:
        reader = csv.reader(fichero, delimiter= ';')
        for dni, nombre, apellido in reader:
            cliente = Cliente(dni, nombre, apellido)
            lista.append(cliente)

    # añadimos metodos estaticos para la clase, no para la instancia

    @staticmethod
    def buscar(dni):
        '''Busca y devuelve el cliente si se ha encontrado, si no, no devuelve nada'''
        for cliente in Clientes.lista:
            if cliente.dni == dni:
                return cliente
            

    @staticmethod
    def crear(dni, nombre, apellido):
        '''Crea un cliente a partir de un DNI,nombre y apellido y devuelve el cliente que se crea
        '''
        cliente = Cliente(dni, nombre, apellido)
        Clientes.lista.append(cliente)
        Clientes.guardar()
        return cliente
    
    @staticmethod
    def modificar(dni, nombre, apellido):
        '''Modifica a partir de un DNI los campos de nombre y apellido y tambien devuelve el cliente modificado
        '''
        for indice, cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                Clientes.lista[indice].nombre = nombre
                Clientes.lista[indice].apellido = apellido
                Clientes.guardar()
                return Clientes.lista[indice]
            
    @staticmethod
    def borrar(dni):
        '''Borra a partir de un DNI y devuelve el cliente borrado, si comprobamos depues si esta en la lista no estara, porque en clientes lista se habra borrado
        '''
        for indice, cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                cliente = Clientes.lista.pop(indice)
                Clientes.guardar()
                return cliente
            
    @staticmethod
    def guardar():
        ''''''
        with open(config.DATABASE_PATH, 'w', newline = '\n') as fichero:
            writer = csv.writer(fichero, delimiter= ';')
            for cliente in Clientes.lista:
                writer.writerow((cliente.dni, cliente.nombre, cliente.apellido))
