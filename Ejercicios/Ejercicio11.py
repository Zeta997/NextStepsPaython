#version 3.11

#Crea un programa en Python que tome una lista de números enteros y devuelva una nueva lista que contenga solo los números que son múltiplos de 3. 

_getInputUser=""
_intValue=[]
_multiplos=[]
_endProgram=False

def startProgrma():
    global _getInputUser, _endProgram

    while _endProgram==False:
        
        _getInputUser=input("Introduce valores: ")
        try:

            _getInputUser=int(_getInputUser)
            _intValue.append(_getInputUser)
            FinishProgram()

        except ValueError:
            print("Debes introducir un valor entero.")
            _getInputUser=""


def FinishProgram():


    _finish=input("¿Deseas finalizar?(si/no): ")
    if _finish=="si":
        GetMultiplos()       
    elif _finish=="no":
        _endProgram=False

def GetMultiplos():
    
    for i in _intValue:
        if i%3==0:
            _multiplos.append(i)
        else:
            continue
    print(_multiplos)
    _endProgram=True


