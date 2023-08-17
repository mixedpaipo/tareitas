import re

digito = re.compile("[1-9]")  
digito_o_zero = re.compile("(?:digito|0)")  
para_entero = re.compile("(?:digito|0)(?:digito_o_zero)*") 
entero = re.compile("(?:para_entero|0)")  
espacio = re.compile(r"\s*")  
ola = re.compile(r"(?:CUPON\s*\(\s*(?:entero|ANS)\s*,\s*espacio*(?:entero|ANS)\s*\))")
clave = re.compile("(?:ANS|ola)")
operador = re.compile(r"(?:espacio*[+\-*/]espacio*)")  
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
    partes = re.split(operacion.pattern, alo)
    if len(partes) == 3:
        op1 = partes[0]
        op2 = partes[2]
        operador = partes[1]
        if operador == "*":
            return int(op1 * op2)
        elif operador == "//":
            if op2 == 0:
                return "Error"
            else: 
                return int(op1 // op2)
        elif operador ==  "+":
            return int(op1 + op2)
        elif operador == "-":
            return int(op1 - op2)
    else: 
        return "Error"       
 
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
    return eval(int(operacion_con_ans))

    
def buscarparentesis(sentencia2, inicio=0):
    pila = []
    i = inicio
    while i < len(sentencia2):
        if sentencia2[i] == "(":
            pila.append(i)
        elif sentencia2[i] == ")":
            if pila:
                inicio_paren = pila.pop()
                operacion = sentencia2[inicio_paren+1:i]
                if validarsintaxis(operacion):
                    resultado = evaluar_operacion(operacion)
                    sentencia2 = sentencia2[:inicio_paren] + str(resultado) + sentencia2[i+1:]
                    i = inicio_paren + len(str(resultado))
                else:
                    return "Sin resolver"
        i += 1
    return sentencia2
            

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
            if resultado != "Sin resolver":
                print(resultado)
                salida.write(f"{linea} = {resultado}\n")
                resultado_anterior = resultado
            else:
                salida.write(f"{linea} = Sin resolver\n")
    
                      
resultado_anterior = 0         
archivo = open("problemas (EJEMPLO).txt","r")
salida = open("desarrollos.txt", "w")
leerlineas(archivo, salida)
            
archivo.close() 
salida.close()

