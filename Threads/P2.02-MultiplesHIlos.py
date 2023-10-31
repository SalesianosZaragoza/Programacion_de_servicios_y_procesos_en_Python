import threading
'''
The purpose of this code is to demonstrate how to create and start multiple threads in Python. The actividad function is executed in each of the 50 threads, as well as in the main thread. The order in which the messages are printed depends on the scheduling of the threads by the operating system, and may not be the same every time the program is run.
'''
def actividad():
  print ("Escribo desde un hilo")
  return

print ("INICIO")
hilos = list()
for i in range(50):
  t = threading.Thread(target=actividad)
  hilos.append(t)
  t.start()
print ("ESCRIBO EN PRINCIPAL")
