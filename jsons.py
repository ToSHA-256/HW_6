import json
import csv


def task_1():
    b_str = b'r\xc3\xa9sum\xc3\xa9'
    s_str = b_str.decode()
    print(b_str.decode())
    print(s_str.encode("iso-8859-1"))


def task_2():
    str_1 = input("Enter string 1: ")
    str_2 = input("Enter string 2: ")
    str_3 = input("Enter string 3: ")
    str_4 = input("Enter string 4: ")

    wr_fl = open("strings.txt", "w")
    wr_fl.write(str_1 + "\n")
    wr_fl.write(str_2 + "\n")
    wr_fl.close()

    with open("strings.txt", "a") as write_to_file:
        write_to_file.write(str_3 + "\n")
        write_to_file.write(str_4 + "\n")


def task_3():
    top_stars = {100001: ("Scarlett Johansson", 38),
                 100002: ("Robert Downey, Jr.", 57),
                 100003: ("Samuel L. Jackson", 74),
                 100004: ("Zoe Saldana", 44),
                 100005: ("Chris Hemsworth", 39),
                 100006: ("Chris Pratt", 43), }

    with open("Top_start_in_leading_roles.json", "w") as write_to:
        json.dump(top_stars, write_to)


def task_4():
    with open("Top_start_in_leading_roles.json", "r") as write_to:
        top_stars = json.load(write_to)

    top_stars_phone = {100001: "+182363541",
                       100002: "+172652562",
                       100003: "+162758541",
                       100004: "+152652802",
                       100005: "+142752077",
                       100006: "+152652005"}

    with open("stars_imdb.csv", "w") as convert_2_csv:
        file_writer = csv.writer(convert_2_csv)
        columns_name = ["ID", "Name", "Age", "Agent`s phone numb"]
        file_writer.writerow(columns_name)
        for iterator in top_stars:
            iter2 = int(str(iterator))
            tmp_list = top_stars[iterator]
            tmp_list.append(top_stars_phone[int(str(iter2))])
            tmp_list.insert(0, iterator)
            file_writer.writerow(tmp_list)


# Tasks
task_1()
task_2()
task_3()
task_4()
