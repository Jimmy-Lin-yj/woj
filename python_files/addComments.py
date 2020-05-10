import time
import threading
def count(n):
    for i in range(n):
        pass
start = time.time()
n=10**8
#count(n)
t1 = threading.Thread(target=count,args=[n//2])
t2 = threading.Thread(target=count,args=[n//2])
t1.start()
t2.start()
t1.join()
t2.join()
print(time.time()-start)