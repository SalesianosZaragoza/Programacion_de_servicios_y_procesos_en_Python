import threading
import random
"""
The purpose of this code is to demonstrate how thread-local storage 
can be used to store data that is specific to each thread. 
Each thread has its own "copy" of the almacen object, 
and can set and get its value independently of the other threads.
"""
def mostrar(almacen):
  try:
    val = almacen.valor
  except AttributeError:
    print(f"Secondary {threading.current_thread().name}: Aún no inicializado dato del almacen\n", end="")
  else:
   print(f"{threading.current_thread().name}: {val}\n", end="")

def hilo(almacen):
  #almacen = threading.local() #variable con instancia local en cada hilo
  mostrar(almacen)
  almacen.valor = random.randint(1, 100)
  mostrar(almacen)

almacen = threading.local() #storage local a cada hilo
#Thread-local data is data whose values are thread specific.

#Main thread
mostrar(almacen)
almacen.valor = 999
mostrar(almacen)

#Hilos
for i in range(3):
  t = threading.Thread(target=hilo, args=(almacen,))
  t.start()