import time
from datetime import datetime

# def execution_time(func):

#     def get_time(N):
#         start_time =  time.time()
#         func(N)
#         last_time = time.time()
#         final_time = last_time - start_time
#         print(f"function executed in {final_time} 's")

#     return get_time



# @execution_time
# def bucle(N):
#     lista = []
#     for n in range(N):
#         for i in range(10):
#             numbers = (n,i)
#             lista.append(numbers)

#     print(lista)
#     return lista






def execution_time(func):
    def wrapper():
        initial_time = datetime.now()
        func()
        final_time = datetime.now()
        time_elapsed =  final_time - initial_time
        print(f"Funcion executed in {time_elapsed.total_seconds()} 's")

    return wrapper

@execution_time
def random_func():
    for _ in range(1000000):
        pass


random_func()