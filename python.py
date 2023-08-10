import re

ANS = 0

digito = re.compile("[1-9]")
digito_o_zero = re.compile("digito | 0")
para_entero = re.compile( "digito+digito_o_zero*")
entero = re.compile("para_entero|0")
espacio = re.compile("")
coma = re.compile(",")
ola = re.compile("CUPON(espacio* (entero|ANS) ((espacio*)  ","  espacio* (entero|ANS) espacio*)?")
clave = re.compile("ANS| ola")
operador = re.compile( "espacio* ("+"|"-"|"*"|"//") espacio*")
operacion = re.compile("(clave|entero) (operador)? (clave|entero)")
sentencia = re.compile("operacion+(operador (entero|clave))*")    

def CUPON(x,y):
    if (y == 0):
        a = int((x*20)/100)
        return a
    else:
        b = int((x*y)/100)
        return b 
    

def leerlineas(file,i):
    b = file.readlines(i)
    if (b != "\n"):
        if(sentencia.match(b) is True):
            
            
        
        
archivo = open("problemas (EJEMPLO).txt","r")
i = 0
for lines in archivo:
    i += 1
    leerlineas(archivo,i)
            
                
archivo.close() 
