researchers_fio = input("Введите ФИО исследователя: ") 
date = input("Введите дату эксперимента: ") 
experiment_title = input("Введите название эксперимента: ") 
conclusion = input("Введите вывод из эксперимента: ") 

with open("journal.txt", "w", encoding="utf-8") as file:
    file.write("Электронный лабораторный журнал\n", end="|_______________________________________________________|\n")
    file.write(f"ФИО исследователя:\t{researchers_fio}\nДата:\t{date}\nЭксперимент:\t{experiment_title}\n", end="|_______________________________________________________|\n")
    file.write(f"Вывод:\n{conclusion}\n", end="|_______________________________________________________|\n")
print("Данные успешно сохранены в journal.txt")


