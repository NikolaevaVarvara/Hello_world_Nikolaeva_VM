new_reagent = input("Название нового реактива: ")
quantity = int(input("Количество (целое число): "))
report = f"Реактив {new_reagent} поступил на склад в количестве {quantity} шт.."
print(report)

f = open("inventory.txt", "w", encoding="utf-8")
print(report, file=f)
f.close()