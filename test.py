import re


def lastindex(sentencia, i):
    a = len(sentencia) - 1
    while a >= 0:
        if sentencia[a] == i:
            return a
        else:
             a -= 1
        
    
def buscarparentesis(sentencia): 
    index = 0
    for i in sentencia:
        if (i == "("):
            index = lastindex(sentencia, i)
            continue
        elif(i == ")"): 
            o = int(sentencia.index(i))
            pro = (sentencia[index+1:o])
            buscarparentesis(pro)
            
# Definir expresiones regulares
digito = re.compile("[1-9]")  # Dígito del 1 al 9
digito_o_zero = re.compile("(?:digito|0)")  # Dígito o el número 0
para_entero = re.compile("(?:digito|0)(?:digito_o_zero)*")  # Dígitos o cero repetidos (para formar enteros)
entero = re.compile("(?:para_entero|0)")  # Entero o 0
espacio = re.compile(r"\s*")  # Espacios en blanco (usamos \s para espacios, tabulaciones, saltos de línea, etc.)
ola = re.compile(r"(?:CUPON(?:espacio*(?:entero|ANS)(?:espacio*,\s*espacio*(?:entero|ANS))*)?)")
clave = re.compile("(?:ANS|ola)")  # Clave es "ANS" o "ola"
operador = re.compile(r"(?:espacio*[+\-*/]espacio*)")  # Operadores (+, -, *, /) con espacios opcionales alrededor
operacion = re.compile(r"(?:(?:clave|entero)(?:operador(?:entero|clave))*)")  # Operaciones
sentencia = re.compile(r"(?:operacion(?:operador(?:entero|clave))*)")  # Sentencia


    
            
