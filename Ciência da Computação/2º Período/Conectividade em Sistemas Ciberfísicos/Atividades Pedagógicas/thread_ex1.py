from time import sleep, perf_counter

def tarefa():
    print('Comecando uma tarefa...')
    sleep(2)
    print('feito')


start_time = perf_counter()

tarefa()
tarefa()

end_time = perf_counter()

print(f'Levou {end_time- start_time: 0.2f} segundos(s) para completar.')