import sympy as sp
import ast
import re
import os

formulas = {
    "MRU": {
        "instructions": "Movimiento Rectilíneo Uniforme: Útil para calcular velocidad constante, distancia o tiempo.",
        "formulas": ["v=d/t"]
    },
    "MRUV": {
        "instructions": "Movimiento Rectilíneo Uniformemente Variado: Para movimientos con aceleración constante.",
        "formulas": [
            "vf=vo+a*t",
            "d=vo*t+(1/2)*a*t^2",
            "vf^2=vo^2+2*a*d",
            "d=(vo+vf)/2*t"
        ]
    },
    "CAIDA LIBRE": {
        "instructions": "Caída Libre: Movimiento vertical bajo la acción de la gravedad (g=9.81 m/s²).",
        "formulas": [
            "vf=vo+9.81*t",
            "h=vo*t+1/2*9.81*t^2",
            "vf^2=vo^2+2*9.81*h"
        ]
    },
    "LANZAMIENTO VERTICAL": {
        "instructions": "Lanzamiento Vertical: Movimiento vertical hacia arriba contra la gravedad.",
        "formulas": [
            "vf=vo-9.81*t",
            "h=vo*t-1/2*9.81*t^2",
            "vf^2=vo^2-2*9.81*h"
        ]
    },
    "MCU": {
        "instructions": "Movimiento Circular Uniforme: Para objetos que se mueven en círculo a velocidad constante.",
        "formulas": [
            "v=l/t",
            "w=theta/t"
        ]
    },
    "MCUV": {
        "instructions": "Movimiento Circular Uniformemente Variado: Para movimientos circulares con aceleración constante.",
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
        "instructions": "Ley de Coulomb: Calcula la fuerza electrostática entre dos cargas puntuales.",
        "formulas": [
            "F=(9*10^9)*(q1*q2)/r^2"
        ]
    },
    "LEY_DE_COULOMB 2 CARGAS LINEA RECTA": {
        "instructions": "Ley de Coulomb para dos cargas en línea recta: Suma de fuerzas electrostáticas. RECORDAR  LA CARGA EN COMUN ES Q2",
        "formulas": [
            "Ft=((9*10^9)*(q1*q2)/r1^2) +((9*10^9)*(q2*q3)/r2^2)"
        ]
    },
    "LEY_DE_COULLOMB ANGULO": {
        "instructions": "Ley de Coulomb con ángulo: Calcula la fuerza resultante considerando componentes vectoriales.",
        "formulas": [
            'F1=(9*10^9)*(q1*q2)/r1^2',
            'F2=(9*10^9)*(q3*q2)/r2^2',
            'F2x=F2sin(theta)',
            'F2y=F2cos(theta)',
            'Ft=((F1+F2x)^2+(F2y)^2)^-2'
        ]
    },
    "ENERGIA": {
        "instructions": "Energía: Calcula diferentes tipos de energía (potencial, cinética, elástica).",
        "formulas": [
            "ep=m*9.81*h",
            "ec=1/2*m*v^2",
            "ek=1/2*k*x^2"
        ]
    },
    "TRABAJO": {
        "instructions": "Trabajo: Calcula el trabajo realizado por una fuerza constante.",
        "formulas": [
            "W=F*d"
        ]
    },
    "POTENCIA": {
        "instructions": "Potencia: Calcula la rapidez con que se realiza un trabajo.",
        "formulas": [
            "P=W/t"
        ]
    },
    "LEY DE OHM": {
        "instructions": "Ley de Ohm: Relaciona voltaje (V), corriente (I) y resistencia (R). P es la potencia.",
        "formulas": [
            "P=V^2/R",
            "P=I_^2*R",
            "P=V*I_",
            "I_=V/R"
        ]
    }
}

def convert_formulas_to_sympy(formulas_dict):
    symbolic_formulas = {}
    instructions = {}
    
    for category, data in formulas_dict.items():
        symbolic_formulas[category] = []
        instructions[category] = data["instructions"]
        print(data)
        
        for formula in data["formulas"]:
            left, right = formula.split('=')
            left_expr = sp.sympify(left)
            right_expr = sp.sympify(right)
            eq = sp.Eq(left_expr, right_expr)
            symbolic_formulas[category].append({
                'equation': eq,
                'latex': sp.latex(eq),
                'steps': []  # Will store solution steps
            })
    
    return symbolic_formulas, instructions

# Convert formulas directly without reading the file
symbolic_formulas, formula_instructions = convert_formulas_to_sympy(formulas)

if symbolic_formulas:
    print("Fórmulas convertidas exitosamente:")
    for category, formula_list in symbolic_formulas.items():
        #print(f"\n{category}:")
        pass
        for formula in formula_list:
         #   print(f"  {formula}")
         pass
else:
    print("Error en la conversión de fórmulas")