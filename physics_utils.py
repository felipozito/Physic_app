import sympy as sp
from unit_conversions import conversiones_unidades
from variables import restricciones_unidades
from formulas import convert_formulas_to_sympy, formulas

def obtener_formulas_movimiento(simbolos):
    # Convert the formulas from formulas.py
    return convert_formulas_to_sympy(formulas)
    
def convertir_a_si(valor, unidad):
    try:
        valor_numerico = float(valor)
        factor = conversiones_unidades.get(unidad, 1)
        return valor_numerico * factor
    except ValueError:
        raise ValueError(f"El valor {valor} no es un número válido")

def validar_unidad(variable, unidad):
    if variable not in restricciones_unidades:
        return True
    return unidad in restricciones_unidades[variable]