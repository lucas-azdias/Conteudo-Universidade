from time import sleep, perf_counter
from threading import Thread

def tarefa():
    print('Comecando uma tarefa...')
    sleep(2)
    print('feito')


start_time = perf_counter()

#criamos duas Threads
tarefa1 = Thread(target=tarefa)
tarefa2 = Thread(target=tarefa)

#dispara as tarefas
tarefa1.start()
tarefa2.start()

#espera as tarefas concluírem
tarefa1.join()
tarefa2.join()

end_time = perf_counter()

print(f'Levou {end_time- start_time: 0.2f} segundos(s) para completar.')