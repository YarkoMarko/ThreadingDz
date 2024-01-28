import os

from threading import Thread
import random


def check(num):
    for i in range(2, int(num) + 1):
        if i != int(num) and int(num) % i == 0:
            return False

    return True


def factorial(num):
    if int(num) == 1 or int(num) == 0:
        return 1

    return int(num) * factorial(int(num) - 1)


def fill_file(file_name, element_amount):
    with open(file_name, "w") as file:
        for _ in range(element_amount):
            file.write(str(random.randint(1, 10)) + " ")


def simple_nums(file_name):
    global file_new

    with open(file_name, "r") as file:
        text = file.read()

    lst = list(text.split(" "))

    lst.pop(len(lst) - 1)

    lst1 = list(filter(lambda x: check(x), lst))

    file_new = write_into_file(input("Enter file name: "), lst1, checker=True)

    print(f"Simple numbers: {lst1}")


def factorial_numbers(file_name):
    with open(file_name, "r") as file:
        text = file.read()

    lst = list(text.split(" "))

    lst.pop(len(lst) - 1)

    lst2 = list(map(lambda x: factorial(x), lst))

    write_into_file(file_new, lst2, checker=False)

    print(f"Factorials: {lst2}")


def write_into_file(file_name, lst, checker):
    if checker:
        with open(file_name, "w") as f:
            for i in range(len(lst)):
                f.write(str(lst[i]) + " ")

            f.write("\n")

        return file_name

    else:
        with open(file_name, "a") as f:
            for i in range(len(lst)):
                f.write(str(lst[i]) + " ")

            f.write("\n")

        return None




path = input("Enter: ")

print(path)

#fill_file(path, 10)

#print(simple_nums(path))

#print(factorial_numbers(path))

thread1 = Thread(target=fill_file, args=(path, 10, ))
thread2 = Thread(target=simple_nums, args=(path, ))
thread3 = Thread(target=factorial_numbers, args=(path, ))
#
thread1.start()
thread1.join()

#print(simple_nums(path))

thread2.start()
thread2.join()

thread3.start()
thread3.join()


#print(factorial_numbers(path))

#
# thread2.start()
# thread3.start()
#
# thread2.join()
# thread3.join()

#print(os.getcwd())