import threading
from random import randint


def fill(lst, lst_len):
    for _ in range(lst_len):
        lst.append(randint(1, 10))


def summ(lst):
    global summ1

    for value in lst:
        summ1 += value


def avr(lst):
    global summ1, avr1
    avr1 = summ1 / len(lst)


lst = []
summ1 = 0
avr1 = 0
t1 = threading.Thread(target=fill, args=(lst, 5, ))
t2 = threading.Thread(target=summ, args=(lst, ))
t3 = threading.Thread(target=avr, args=(lst, ))

t1.start()
t1.join()

t2.start()
t3.start()

t2.join()
t3.join()

print(lst)
print(summ1)
print(avr1)