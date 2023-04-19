#version3.11

#Crea un un programa en Python que tome una lista de cadenas de caracteres y devuelva una nueva lista que contenga solo las cadenas que contienen al menos una vocal.


_getStringInputUser=""
_listVowel=['a','e','i','o','u','A','E','I','O','U']
_listAllString=[]
_listStringWithVowel=[]

def startPogram():
    
    while True:
        _getStringInputUser= input("Introduce una cadena de caracteres: ")
        _listAllString.append(_getStringInputUser)       
        _getInputUser=input("¿Quieres finalizar el programa(si/no): ")
        if _getInputUser== "si":
            CompareVowel()
            print(_listStringWithVowel)
            break
    
def CompareVowel():
    
    for i in _listAllString:
            _valoranadido=False      
            for a in i[0:]: 
                if not _valoranadido:
                    for e in _listVowel[0:]:
                        if a==e:
                            _listStringWithVowel.append(i)
                            _valoranadido=True
                            break
                else:
                    break


if __name__=="__main__":
    startPogram()