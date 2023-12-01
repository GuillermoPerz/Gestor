import os
import platform 
import re

def limpiar_pantalla():
    '''Funcion auciliar que nos permite hacer el clean de la app en cualquier os'''
    os.system('cls') if platform.system() == 'Windows' else os.system('clear') #clear en Mac y Linux. Limpia lo que se muestra.

def leer_texto(longitud_min=0, longitud_max=100, mensaje=None):
    print(mensaje) if mensaje else None
    '''Nos permite ejecutar una instruccion si se cumple una condicion (if) en caso contrario no hace nada'''
    while True:
        texto = input('> ')
        if len(texto) >= longitud_min and len(texto) <= longitud_max:
            return texto
        
def dni_valido(dni, lista):
    '''Solicita a traves de una expresion regular 2 digitos de 0 a 9 y una letra de la A a la Z.'''
    if not re.match('[0-9]{2}[A-Z]$', dni):
        print('DNI incorrecto, debe cumplir el formato')
        return False
    for cliente in lista:
        if cliente.dni == dni:
            print('DNI utilizado por otro cliente')
            return False
    return True