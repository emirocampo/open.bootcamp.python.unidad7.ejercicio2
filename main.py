from tiempo.faltante import diaActual
from tiempo.faltante import horaFaltante


def main():
    dia = diaActual()
    print("HOY ES: %d %d %d"%(dia[0],dia[1],dia[2]))
    horas, minutos, segundos = horaFaltante()
    if(horas < 0 and minutos < 0 and segundos < 0):
        print("ya debiste haber salido")
    else:
        print("PARA SALIR A CASA FALTAN: %d horas %d minutos %d segundos"%(horas, minutos, segundos))
    


if(__name__ == "__main__"): 
    main()