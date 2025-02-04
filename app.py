from flask import Flask, render_template, request
import sympy as sp
from physics_utils import convertir_a_si, validar_unidad
from unit_conversions import conversiones_unidades
from variables import restricciones_unidades
from formulas import symbolic_formulas, formula_instructions

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html', formulas=symbolic_formulas.keys())

@app.route('/form', methods=['POST'])
def formulario():
    try:
        nombre_formula = request.form['formula']
        # Fix: Access the equation from the formula dictionary
        variables = {str(var) for formula in symbolic_formulas[nombre_formula] 
                    for var in formula['equation'].free_symbols}
        return render_template(
            'form.html',
            formula_name=nombre_formula,
            formula_instruction=formula_instructions[nombre_formula],
            variables=variables,
            units=conversiones_unidades.keys(),
            unit_restrictions=restricciones_unidades
        )
    except KeyError:
        return "Error: Fórmula seleccionada inválida.", 400

@app.route('/calculate', methods=['POST'])
def calcular():
    try:
        nombre_formula = request.form['formula_name']
        variable_objetivo = request.form['target_var']
        formulas_seleccionadas = symbolic_formulas[nombre_formula]
        simbolo_objetivo = sp.Symbol(variable_objetivo)

        # Recolectar y validar valores conocidos
        valores_conocidos = {}
        for formula_data in formulas_seleccionadas:
            formula = formula_data['equation']  # Fix: Access the equation
            for var in formula.free_symbols:
                var_str = str(var)
                if var_str != variable_objetivo:
                    valor = request.form.get(f"value_{var_str}")
                    unidad = request.form.get(f"unit_{var_str}")
                    if not all([valor, unidad]):
                        continue
                    if not validar_unidad(var_str, unidad):
                        return f"Error: Unidad inválida {unidad} para {var_str}.", 400
                    try:
                        valores_conocidos[var] = convertir_a_si(valor, unidad)
                    except ValueError:
                        return f"Error: Valor inválido para {var_str}.", 400

        # Encontrar fórmula adecuada y resolver
        for formula_data in formulas_seleccionadas:
            formula = formula_data['equation']
            if simbolo_objetivo in formula.free_symbols:
                variables_desconocidas = [var for var in formula.free_symbols if var not in valores_conocidos]
                if len(variables_desconocidas) == 1 and variables_desconocidas[0] == simbolo_objetivo:
                    try:
                        # Get the equation with substituted values
                        eq_with_values = formula.subs(valores_conocidos)
                        
                        # Solve and get steps
                        steps = []
                        steps.append(f"Original equation: {sp.latex(formula)}")
                        steps.append(f"Substituting values: {sp.latex(eq_with_values)}")
                        
                        # Solve the equation
                        solution = sp.solve(eq_with_values, simbolo_objetivo)[0]
                        steps.append(f"Solution: {variable_objetivo} = {sp.latex(solution)}")
                        
                        # Calculate numerical result
                        valor_resuelto = float(solution)
                        steps.append(f"Numerical result: {valor_resuelto}")

                        return render_template(
                            'result.html',
                            formula_name=nombre_formula,
                            formula=sp.latex(formula),
                            unknown_var=variable_objetivo,
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