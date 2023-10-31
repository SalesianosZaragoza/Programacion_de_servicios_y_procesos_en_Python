import psutil

for proc in psutil.process_iter():
  try:
    # Obtener el nombre del proceso
    nombreProceso = proc.name()    
    if proc.name() == "gedit":
      PID = proc.pid
      print(proc.username())
      print("Eliminando el proceso: ", nombreProceso , ' ::: ', PID)
      proc.kill()    
  except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
    print ("error")

