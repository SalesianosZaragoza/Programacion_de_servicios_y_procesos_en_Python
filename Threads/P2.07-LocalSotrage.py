import threading
import random
"""
The purpose of this code is to demonstrate how thread-local storage 
can be used to store data that is specific to each thread. 
Each thread has its own "copy" of the almacen object, 
and can set and get its value independently of the other threads.
"""
hola = "hola"
def mostrar(almacen):
  try:
    llaves = almacen.llaves
  except AttributeError:
    print(f"Secondary {threading.current_thread().name}: Aún no tiene las llaves dato del almacen\n", end="")
  else:
   print(f"{threading.current_thread().name}: {llaves}\n", end="")

def hilo(almacen):
  #almacen = threading.local() #variable con instancia local en cada hilo
  mostrar(almacen)
  almacen.llaves = random.randint(1, 100)
  mostrar(almacen)

class local():
  pass

almacen = threading.local() #storage local a cada hilo
#Thread-local data is data whose values are thread specific.

#Main thread
mostrar(almacen)
almacen.llaves = 999
mostrar(almacen)

#Hilos
for i in range(3):
  t = threading.Thread(target=hilo, args=(almacen,))
  t.start()