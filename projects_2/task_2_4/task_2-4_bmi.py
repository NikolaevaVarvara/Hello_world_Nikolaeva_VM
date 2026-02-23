weight = float(input("Введите вес (кг): "))
height = float(input("Введите рост (м): "))

bmi = weight / (height ** 2)
print("ОТЧЕТ О СОСТОЯНИИ ЗДОРОВЬЯ:\n")
print(f"Рост:\t{height}\nВес:\t{weight}\nИндекс массы тела пациента:\t{bmi:.2f}")