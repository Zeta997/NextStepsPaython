#version 3.11

#Crea un programa en Python que acepte una lista de cadenas de caracteres y devuelva una nueva lista que contenga solo las cadenas que tienen más de 5 caracteres.

_getStringUser=""
listString=[]
_getStringFive=[]

def startProgram():
    

    while True:
        _getStringUser=input("Introduce una palabra: ")
        listString.append(_getStringUser.strip())
        _finishProgram=input("¿Desea finalizar?(si/no): ")            
        if _finishProgram=="si":
            CompareText()  
            break


def CompareText():
        _getStringFive=[x for x in listString if len(x)>= 5]       
        if _getStringFive==[]:
            print("La lista está vacía")
        else:
            print(_getStringFive)

          