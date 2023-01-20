from multiprocessing import Process, Queue, Value
import RightSide, LeftSide

temp = 3
def main():
    street = Value('d', 0)
    id = Value('d', 1)
    turnP = Value('d', 0)
    turnC = Value('d', 0)
    f0P = Value('d', 0)
    fP1 = Value('d', 0)
    f0C = Value('d', 0)
    f1C = Value('d', 0)

    car_list1 = Queue(maxsize=10)
    car_list2 = Queue(maxsize=10)

    prod1 = Process(target=RightSide.producer, args=(car_list1, id, f0P, fP1, turnP))
    cons1 = Process(target=RightSide.consumer, args=(car_list1, street, f0C, f1C, turnC))
    prod1.start()
    cons1.start()

    prod2 = Process(target=LeftSide.producer, args=(car_list2, id, f0P, fP1, turnP))
    cons2 = Process(target=LeftSide.consumer, args=(car_list2, street, f0C, f1C, turnC))
    prod2.start()
    cons2.start()


if __name__ == '__main__':
    main()

