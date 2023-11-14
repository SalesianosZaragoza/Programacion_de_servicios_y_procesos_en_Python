from threading import *
import time

def hilo():				
  for i in range(10):
    print('Hilo no Daemon (Foregoround)')
    time.sleep(1)
  print('Terminando Hilo secundario')

t = Thread(target=hilo)
t.start()	

time.sleep(5)				
print('Terminando Hilo principal')