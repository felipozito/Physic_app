import sympy as sp
import numpy as np
def Coulomb_angle(valores_conocidos):
    try:
        ans={}
        valores_numericos = {}
        for var_str, valor in valores_conocidos.items():
            valores_numericos[str(var_str)] = float(valor) 
        F1 = (9e9) * (valores_numericos['q1'] * valores_numericos['q2']) / (valores_numericos['r1']**2)
        F2 = (9e9) * (valores_numericos['q3'] * valores_numericos['q2']) / (valores_numericos['r2']**2)
        F2x = F2 * np.cos(valores_numericos['theta']*(np.pi)/180,)
        F2y = F2 * np.sin(valores_numericos['theta']*(np.pi)/180,)
        Ft = ((F1 + F2x)**2 + F2y**2)**(1/2)
    
                # Prepare steps for display
        steps = []
        steps.append(f"Paso 1 - F1: {F1:.2e} N")
        steps.append(f"Paso 2 - F2: {F2:.2e} N")
        steps.append(f"Paso 3 - F2x: {F2x:.2e} N")
        steps.append(f"Paso 4 - F2y: {F2y:.2e} N")
        steps.append(f"Paso 5 - Ft: {Ft:.2e} N")
        
        ans["steps"]=steps
        ans["valor_resuelto"]=Ft
        return ans
    except Exception as e:
                return f"Error en el cálculo: {str(e)}"         
