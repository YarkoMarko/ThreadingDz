from threading import Thread
from random import randint


def copy(file_name, new_file_name):
    with open(file_name, "r") as file:
        text = file.read()

    lst = list(text.split(" "))

    lst.pop(len(lst) - 1)

    print(lst)

    with open(new_file_name, "w") as file:
        for i in range(len(lst)):
            file.write(str(lst[i]) + " ")


path = input("Enter name of file: ")

with open(path, "w") as f:
    for _ in range(10):
        f.write(str(randint(1, 10)) + " ")

thread = Thread(target=copy, args=(path, input("Enter file name: ")))

thread.start()
thread.join()