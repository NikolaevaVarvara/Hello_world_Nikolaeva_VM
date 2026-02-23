volume = int(input("Введите нужный объем раствора (в мл): "))

salt_mass = volume * 0.009
normal_salt_mass = f"{salt_mass:.2f}"
water_volume = volume
with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write(f"ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n")
    file.write("-" * 23)
    file.write(f"\nОбщий объем:\t{volume} мл\nМасса соли:\t{normal_salt_mass} г\nОбъем воды:\t{water_volume} мл")

