nutrient_medium = input("Название питательной среды: ")
concentration = input("Концентрация агара (%): ")
temperature = input("Температуру стерилизации (°C): ")

with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write(f"НАЗВАНИЕ ПИТАТЕЛЬНОЙ СРЕДЫ: {nutrient_medium}\n") 
    file.write(f"Концентрация агара (%):  {concentration}\n")
    file.write(f"Температура стерилизации (°C):  {temperature}")

print("Файл 'recipe.txt' успешно сформирован!")