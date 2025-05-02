#import brenchmarking as bm
import time
from brenchmarking import Brenchmarking
from metodos_ordenamientos import metodos_ordenamiento

if __name__ == "__main__":
    print("Funciona")
    bench = bm.brenchmarking()
    metodosO = metodos_ordenamiento()
    tamanios = [5000, 10000, 20000]
    resultados= []
    for tam tamanios:
        arreglo_base = bench.build_arreglo(tam)

    metodos_dic={
        "Burbuja": metodosO.metodo_sort_bubble,
        "Burbuja_mejorado": metodosO.metodo_sort_bubble_mejorado
        "Seleccion": metodosO.metodo_sort_seleccion
        "Inserccion": metodosO.metodo_sort_insercion
    }

    resultados = []
    for nombre, fun_metodo in metodos_dic.items():
        tiempo_resultado = bench.medir_tiempo(fun_metodo, arreglo_base)
        tupla_resultado = (tam, nombre, tiempo_resultado)
        resultados.append(tupla_resultado)

    for tam, nombre, tiempo in resultados:
        print(f"Tamaño:  {tam},nombre tetodo: {nombre}, tiempo: {tiempo: 6f} segundos")
    #bm.Brenchmarking
    #Brenchmarking()
    
    #arreglo = builarreglo(1000)