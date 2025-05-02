from metodos_ordenamiento import metodos_ordenamiento as mb
import random
import time

class Brenchmarking:
    
    def__init__(sefl):
        print("Bemchmarking instanciado")
    

    def __init__(self):
        print("Brenchmarking")
        mb.metodos_ordenamiento()
        
        arreglo = self.builarreglo(1000)
        
        tarea = lambda: mb.metodos_ordenamiento()
        #tarea = () ->
        tarea=lambda: self.mb.metodo_sort_bubble(arreglo)
        tiempoM= self.contar_con_current_time_milles(tarea)
        tiempoN= self.contar_con_current_time_nano(tarea)
        
        print("Timepo en milisegundo", (tiempoM))
        print("Tiempo en nanosegundos", (tiempoN))
        
    
    def buil_arreglo(self, tamano):
        arreglo = []
        for i in range(tamano):
            numero = random.randint(0 , 9999)
            arreglo.append(numero)
        return arreglo
    def buil_arreglo(self, tamano):
        arreglo=[tamano]
    def contar_con_current_time_milles(self, tarea):
        inicio= time.time()
        tarea()
        fin = time.time()
        return(fin - inicio)
    def contar_con_current_time_nano(self, tarea):
        inicio = time.time_ns
        tarea()
        fin = time.time_ns
        return (fin - inicio)/1000000000