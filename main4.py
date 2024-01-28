from threading import Thread


def search(file_name):
    global new_file

    with open(file_name, "r") as file:
        text = file.read()

    lst = list(text.split(" "))

    lst.pop(len(lst) - 1)

    print(lst)

    searching_word = input("Enter word to search: ")

    new_file = input("Enter new file: ")

    with open(new_file, "w") as file:
        for word in lst:
            if searching_word in word:
                file.write(word + " ")


def filtration():
    with open(path_forbidden, "r") as file:
        text = file.read()

    lst = list(text.split(" "))

    #lst.pop(len(lst) - 1)

    print(lst)

    with open(new_file, "r") as file:
        text = file.read()

    lst2 = list(text.split(" "))

    lst2.pop(len(lst2) - 1)

    print(lst2)

    new_file2 = input("Enter new file: ")

    flag = True

    with open(new_file2, "w") as file:
        for word in lst2:
            for new_word in lst:
                if new_word in word:
                    flag = False
                    break

            if flag:
                file.write(word + " ")

            else:
                flag = True


path_forbidden = "forbidden.txt"

path = input("Enter first file: ")

with open(path, "w") as file:
    for _ in range(10):
        file.write(input("Enter word: ") + " ")

thread1 = Thread(target=search, args=(path, ))
thread2 = Thread(target=filtration, args=())

thread1.start()
thread1.join()

thread2.start()
thread2.join()

