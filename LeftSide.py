from multiprocessing import Process, Queue, Value, Array
from time import sleep
from Car import Car


def producer(queue, id, f0P, f1P, turnP):
    print('Producer: Running', flush=True)
    while True:
        value = Car(id.value)
        turnP.value = 1
        f0P.value = 1
        while f1P.value == 1 and turnP.value == 1:
            pass
        # critical section start here
        id.value += 1
        # critical section finish here
        f0P.value = 0
        sleep(1)
        queue.put(value)


def consumer(queue, street, f0C, f1C, turnC):
    print('Consumer: Running', flush=True)
    while True:
        item = queue.get()
        f0C.value = 1
        turnC.value = 1
        while f1C.value == 1 and turnC.value == 1:
            pass
        # critical section start here
        street.value = item.id
        print('left car id: ', item.id, 'sleep: ', item.time)
        temp = street.value
        sleep(item.time)
        # critical section finish here
        if temp != street.value:
            print('Process conflict!')
        f0C.value = 0
