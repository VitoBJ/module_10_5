import time
import multiprocessing
import os


def read_info(name):
    if not os.path.isfile(name):
        print(f"Файл не найден: {name}")
        return
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())
    return


if __name__ == '__main__':
    file_names = ['file 1.txt', 'file 2.txt', 'file 3.txt']


    start_time = time.time()
    for file_name in file_names:
        read_info(file_name)
    linear_time = time.time() - start_time
    print(f"Время выполнения линейного подхода: {linear_time:.2f} секунд")

    
    start_time = time.time()
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        pool.map(read_info, file_names)
    parallel_time = time.time() - start_time
    print(f"Время выполнения многопроцессного подхода: {parallel_time:.2f} секунд")