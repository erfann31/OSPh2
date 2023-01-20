from multiprocessing import Process, Queue, Value, Array
from time import sleep
from Car import Car


def producer(queue, id, f0P, f1P, turnP):
    print('Producer: Running', flush=True)
    while True:
        value = Car(id.value)
        turnP.value = 0
        f1P.value = 1
        while f0P.value == 1 and turnP.value == 0:
            pass
        # critical section start here
        id.value += 1
        # critical section finish here
        f1P.value = 0
        sleep(0.5)
        queue.put(value)


def consumer(queue, street, f0C, f1C, turnC):
    print('Consumer: Running', flush=True)
    while True:
        item = queue.get()
        f1C.value = 1
        turnC.value = 0
        while f0C.value == 1 and turnC.value == 0:
            pass
        # critical section starts here
        street.value = item.id
        print('right car id: ', item.id, 'sleep: ', item.time)
        temp = street.value
        sleep(item.time)
        # critical section finish here
        if temp != street.value:
            print('Process conflict!')
        f1C.value = 0
