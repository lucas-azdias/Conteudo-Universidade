#!/usr/bin/env python3

import threading
import time
import random
import os
import sys 

EXE = 1

# REGISTRA O LANÇAMENTO DA THREAD EM UM LOG
def writelog(n):
    f = open('log.txt','a')
    f.write(f'thread {n}\n')
    f.close()

# REPRESENTA A THREAD
def minhathread(n):
    global count
    t = random.randint(1,3)
    time.sleep(t)
    
    if EXE == 4 and n == 5:
        print(f'A thread {n} causou uma violação no sistema')
        os._exit(0) # aborta o processo imediatamente
        sys.exit() # lança uma exceção

    #lock.acquire()
    mycount = count
    writelog(n)
    print(f'Thread {n} lançada em {t}s')
    count = mycount + 1
    #lock.release()

#--------------------------------------------------------------------------
# PROCESSO PRINCIPAL
if __name__ == '__main__':

    start = time.time()
    open('log.txt','w').close()

    count = 0
    threads = []
    lock = threading.Lock()

    for i in range(10):
        t = threading.Thread(target=minhathread, args=(i,)) 
        threads.append(t)
        t.start()
  
    for x in threads : x.join()

    print("Threads lançadas ", count)
    print('Tempo de execucao', time.time() - start )