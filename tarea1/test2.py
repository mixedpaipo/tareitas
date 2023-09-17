import re

digito = re.compile("[1-9]")  
digito_o_zero = re.compile("[1-9]|0")  
entero = re.compile("([1-9][0-9]*|0)")  
espacio = re.compile(r"\s*")  
clave = re.compile("(?:ANS|CUPON\(\s*(?:entero|ANS)\s*(?:,\s*(?:entero|ANS)\s*)?\))")
operador = re.compile(r"\s*[+\-*/]{1}\s*")  
operacion = re.compile(r"(?:(?:clave|entero)(?:operador(?:entero|clave))*)")  
sentencia = re.compile(r"(?:operacion(?:operador(?:entero|clave))*)")

def lastindex(sentencia2, i):
    a = len(sentencia2) - 1
    while a >= 0:
        if sentencia2[a] == i:
            return a
        else:
            a -= 1
            
def operacionesbasicas(match):
    alo = match.group(0)
    partes = re.split(operador.pattern, alo)
    if len(partes) == 3:
        op1 = partes[0]
        op2 = partes[2]
        operador = partes[1]
        if operador == "+":
            return str(int(op1) + int(op2))
        elif operador == "-":
            return str(int(op1) - int(op2))
        elif operador == "*":
            return str(int(op1) * int(op2))
        elif operador == "//":
            if op2 == "0":
                return "Error"        
            else:
                return str(int(op1) // int(op2))
    else: 
        return "Error"       
 
def cupon(match):
    if match.group(2) is None:
        x = int(match.group(1))
        return str(int(x * 0.2))
    else:
        x = int(match.group(1))
        y = int(match.group(2))
        return str(int(x * 100 / y))
     
             
def hacercupon(match):
    return str(cupon(match))

def validarsintaxis(sentencia2):
    return sentencia.fullmatch(sentencia2) is not None

def validaroperacion(operacion3):
    if operacion.fullmatch(operacion3) is not None:
        return True
    else: 
        return False

def evaluar_operacion(operacion2):
    operacion_con_cupon = re.sub(clave.pattern, hacercupon, operacion2)
    operacion_con_ans = operacion_con_cupon.replace("ANS", str(resultado_anterior))
    operacion_con_resultados = re.sub(operacion.pattern, operacionesbasicas, operacion_con_ans)
    return operacion_con_resultados
    
    
def buscarparentesis(sentencia2): 
    index = 0
    for i in sentencia2:
        if (i == "("):
            index = lastindex(sentencia2, i)
            continue
        elif(i == ")"): 
            o = int(sentencia2.index(i))
            operacion = sentencia2[index+1:o]
            if validaroperacion(operacion):
                pro = evaluar_operacion(operacion)
                return buscarparentesis(sentencia2[:index] + str(pro) + sentencia2[o+1:])
            else:
                return "Sin resolver (error de sintaxis)"
    return evaluar_operacion(sentencia2)
        
def leerlineas(entrada, salida):
    global resultado_anterior
    for linea in entrada:
        linea = linea.strip()
        if linea == "":
            resultado_anterior = 0
            salida.write("\n")
            continue
        else:
            if validarsintaxis(linea):
                resultado = buscarparentesis(linea)
                if isinstance(resultado, int):
                    salida.write(f"{linea} = {resultado}\n")
                    resultado_anterior = resultado
                else:
                    salida.write(f"{linea} = Sin resolver (error en operación)\n")
            else:
                salida.write(f"{linea} = Sin resolver (error de sintaxis)\n")
                

            
resultado_anterior = 0         
archivo = open("problemas (EJEMPLO).txt","r")
salida = open("desarrollos.txt", "w")
leerlineas(archivo, salida)
            
archivo.close() 
salida.close()