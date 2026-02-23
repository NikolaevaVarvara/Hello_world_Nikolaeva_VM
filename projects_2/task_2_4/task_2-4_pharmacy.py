total_quantity = int(input("Введите общее количество произведенных капсул: "))
packaging = int(input("Введите количество капсул в одной упаковке: "))

full_packages = total_quantity // packaging
remains = total_quantity % packaging

print("ОТЧЕТ ФАСОВОЧНОГО ЦЕХА:\n")
print(f"Полных упаковок:\t{full_packages}\nОстаток капсул:\t{remains}")