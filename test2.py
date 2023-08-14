import re

# Definir expresiones regulares
digito = re.compile("[1-9]")  # Dígito del 1 al 9
digito_o_zero = re.compile("(?:[1-9]|0)")  # Dígito o el número 0
para_entero = re.compile("(?:[1-9][0-9]*)|(?:0)")  # Dígitos o cero repetidos (para formar enteros)
entero = re.compile("(?:para_entero|0)")  # Entero o 0
espacio = re.compile(r"\s*")  # Espacios en blanco (usamos \s para espacios, tabulaciones, saltos de línea, etc.)
operador = re.compile(r"(?:espacio*([+\-*/])espacio*)")  # Operadores (+, -, *, /) con espacios opcionales alrededor
operacion = re.compile(r"(?:(?:clave|entero)(?:operador(?:entero|clave))*)")  # Operaciones con paréntesis

# Expresión matemática
expresion = "3000 * (5 - 23) // 5"

# Buscar operaciones en la expresión
resultado = operacion.findall(expresion)  # Encontrar todas las operaciones

# Función para evaluar la operación contenida en una cadena
def evaluar_operacion(cadena):
    return eval(cadena.replace("ANS", "result_anterior"))  # Evaluar con "ANS" reemplazado por el resultado anterior

# Evaluar cada operación encontrada en la expresión
result_anterior = None
for oper in resultado:
    resultado_actual = evaluar_operacion(oper)
    print("Resultado de", oper, ":", resultado_actual)
    result_anterior = resultado_actual  # Actualizar el resultado anterior