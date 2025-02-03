from flask import Flask, render_template, request
import sympy as sp
from physics_utils import obtener_formulas_movimiento, convertir_a_si, validar_unidad
from unit_conversions import conversiones_unidades
from variables import crear_simbolos, restricciones_unidades

app = Flask(__name__)

# Inicializar símbolos y fórmulas físicas
simbolos = crear_simbolos()
formulas = obtener_formulas_movimiento(simbolos)

@app.route('/')
def inicio():
    return render_template('index.html', formulas=formulas.keys())

@app.route('/form', methods=['POST'])
def formulario():
    try:
        nombre_formula = request.form['formula']
        variables = {str(var) for formula in formulas[nombre_formula] for var in formula.free_symbols}
        return render_template(
            'form.html',
            formula_name=nombre_formula,
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
        formulas_seleccionadas = formulas[nombre_formula]
        simbolo_objetivo = sp.Symbol(variable_objetivo)

        # Recolectar y validar valores conocidos
        valores_conocidos = {}
        for formula in formulas_seleccionadas:
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
        for formula in formulas_seleccionadas:
            if simbolo_objetivo in formula.free_symbols:
                variables_desconocidas = [var for var in formula.free_symbols if var not in valores_conocidos]
                if len(variables_desconocidas) == 1 and variables_desconocidas[0] == simbolo_objetivo:
                    try:
                        valor_resuelto = sp.solve(formula.subs(valores_conocidos), simbolo_objetivo)[0]
                        return render_template(
                            'result.html',
                            formula_name=nombre_formula,
                            formula=str(formula),
                            unknown_var=variable_objetivo,
                            solved_value=float(valor_resuelto)
                        )
                    except (sp.SolveError, ValueError):
                        return "Error: No se pudo resolver la ecuación.", 400

        return "Error: Información insuficiente para resolver la variable seleccionada.", 400

    except KeyError as e:
        return f"Error: Campo requerido faltante {str(e)}.", 400
    except Exception as e:
        return f"Error: Ocurrió un error inesperado: {str(e)}.", 500

if __name__ == '__main__':
    app.run(debug=True)