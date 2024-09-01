from time import sleep, perf_counter
from threading import Thread

def tarefa(id):
    print(f'Comecando uma tarefa {id}...')
    sleep(2)
    print(f'A tarefa {id} encerrou!')


start_time = perf_counter()

#vamos criar 10 Threads
threads = []
for n in range(1,11):
	t = Thread(target=tarefa, args=(n,))
	threads.append(t)
	t.start()

#esperar pelas 10 tarefas concluírem
for t in threads:
	t.join()


end_time = perf_counter()

print(f'Levou {end_time- start_time: 0.2f} segundos(s) para completar.')