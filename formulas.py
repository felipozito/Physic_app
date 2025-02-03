import sympy as sp
import ast
import re
import os
 
formulas={
    "MRU": [
        "v=d/t"
    ],
    "MRUV": [
        "vf=vo+a*t",
        "d=vo*t+(1/2)*a*t^2",
        "vf^2=vo^2+2*a*d",
        "d=(vo+vf)/2*t",
    ],
    "CAIDA LIBRE":[ 
        "vf=vo+9.81*t",
        "h=vo*t+1/2*9.81*t^2",
        "vf^2=vo^2+2*9.81*h"
    ],
    "LANZAMIENTO VERTICAL":[
        "vf=vo-9.81*t",
        "h=vo*t-1/2*9.81*t^2",
        "vf^2=vo^2-2*9.81*h"
    ],
    "MCU": [
        "v=l/t",
        "w=theta/t",
    ],
    "MCUV": [
        "vf=vo+a*t",
        "l=vo*t+(1/2)*a*t^2",
        "vf^2=vo^2+2*a*l",
        "wf=wo+at*t",
        "theta=wo*t+(1/2)*at*t^2",
        "wf^2=wo^2+2*at*theta",
    ],
    "LEY_DE_COULOMB": [
        "F=(9*10^9)*(q1*q2)/r^2"
    ],
    "LEY_DE_COULOMB 2 CARGAS LINEA RECTA": [
        "Ft=((9*10^9)*(q1*q2)/r1^2) +((9*10^9)*(q2*q3)/r2^2)",
    ],
    "ENERGIA": [
        "ep=m*9.81*h",
        "ec=1/2*m*v^2",
        "ek=1/2*k*x^2",
    ],  
    "TRABAJO":[
        "W=F*d",
    ],
    "POTENCIA": [ 
        "P=W/t",
    ],
    "LEY DE OHM":[
        "I=V/R",
        "P=V^2/R",
        "P=(I^2)*R",
    ]
    
        
}

def convert_formulas_to_sympy(formulas_dict):
    symbolic_formulas = {}
    for category, formula_list in formulas_dict.items():
        symbolic_formulas[category] = []
        for formula in formula_list:
            left, right = formula.split('=')
            left_expr = sp.sympify(left)
            right_expr = sp.sympify(right)
            symbolic_formulas[category].append(sp.Eq(left_expr, right_expr))
                
    return symbolic_formulas

# Convert formulas directly without reading the file
symbolic_formulas = convert_formulas_to_sympy(formulas)

if symbolic_formulas:
    print("Fórmulas convertidas exitosamente:")
    for category, formula_list in symbolic_formulas.items():
        print(f"\n{category}:")
        for formula in formula_list:
            print(f"  {formula}")
else:
    print("Error en la conversión de fórmulas")