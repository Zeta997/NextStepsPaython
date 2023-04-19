#version 3.11

#Crea un programa en Python que tome una lista de números enteros y devuelva una nueva lista que contenga solo los números que son múltiplos de 3. 

_getInputUser=""
_intValue=[]
_multiplos=[]

def startProgrma():
    while True:       
        _getInputUser=input("Introduce valores: ")
        try:

            int(_getInputUser)
            _intValue.append(_getInputUser)
            _finish=input("¿Deseas finalizar?(si/no): ")
            if _finish=="si":
                _multiplos=[x for x in _intValue if int(x)%3==0]
                if _multiplos==[]:
                    print("No hay multiplos del 3")
                    break 
                else:
                    print(_multiplos)
                    break 
        except ValueError:
            print("Debes introducir un valor entero.")
            continue 


if __name__=="__main__":
    startProgrma()
