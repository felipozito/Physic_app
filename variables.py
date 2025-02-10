import sympy as sp

# Variables simbólicas comunes
def crear_simbolos():
    return {
        't': sp.Symbol('t'),     # tiempo
        'a': sp.Symbol('a'),     # aceleración
        'd': sp.Symbol('d'),     # distancia
        'vo': sp.Symbol('vi'),   # velocidad inicial
        'vf': sp.Symbol('vf'),   # velocidad final
        'v': sp.Symbol('v'),     # velocidad
        'l': sp.Symbol('l'),     # longitud de arco
        'g': sp.Symbol('g'),     # gravedad
        'm': sp.Symbol('m'),     # masa
        'F': sp.Symbol('F'),     # fuerza
        'Ft': sp.Symbol('Ft'),   # fuerza total
        'F1':sp.Symbol('F1'),  # fuerza F1 total
        'F2':sp.Symbol('F2'),  # fuerza F2 total
        'F2x':sp.Symbol('F2x'),    # fuerza 2x total
        'F2y':sp.Symbol('F2y'),    # fuerza 2y total
        'wo': sp.Symbol('wo'),   # velocidad angular inicial
        'wf': sp.Symbol('wf'),   # velocidad angular final
        'at': sp.Symbol('at'),   # aceleración angular
        'r': sp.Symbol('r'),     # distancia entre cargas
        'r1': sp.Symbol('r1'),   # distancia entre cargas 1
        'r2': sp.Symbol('r2'),   # distancia entre cargas 2
        'r3': sp.Symbol('r3'),   # distancia entre cargas 3
        'q1': sp.Symbol('q1'),   # carga 1
        'q2': sp.Symbol('q2'),   # carga 2
        'q3': sp.Symbol('q3'),   # carga 3
        'w': sp.Symbol('w'),     # velocidad angular
        'theta': sp.Symbol('theta'), # ángulo
        'vo': sp.Symbol('vo'),   # velocidad inicial
        'h': sp.Symbol('h'),     # altura
        'k': sp.Symbol('k'),     # constante elástica
        'x': sp.Symbol('x'),     # posición
        'ep': sp.Symbol('ep'),   # energía potencial
        'ec': sp.Symbol('ec'),   # energía cinética
        'ek': sp.Symbol('ek'),    # energía elástica
        'W': sp.Symbol('W'),     # trabajo
        'V': sp.Symbol('V'),     # voltaje
        'I_': sp.Symbol('I'),     # corriente
        'P': sp.Symbol('P'),     # potencia
        'R': sp.Symbol('R'),     # resistencia
        
    }

# Restricciones de unidades por tipo de variable
restricciones_unidades = {
    'd': ['m', 'km', 'dm'],          # distancia en km o m
    't': ['s', 'min', 'hrs'],          # tiempo en min, s o h
    'v': ['m/s', 'km/h'],            # velocidad en m/s o km/h
    'vf': ['m/s', 'km/h'],           # velocidad final en m/s o km/h
    'vo': ['m/s', 'km/h'],           # velocidad inicial en m/s o km/h
    'm': ['kg', 'g'],                # masa en kg o g
    'a': ['m/s²'],                   # aceleración en m/s²
    'F': ['N'],                      # fuerza en Newtons
    'Ft': ['N'],                      # fuerza total en Newtons
    'F1': ['N'],                      # fuerza F1 total en Newtons
    'F2': ['N'],                      # fuerza F2 total en Newtons
    'F2x': ['N'],                      # fuerza 2x total en Newtons
    'F2y': ['N'],                      # fuerza 2y total en Newtons
    'q1': ['uC', 'nC', 'pC'],        # carga en Coulombs
    'q2': ['uC', 'nC', 'pC'],        # carga en Coulombs
    'q3': ['uC', 'nC', 'pC'],        # carga en Coulombs
    'x': ['cm', 'm'],                # distancia en metros
    'k': ['Nm'],                     # constante elástica
    'r': ['m','cm'] ,                # distancia en metros
    'r1':['m','cm'],                 # distancia entre cargas en metros
    'r2':['m','cm'],                 # distancia entre cargas en metros
    'r3':['m','cm'],                 # distancia entre cargas en metros
    'h':['m','km'],                 # altura en metros o kilómetros
    'ep':['J'],                     # energía potencial
    'ec':['J'],                     # energía cinética
    'ek':['J'],                     # energía elástica
    'theta':['deg','rad',],                # ángulo
    'at':['rad/s²'],                # aceleración tangencial
    'l':['m','cm'],                 # longitud de arco en metros o centímetros
    'w':['rad/s'],                  # velocidad angular
    'at':['rad/s²'],                # aceleración tangencial
    'wo':['rad/s'],                 # velocidad angular inicial
    'wf':['rad/s'],                 # velocidad angular final
    'W':['J'],                     # trabajo
    'V':['V','mV'],                      # voltaje
    'I_':['A','mA'],                      # corriente
    'P':['Watts'],                      # potencia
    'R':['Ohm','MOhm','KOhm'],                    # resistencia
    
}