import threading

def escribeLetter(letter):
  for i in range(100):
    print (letter, end="", flush=True)
  return

print ("INICIO")
t1 = threading.Thread(target=escribeLetter, args=("Y"))
t1.start()
#t2 = threading.Thread(target=escribeLetter, args=("X"))
#t2.start()

for i in range(100):
  print ("X", end="", flush=True)