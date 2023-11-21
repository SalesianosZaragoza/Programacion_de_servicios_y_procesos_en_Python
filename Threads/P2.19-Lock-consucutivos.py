import threading 
    
algo = 0
print(algo)
lock = threading.Lock() 
  
lock.acquire() 
algo +=1
print(algo) 
lock.acquire()  
algo += 2
print(algo)
lock.release() 
  
print(algo) 