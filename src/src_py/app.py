from benchmarking import Benchmarking
from metodos_ordenamiento import MetodosOrdenamiento
import matplotlib.pyplot as plt
import time

if __name__ == "__main__":
    print("funciona")

    bench = Benchmarking()
    metodosO = MetodosOrdenamiento()

    tamanios = [5000, 10000, 15000]
    resultados = []

    for tam in tamanios:
        arreglo_base = bench.build_arreglo(tam)

        metodos_dic = {
            "burbuja": metodosO.metodo_sort_bubble,
            "burbuja mejorado": metodosO.metodo_sort_bubble_mejorado,
            "seleccion": metodosO.metodo_sort_seleccion,
            "insercion": metodosO.metodo_sort_insercion,
        }

        for nombre, metodo in metodos_dic.items():
            time_resultado = bench.medir_tiempo(metodo, arreglo_base)
            tupla_resultado = (tam, nombre, time_resultado)
            resultados.append(tupla_resultado)

    for tam, nombre, tiempo in resultados:
        print(f"Tamaño: {tam}, nombre método: {nombre}, tiempo: {tiempo:.6f} segundos")

    # Diccionario para guardar tiempos por método
    tiempos_by_metodo = {
        "burbuja": [],
        "burbuja_mejorado": [],
        "seleccion": [],
        "insercion": [],
    }

    # Llenar los tiempos por método correctamente
    for tam, nombre, tiempo in resultados:
        if nombre == "burbuja":
            tiempos_by_metodo["burbuja"].append(tiempo)
        elif nombre == "burbuja mejorado":
            tiempos_by_metodo["burbuja_mejorado"].append(tiempo)
        elif nombre == "seleccion":
            tiempos_by_metodo["seleccion"].append(tiempo)
        elif nombre == "insercion":
            tiempos_by_metodo["insercion"].append(tiempo)

    # Graficar los resultados
    plt.figure(figsize=(10, 6))

    for nombre, tiempos in tiempos_by_metodo.items():
        plt.plot(tamanios, tiempos, label=nombre, marker="o")

    plt.title("Comparación de tiempo para cada método de ordenamiento")
    plt.xlabel("Tamaño de los arreglos")
    plt.ylabel("Tiempo de ejecución (s)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

