import multiprocessing
import time
import os

def gentle_cpu_worker(target_load=0.4):
    """
    Генерирует контролируемую нагрузку на одно ядро.
    target_load = 0.4 означает ~40% нагрузки.
    """
    print(f"[CPU] Поток запущен на PID: {os.getpid()}")
    
    # Временной шаг в секундах (окно регулирования)
    step_time = 0.1
    run_time = step_time * target_load
    sleep_time = step_time * (1 - target_load)

    while True:
        start_time = time.time()
        # Активная фаза: крутим пустой цикл ровно run_time секунд
        while time.time() - start_time < run_time:
            pass  # Просто сжигаем такты процессора
        
        # Фаза отдыха: даем ядру остыть sleep_time секунд
        time.sleep(sleep_time)

def start_gentle_load():
    # Задаем желаемую нагрузку (0.3 = 30%, 0.5 = 50%)
    LOAD_PERCENT = 0.35 
    
    cores = multiprocessing.cpu_count()
    print(f"Обнаружено ядер: {cores}")
    print(f"Запускаем щадящую нагрузку (~{int(LOAD_PERCENT * 100)}%) на все ядра...")
    
    processes = []
    for _ in range(cores):
        p = multiprocessing.Process(target=gentle_cpu_worker, args=(LOAD_PERCENT,))
        p.start()
        processes.append(p)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nОстанавливаем нагрузку...")
    finally:
        for p in processes:
            p.terminate()
        print("Процессор полностью свободен.")

if __name__ == "__main__":
    start_gentle_load()
