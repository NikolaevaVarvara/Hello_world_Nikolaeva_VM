operators_name = input("Введите имя оператора: ")
sensor_value = input("Введите текущее значение датчика давления: ")
with open("sensor_log.txt", "w", encoding="utf-8") as file:
    file.write(f"ОПЕРАТОР: {operators_name}\tЗНАЧЕНИЕ: {sensor_value}")
print("Данные успешно сохранены в sensor_log.txt")