import re

digito = re.compile("[1-9]")  
digito_o_zero = re.compile("(?:digito|0)")  
para_entero = re.compile("(?:digito|0)(?:digito_o_zero)*") 
entero = re.compile("(?:para_entero|0)")  
espacio = re.compile(r"\s*")  
ola = re.compile(r"(?:CUPON\s*\(\s*(?:entero|ANS)\s*,\s*espacio*(?:entero|ANS)\s*\))")
clave = re.compile("(?:ANS|ola)")
operador = re.compile(r"(?:espacio*[+\-*//]+espacio*)")  
operacion = re.compile(r"(?:(?:clave|entero)(?:operador(?:entero|clave))*)")  
sentencia = re.compile(r"(?:\(\s*)?(?:(?:clave|entero)(?:operador(?:entero|clave))*(?:\s*\))?)?")  

def lastindex(sentencia2, i):
    a = len(sentencia2) - 1
    while a >= 0:
        if sentencia2[a] == i:
            return a
        else:
            a -= 1
            
def sumayresta(ayuda):
    l = 0
    while l < len(ayuda):
        index = ayuda[l]
        if index == "+":
            op1 = int(ayuda[l-1])
            op2 = int(ayuda[l+1])
            resultadointermedio = op1 + op2
            del ayuda[l-1:l+2]
            ayuda.insert(l-1, resultadointermedio)
        elif index == "-":
            op1 = int(ayuda[l-1])
            op2 = int(ayuda[l+1])
            resultadointermedio = op1 - op2
            del ayuda[l-1:l+2]
            ayuda.insert(l-1, resultadointermedio)
        else:
            l += 1
            
def multiplicaciones(ayuda):
    l = 0
    while l < len(ayuda):
        index = ayuda[l]
        if index == "*":
            op1 = int(ayuda[l-1])
            op2 = int(ayuda[l+1])
            resultadointermedio = op1 * op2
            del ayuda[l-1:l+2]
            ayuda.insert(l-1, resultadointermedio)
        else:
            l += 1

def divisiones(ayuda):
    l = 0
    while l < len(ayuda):
        index = ayuda[l]
        if index == "//":
            op1 = int(ayuda[l-1])
            op2 = int(ayuda[l+1])
            if op2 != 0:
                resultadointermedio = op1 // op2
                del ayuda[l-1:l+2]
                ayuda.insert(l-1, resultadointermedio)
            else:
                return "Error"
        else:
            l += 1
        
        
def operacionesbasicas(match):
    partes = re.split(r"\s*([+\-*]|//)\s*", match)
    while "(" in partes:
        index_open = partes.index("(")
        index_close = partes.index(")", index_open)
        partes = partes[:index_open] + partes[index_open+1:index_close] + partes[index_close+1:]
    print(partes)
    multiplicaciones(partes)
    divisiones(partes)
    sumayresta(partes)
    if int(partes[0]) >= 0:
        return int(partes[0])
    else:
        return 0

def cupon(match):
    if match.group(2) is None:
        x = int(match.group(1))
        return int(x*0.2)
    else:
        x = int(match.group(1))
        y = int(match.group(2))
        return int(x*100/y)
     
             
def hacercupon(match):
    return str(cupon(match))


def validarsintaxis(linea):
    return re.fullmatch(sentencia.pattern, linea) is not None

def evaluar_operacion(operacion2):
    operacion_con_cupon = re.sub(ola.pattern, hacercupon, operacion2)
    operacion_con_ans = operacion_con_cupon.replace("ANS", str(resultado_anterior))
    print(operacion_con_ans)
    a = operacionesbasicas(operacion_con_ans)
    return a

def buscarparentesis(sentencia2):
    index = 0
    while "(" in sentencia2:
        index_open = sentencia2.rindex("(")
        index_close = sentencia2.index(")", index_open)
        operacion = sentencia2[index_open+1:index_close]
        
        if validarsintaxis(operacion):
            resultado_operacion = evaluar_operacion(operacion)
            sentencia2 = sentencia2[:index_open] + str(resultado_operacion) + sentencia2[index_close+1:]
        else:
            return "Sin resolver (error de sintaxis)"
    
    return evaluar_operacion(sentencia2)   

def leerlineas(entrada, salida):
    global resultado_anterior
    for linea in entrada:
        linea = linea.strip()
        if linea == "":
            resultado_anterior = 0
            salida.write(f"\n")
            continue
        else: 
            resultado = buscarparentesis(linea) 
            if resultado != "Error":
                salida.write(f"{linea} = {resultado}\n")
                resultado_anterior = resultado
            elif resultado == "Error":
                salida.write(f"{linea} = Error\n")
            else:
                salida.write(f"{linea} = Sin resolver\n")
    
                      
resultado_anterior = 0         
archivo = open("problemas (EJEMPLO).txt","r")
salida = open("desarrollos.txt", "w")
leerlineas(archivo, salida)
            
archivo.close() 
salida.close()

