import time
import multiprocessing
import threading


def useless_function():
    dummy = 0
    for x in range(10000):
        dummy = dummy + x
        for x in range(10000):
            dummy = dummy - 1


def main():
    ##
    # try multiprocessing
    start = time.perf_counter()

    process1 = multiprocessing.Process(target=useless_function)
    process2 = multiprocessing.Process(target=useless_function)

    process1.start()
    process2.start()
    
    process1.join()
    process2.join()

    end = time.perf_counter()
    print(f'Multiprocessing finished in {round(end-start, 4)} second(s)')

    ##
    # try multithreading
    start2 = time.perf_counter()
    t1 = threading.Thread(target=useless_function)
    t2 = threading.Thread(target=useless_function)

    t1.start()
    t2.start()
 
    t1.join()
    t2.join()

    end2 = time.perf_counter()
    print(f'Multithreading finished in {round(end2-start2, 4)} second(s)')

if __name__ == "__main__":
    main()