

import Ejercicios2.Ejercicio1 as ej1
import Ejercicios2.Ejercicio2 as ej2
import Ejercicios2.Ejercicio3 as ej3
import Ejercicios2.Ejercicio4 as ej4
import Ejercicios2.Ejercicio5 as ej5
import Ejercicios2.Ejercicio6 as ej6
import Ejercicios2.Ejercicio9 as ej9



import Ejercicios.Ejercicio7 as ej7
import Ejercicios.Ejercicio8 as ej8
import Ejercicios.Ejercicio10 as ej7

def main():
    print("--------Inicio del Programa---------")
    print("Elije un ejercicio del 1-11")
    print("Para salir escriba 0")

    while True:
    
        _getInput=input("Seleciona un ejercicio: ")

        try:
            int(_getInput)

            if _getInput=='0':
                print('Fin del programa')
                break
            elif _getInput=='1':
                
        except ValueError:
            print("Solo se permiten valores enteros del 0 al 11")
            return True

