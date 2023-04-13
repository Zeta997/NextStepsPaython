

import Ejercicios2.Ejercicio1 as ej1
import Ejercicios2.Ejercicio2 as ej2
import Ejercicios2.Ejercicio3 as ej3
import Ejercicios2.Ejercicio4 as ej4
import Ejercicios2.Ejercicio5 as ej5
import Ejercicios2.Ejercicio6 as ej6
import Ejercicios2.Ejercicio9 as ej9


import Ejercicios.Ejercicio7 as ej7
import Ejercicios.Ejercicio8 as ej8
import Ejercicios.Ejercicio10 as ej10
import Ejercicios.Ejercicio11 as ej11

def main():
    print("--------Inicio del Programa---------")
    print("Elije un ejercicio del 1-11")
    print("Para salir escriba 0")

    while True:
    
        _getInput=input("Seleciona un ejercicio: ")

        try:
            int(_getInput)
       
        except ValueError:
            print("Solo se permiten valores enteros del 0 al 11")
            return True
        else:
            if _getInput=='0':
                print('Fin del programa')
                break
            elif _getInput=='1':
                ej1.Ejercicios1()
                break
            elif _getInput=='2':
                ej2.Ejercicio2()
                break
            elif _getInput=='3':
                ej3.Ejercicio3()
                break
            elif _getInput=='4':
                ej4.Ejercicio4()
                break
            elif _getInput=='5':
                ej5.Ejercicios1()
                break
            elif _getInput=='6':
                ej6.Ejercicios1()
                break
            elif _getInput=='7':
                ej7._startProgram()
                break
            elif _getInput=='8':
                ej8._startProgram()
                break
            elif _getInput=='9':
                ej9.Ejercicio9()  
                break
            elif _getInput=='10':
                ej10._startPogram()
                break
            elif _getInput=='11':
                ej11._startProgrma()
                break


main()