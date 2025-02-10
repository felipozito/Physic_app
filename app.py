from flask import Flask, render_template, request
import sympy as sp
from physics_utils import convertir_a_si, validar_unidad
from unit_conversions import conversiones_unidades
from variables import restricciones_unidades
from formulas import temas_simbolica, instrucciones_formulas, variables as var
from utils import Coulomb_angle
app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html', temas=temas_simbolica.keys())

@app.route('/form', methods=['POST'])
def formulario():
    try:
        tema_seleccionado = request.form['tema'] # Obtengo el tema seleccionada
        if tema_seleccionado == "LEY DE COULOMB ANGULO":
            variables=var[tema_seleccionado]  
        else:
            variables = {str(var) for tema in temas_simbolica[tema_seleccionado] 
                    for var in tema['equation'].free_symbols}
        return render_template(
            'form.html',
            tema_seleccionado=tema_seleccionado,
            instrucciones_formulas=instrucciones_formulas[tema_seleccionado],
            variables=variables,
            restricciones_unidades=restricciones_unidades
        )
    except KeyError:
        return "Error: Fórmula seleccionada inválida.", 400

@app.route('/calculate', methods=['POST'])
def calcular():
    try:
        ## Llamamos los datos del formulario
        tema_seleccionado = request.form['tema_seleccionado'] #Obtengo el tema seleccionado
        variable = request.form['variable']#Obtengo la variable seleccionada
        formulas_tema = temas_simbolica[tema_seleccionado] #Obtengo las fórmulas del tema seleccionado
        simbolo_objetivo = sp.Symbol(variable) #Crear simbolo de la variable en busqueda
        valores_conocidos = {} # Recolectar y validar valores conocidos
        for formula_data in formulas_tema:
            formula = formula_data['equation'] #Obtengo la formula
            for var in formula.free_symbols: #Obtengo los simbolos de la formula
                var_str = str(var) #Convertimos el simbolo a string
                if var_str != variable: #Comprobamos si el simbolo es el objetivo
                    valor = request.form.get(f"value_{var_str}") #Obtengo el valor de la variable
                    unidad = request.form.get(f"unit_{var_str}") #Obtengo la unidad de la variable
                    if not all([valor, unidad]): #Compruebo valores nulos
                        continue
                    try:
                        valores_conocidos[var] = convertir_a_si(valor, unidad)
                    except ValueError:
                        return f"Error: Valor inválido para {var_str}.", 400
                    
        if(tema_seleccionado == "LEY DE COULOMB ANGULO"):
            ans=Coulomb_angle(valores_conocidos)
            print(ans)
            return render_template(
                            'result.html',
                            formula_name=tema_seleccionado,
                            formula=sp.latex(formula),
                            unknown_var=variable,
                            solved_value=ans["valor_resuelto"],
                            steps=ans["steps"]
                        )
        ## Reemplazo los valores en la formula
        for formula_data in formulas_tema: 
            formula = formula_data['equation']
            if simbolo_objetivo in formula.free_symbols: 
                variables_desconocidas = [var for var in formula.free_symbols if var not in valores_conocidos]
                if len(variables_desconocidas) == 1 and variables_desconocidas[0] == simbolo_objetivo:
                    try:
                        eq_with_values = formula.subs(valores_conocidos)# Sustituyo los valor 
                        steps = []    # Agregos los pasos
                        steps.append(f"Datos: {str(valores_conocidos)}") #Datos del problema
                        steps.append(f"EcuacionOriginal: {sp.latex(formula)}")#Formula a utilizar
                        steps.append(f"SubstituyendoValores: {sp.latex(eq_with_values)}")#Formula sustituida
                        solution = sp.solve(eq_with_values, variable)[0]#Solucion
                        steps.append(f"Solucion: {variable} = {sp.latex(solution)}")
                        valor_resuelto = float(solution) #Convertimos a float

                        return render_template(
                            'result.html',
                            formula_name=tema_seleccionado,
                            formula=sp.latex(formula),
                            unknown_var=variable,
                            solved_value=valor_resuelto,
                            steps=steps
                        )
                    except (sp.SolveError, ValueError) as e:
                        return f"Error: No se pudo resolver la ecuación. {str(e)}", 400
        return "Error: Información insuficiente para resolver la variable seleccionada.", 400
    except Exception as e:
        return f"Error: Ocurrió un error inesperado: {str(e)}.", 500

if __name__ == '__main__':
    app.run(debug=True)