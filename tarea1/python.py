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
sentencia = re.compile(r"(?:operacion(?:operador(?:entero|clave))*)")  

def lastindex(sentencia2, i):
    a = len(sentencia2) - 1
    while a >= 0:
        if sentencia2[a] == i:
            return a
        else:
            a -= 1
            
def sumayresta(ayuda):
    l = 0
    for index in ayuda:
        if index == "+":
            op1 = int(ayuda[l-1])
            op2 = int(ayuda[l+1])
            del ayuda[l-1:l+2]
            resultadointermedio = op1 + op2
            ayuda.insert(l,resultadointermedio)
            print(ayuda)
        elif index == "-":
            op1 = int(ayuda[l-1])
            op2 = int(ayuda[l+1])
            del ayuda[l-1:l+2]
            resultadointermedio = op1 - op2
            ayuda.insert(l,resultadointermedio)
            print(ayuda)
        
            
            
def multiplicaciones(ayuda):
    l = 0
    for index in ayuda: 
        print(index)
        if index == "*":
            op1 = int(ayuda[l-1])
            op2 = int(ayuda[l+1])
            del ayuda[l-1:l+2]
            resultadointermedio = op1 * op2
            ayuda.insert(l,resultadointermedio)
            print(ayuda)
        else:
            return ayuda
        l += 1
        
    
def divisiones(ayuda):
    l = 0
    for index in ayuda: 
        if index == "//":
            op1 = int(ayuda[l-1])
            op2 = int(ayuda[l+1])
            del ayuda[l-1:l+2]
            resultadointermedio = op1 // op2
            ayuda.insert(l,resultadointermedio)
            print(ayuda)
            divisiones(ayuda)
        else:
            return ayuda
    l += 1
        
        
        
def operacionesbasicas(match):
    partes = re.split(r"\s*([+\-*]|//)\s*", match)
    print(partes)
    resultadointermedio = 0
    partes = multiplicaciones(partes)
    partes = divisiones(partes)
    partes = sumayresta(partes)
    
    
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
    for i in sentencia2:
        if (i == "("):
            index = lastindex(sentencia2, i)
            continue
        elif(i == ")"): 
            o = int(sentencia2.index(i))
            operacion = sentencia2[index+1:o]
            if validarsintaxis(operacion):
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
            salida.write(f"\n")
            continue
        else: 
            resultado = buscarparentesis(linea) 
            if resultado != "Sin resolver":
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

