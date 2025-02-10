import sympy as sp
import ast
import re
import os

formulas = {
    "MRU": {
        "instrucciones": "Movimiento Rectilíneo Uniforme: Útil para calcular velocidad constante, distancia o tiempo.",
        "formulas": ["v=d/t"]
    },
    "MRUV": {
        "instrucciones": "Movimiento Rectilíneo Uniformemente Variado: Para movimientos con aceleración constante.",
        "formulas": [
            "vf=vo+a*t",
            "d=vo*t+(1/2)*a*t^2",
            "vf^2=vo^2+2*a*d",
            "d=(vo+vf)/2*t"
        ]
    },
    "CAIDA LIBRE": {
        "instrucciones": "Caída Libre: Movimiento vertical bajo la acción de la gravedad (g=9.81 m/s²).",
        "formulas": [
            "vf=vo+9.81*t",
            "h=vo*t+1/2*9.81*t^2",
            "vf^2=vo^2+2*9.81*h"
        ]
    },
    "LANZAMIENTO VERTICAL": {
        "instrucciones": "Lanzamiento Vertical: Movimiento vertical hacia arriba contra la gravedad.",
        "formulas": [
            "vf=vo-9.81*t",
            "h=vo*t-1/2*9.81*t^2",
            "vf^2=vo^2-2*9.81*h"
        ]
    },
    "MCU": {
        "instrucciones": "Movimiento Circular Uniforme: Para objetos que se mueven en círculo a velocidad constante.",
        "formulas": [
            "v=l/t",
            "w=theta/t"
        ]
    },
    "MCUV": {
        "instrucciones": "Movimiento Circular Uniformemente Variado: Para movimientos circulares con aceleración constante.",
        "formulas": [
            "vf=vo+a*t",
            "l=vo*t+(1/2)*a*t^2",
            "vf^2=vo^2+2*a*l",
            "wf=wo+at*t",
            "theta=wo*t+(1/2)*at*t^2",
            "wf^2=wo^2+2*at*theta"
        ]
    },
    "LEY_DE_COULOMB": {
        "instrucciones": "Ley de Coulomb: Calcula la fuerza electrostática entre dos cargas puntuales.",
        "formulas": [
            "F=(9*10^9)*(q1*q2)/r^2"
        ]
    },
    "LEY_DE_COULOMB 2 CARGAS LINEA RECTA": {
        "instrucciones": "Ley de Coulomb para dos cargas en línea recta: Suma de fuerzas electrostáticas. RECORDAR  LA CARGA EN COMUN ES Q2",
        "formulas": [
            "Ft=((9*10^9)*(q1*q2)/r1^2) +((9*10^9)*(q2*q3)/r2^2)"
        ]
    },
    "LEY DE COULOMB ANGULO": {
        "instrucciones": "Ley de Coulomb con ángulo: Calcula la fuerza resultante considerando componentes vectoriales.",
        "variables": ["Ft","q1", "q2", "q3", "r1", "r2", "theta"],
        "steps": [
            {
                "name": "Calcular F1",
                "formula": "F1=(9*10^9)*(q1*q2)/r1^2"
            },
            {
                "name": "Calcular F2",
                "formula": "F2=(9*10^9)*(q3*q2)/r2^2"
            },
            {
                "name": "Calcular componente x de F2",
                "formula": "F2x=F2*sin(theta)"
            },
            {
                "name": "Calcular componente y de F2",
                "formula": "F2y=F2*cos(theta)"
            },
            {
                "name": "Calcular Fuerza Total",
                "formula": "Ft=((F1+F2x)^2+(F2y)^2)^(1/2)"
            }
        ]
    },
    
    "ENERGIA": {
        "instrucciones": "Energía: Calcula diferentes tipos de energía (potencial, cinética, elástica).",
        "formulas": [
            "ep=m*9.81*h",
            "ec=1/2*m*v^2",
            "ek=1/2*k*x^2"
        ]
    },
    "TRABAJO": {
        "instrucciones": "Trabajo: Calcula el trabajo realizado por una fuerza constante.",
        "formulas": [
            "W=F*d"
        ]
    },
    "POTENCIA": {
        "instrucciones": "Potencia: Calcula la rapidez con que se realiza un trabajo.",
        "formulas": [
            "P=W/t"
        ]
    },
    "LEY DE OHM": {
        "instrucciones": "Ley de Ohm: Relaciona voltaje (V), corriente (I) y resistencia (R). P es la potencia.",
        "formulas": [
            "P=V^2/R",
            "P=I_^2*R",
            "P=V*I_",
            "I_=V/R"
        ]
    }
}

def convert_formulas_to_sympy(formulas_dict):
    temas_simbolica = {}
    instrucciones = {}
    variables = {}
    for tema, data in formulas_dict.items():
        temas_simbolica[tema] = []
        instrucciones[tema] = data["instrucciones"]
        if 'variables' in data:
            variables[tema] = data["variables"]  
        else:
            variables[tema] = None 
        if "steps" in data:
            # Obtener pasos a simbologia
            for step in data["steps"]:
                formula = step["formula"] 
                left, right = formula.split('=')#Separamos la ecuacion donde este igual (variable, formula)
                left_expr = sp.sympify(left) #Creo la expresion (variable)
                right_expr = sp.sympify(right) #Creo la expresion (formula)
                eq = sp.Eq(left_expr, right_expr) #Creo la ecuacion (variable, formula)
                temas_simbolica[tema].append({
                    'equation': eq,
                    'latex': sp.latex(eq),
                    'step_name': step["name"]
                })
        else:
            # Obtener formulas a simbologia
            for formula in data["formulas"]:
                left, right = formula.split('=')#Separamos la ecuacion donde este igual (variable, formula)
                left_expr = sp.sympify(left) #Creo la expresion (variable)
                right_expr = sp.sympify(right)#Creo la expresion (formula)
                eq = sp.Eq(left_expr, right_expr) #Creo la ecuacion (variable, formula)
                temas_simbolica[tema].append({
                    'equation': eq,
                    'latex': sp.latex(eq),
                    'step_name': None
                })

    return temas_simbolica, instrucciones, variables

# Convert formulas directly without reading the file
temas_simbolica, instrucciones_formulas, variables = convert_formulas_to_sympy(formulas)

if temas_simbolica:
    #print(temas_simbolica)
    #print(instrucciones_formulas)
    #print(variables)
    for tema, data in temas_simbolica.items():
        ##print(f"\n{tema}:")
        pass
        for formula in data:
           ##print(f"  {formula}")
           pass
else:
    print("Error en la conversión de fórmulas")