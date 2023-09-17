import re

digito = re.compile("[1-9]")  
digito_o_zero = re.compile("(?:digito|0)")  
para_entero = re.compile("(?:digito|0)(?:digito_o_zero)*") 
entero = re.compile("(?:para_entero|0)")  
espacio = re.compile(r"\s*")  
ola = re.compile(r"CUPON\s*\(\s*-?\d+\s*(?:,\s*-?\d+\s*)?\)")
clave = re.compile("(?:ANS|ola)")
operador = re.compile(r"(?:espacio*[+\-*//]+espacio*)")  
operacion = re.compile(r"(?:(?:clave|entero)(?:operador(?:entero|clave))*)")  
sentencia = re.compile(r"(?:\(\s*)?(?:(?:(?:ANS|(?:CUPON\s*\(\s*(?:(?:(?:[1-9]|0)(?:(?:[1-9]|0))*|0)|ANS)\s*,\s*\s*(?:(?:(?:[1-9]|0)(?:(?:[1-9]|0))*|0)|ANS)\s*\)))|(?:(?:[1-9]|0)(?:(?:[1-9]|0))*|0))(?:(?:\s*[+\-*//]+\s*)([-]?)(?:(?:(?:[1-9]|0)(?:(?:[1-9]|0))*|0)|(?:ANS|(?:CUPON\s*\(\s*(?:(?:[1-9]|0)(?:(?:[1-9]|0))*|ANS)\s*,\s*espacio*(?:(?:(?:[1-9]|0)(?:(?:[1-9]|0))*|0)|ANS)\s*\)))))*(?:\s*\))?)?")  


# Debido a un error de comentación, algunos comentarios serán de esta manera. 
# De ante mano lo lamento, no supe como arreglarlo
            
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
            if (ayuda[l-1]) == "":
                op1 = int(ayuda[l+1])
                op2 = int(ayuda[l+3])
                resultadointermedio = (-(op1+op2))
                del ayuda[l-1:l+3]
                ayuda.insert(l-1,resultadointermedio)
            else: 
                op1 = int(ayuda[l-1])
                op2 = int(ayuda[l+1])
                resultadointermedio = op1 - op2
                del ayuda[l-1:l+2]
                ayuda.insert(l-1, resultadointermedio)
        l += 1 
        
    
   # """
   # *def sumayresta(ayuda)
   # *ayuda es una lista
   # *
   # *Esta función revisa cada aparición del operador + y - e inserta el valor en la lista ayuda
   # """

            
def multiplicaciones(ayuda):
    l = 0
    n = 0
    while l < len(ayuda):
        index = ayuda[l]
        if index == "*":
            op1 = int(ayuda[l-1])
            if (ayuda[l+1]) != "":
                op2 = int(ayuda[l+1])
                resultadointermedio = op1 * op2
                del ayuda[l-1:l+2]
                ayuda.insert(l-1, resultadointermedio)
            else:
                op2 = int(ayuda[l+3])
                resultadointermedio = op1 * -op2
                del ayuda[l-1:l+3]
                ayuda.insert(l-1, resultadointermedio)
        else:
            l += 1

# """ 
#    def multiplicaciones(ayuda)
#    *ayuda: lista hecha con re.split 
#    *
#    *Esta función como en sumayresta, encuentra cada operador * y lo evalua para después insertar el valor en ayuda
# """

def divisiones(ayuda):
    l = 0
    while l < len(ayuda):
        index = ayuda[l]
        if index == "//":
            op1 = int(ayuda[l-1])
            op2 = int(ayuda[l+1])
            if ayuda[l+1] != "-":
                if op2 != 0:
                    resultadointermedio = op1 // op2
                    del ayuda[l-1:l+2]
                    ayuda.insert(l-1, resultadointermedio)
                else:
                    return "Error"
            else:
                op2 = int(ayuda[l+3])
                if op2 != 0:
                    resultadointermedio = op1 // -op2
                else:
                    "Error"
        else:
            l += 1
                   
#"""
#*def divisiones(ayuda)
#*ayuda: lista hecha con re.split 
#*
#*Esta función al igual que multiplicaciones, solo que con el operador // y verifica que
#*op2 no sea 0, para tirar error si es que lo es  
#""" 
       
def operacionesbasicas(match):
    partes = re.split(r"\s*([+\-*]|//)\s*", match)
    multiplicaciones(partes)
    divisiones(partes)
    sumayresta(partes)
    if partes[0] != "Error":
        return int(partes[0])
    else:
        return 0

#    """
#   *def operacionesbasicas(match)
#    *match es un string
#    *
#    *Esta función va por orden de prioridad usando las diferentes funciones descritas más arriba
#    *y retornando el valor si es que este no es Error
#    """

def cupon(match):
    partes = re.split(r"\(|\)|\,",match)
    if len(partes) == 4:
        x = int(partes[1])
        y = int(partes[2])
        if y < 100:
            b = int(x*100/y)
            return str(b)
    elif len(partes) == 3:
        x = int(partes[1])
        b = int(x*0.2)
        return str(b)
    return "Error"
             
#    """
#def cupon(match)
#    *un string
#    *
#    *Esta función separa el string match en una lista para su mejor uso
#    *y evalúa dependiendo del tamaño de la lista que se genera CUPON(x) o CUPON(x,y)   
#"""

def hacercupon(match):
    return str(cupon(match))

 #   """
 #   *def hacercupon(match)
 #   *match es un string
 #   *
 #   *es para hacer la función cupon
 #   """

def validarsintaxis(linea):
    return re.fullmatch(sentencia.pattern, linea) is not None

#    """
#    *def validarsintaxis(linea)
#    *linea es un string
#    *
#    *Verifica la sintaxis de la línea correspondiente
#    """

def evaluar_operacion(operacion2):
    coincidencias = re.findall(r"CUPON\s*\(\s*-?\d+\s*(?:,\s*-?\d+\s*)?\)", operacion2)
    for coincidencia in coincidencias:
        resultado_cupon = hacercupon(coincidencia)
        operacion2 = operacion2.replace(coincidencia, str(resultado_cupon), 1)
    
    operacion_con_ans = operacion2.replace("ANS", str(resultado_anterior))
    a = operacionesbasicas(operacion_con_ans)
    return a

#    """
#    *def evaluar_operacion(operacion2)
#    *operacion2 es un string 
#    *
#    *Esta función revisa primero si es que existe un cupon en la operacion2, para reemplazarlo con su resultado
#    *luego revisa si la palabra clave ANS existe en esta y la reemplaz con resultado_anterior
#    *para finalmente realizar las operaciones básicas
#    """
    
def buscarparentesis(sentencia2):
    index_open = sentencia2.rfind("(")
    if index_open == -1:
        return evaluar_operacion(sentencia2)
    
    index_close = sentencia2.find(")", index_open)
    if index_close == -1:
        return "Error"
    
    operaciona = sentencia2[index_open+1:index_close]
    if not re.search(r"[+\-*//]", operaciona):
        return "Error"
    
    a = validarsintaxis(operaciona)
    if a is True:
        resultado_operacion = evaluar_operacion(operaciona)
        sentencia2 = sentencia2[:index_open] + str(resultado_operacion) + sentencia2[index_close+1:]
        return buscarparentesis(sentencia2)
    elif a is False:
        return "Error"
    
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
            if resultado != "Error" and int(resultado) > 0:
                salida.write(f"{linea} = {resultado}\n")
                resultado_anterior = resultado
            elif resultado == "Error":
                salida.write(f"{linea} = Error\n")
            elif int(resultado) < 0:
                salida.write(f"{linea} = 0 \n")
                resultado_anterior = 0 
            else:
                salida.write(f"{linea} = Sin resolver\n")
                
#    """
#   *def leerlineas(entrada, salida)
#   *entrada = archivo de entrada
#    *salida = archivo de salida
#    *Esta función va leyendo linea por linea el archivo y pasandolas a validar sintaxis
#    *esto para verificar si la operacion se puede hacer o si no retornar "error" y escribirlo en el archivo
#    *Así en cada caso, hasta para el caso de que el resultado sea negativo, escribiendo en el archivo = 0
#    """
    
                      
resultado_anterior = 0         
archivo = open("problemas.txt","r")
salida = open("desarrollos.txt", "w")
leerlineas(archivo, salida)
archivo.close() 
salida.close()

