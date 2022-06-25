import time

def obtenerHora():
    """
    devuelve una tupla con la hora local
    """
    r = time.localtime()
    return r

def diaActual():
    """
    devuelve una tupla en formado %dd%mm%yyyy
    """
    tupla = obtenerHora()
    dia = (tupla[2],tupla[1],tupla[0])
    return dia

def horaFaltante():
    """
    devuelve el tiempo faltante para salir del trabajo
    """
    tupla = obtenerHora()
    horas = tupla[3]
    minutos = tupla[4]
    segundos = tupla[5]
    horas_f = 17 - horas
    minutos_f = 59 - minutos
    segundos_f = 59 - segundos
    return horas_f, minutos_f, segundos_f

