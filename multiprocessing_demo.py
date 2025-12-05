import multiprocessing


def process_worker(shared_counter):
    for _ in range(100_000):
        with shared_counter.get_lock():
            shared_counter.value += 1


if __name__ == "__main__":
    counter = multiprocessing.Value('i', 0)
    processes = [multiprocessing.Process(target=process_worker, args=(counter,)) for _ in range(4)]

    for p in processes:
        p.start()
    for p in processes:
        p.join()

    print(f"Итоговый счётчик (процессы): {counter.value}")
