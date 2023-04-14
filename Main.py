from Ejercicios2 import Ejercicio1 
from Ejercicios2 import Ejercicio2
from Ejercicios2 import Ejercicio3
from Ejercicios2 import Ejercicio4
from Ejercicios2 import Ejercicio5
from Ejercicios2 import Ejercicio6
from Ejercicios2 import Ejercicio9
# from Ejercicios2 import *
from Ejercicios import Ejercicio7
from Ejercicios import Ejercicio8
from Ejercicios import Ejercicio10 
from Ejercicios import Ejercicio11 


def _main():
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
                Ejercicio1.ejercicio1()
                break
            elif _getInput=='2':
                Ejercicio2.Ejercicio2()
                break
            elif _getInput=='3':
                Ejercicio3.Ejercicio3()
                break
            elif _getInput=='4':
                Ejercicio4.Ejercicio4()
                break
            elif _getInput=='5':
                Ejercicio5.Ejercicio5()
                break
            elif _getInput=='6':
                Ejercicio6.Ejercicio6()
                break
            elif _getInput=='7':
                Ejercicio7._startProgram()
                break
            elif _getInput=='8':
                Ejercicio8._startProgram()
                break
            elif _getInput=='9':
                Ejercicio9.Ejercicio9() 
                break
            elif _getInput=='10':
                Ejercicio10._startPogram()
                break
            elif _getInput=='11':
                Ejercicio11._startProgrma()
                break
        except ValueError:
            print("Solo se permiten valores enteros del 0 al 11")
            return True


_main()