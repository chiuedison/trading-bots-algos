import time
import multiprocessing

def increment(counter):
    print("whee")
    # time.sleep(0.1)
    counter.value += 1

def useless_function(sec):
     print(f'Sleeping for {sec} second(s)')
     time.sleep(sec)
     print(f'Done sleeping')

def push_buys(list):
    # loop 5 times
    for i in range(10):
        time.sleep(0.1)
        list.append(i)

def push_sells(list):
    # loop 5 times
    for i in range(10):
        time.sleep(0.1)
        list.append(-i)

def main():
    # counter = 0
    manager = multiprocessing.Manager()
    list = manager.list()
    start = time.perf_counter()
    process1 = multiprocessing.Process(target=push_buys, args=[list])
    process2 = multiprocessing.Process(target=push_sells, args=[list])
    process1.start()
    process2.start()
    process1.join()
    process2.join()
    end = time.perf_counter()
    print(f'Finished in {round(end-start, 4)} second(s)')
    print(list)

if __name__ == "__main__":
    main()