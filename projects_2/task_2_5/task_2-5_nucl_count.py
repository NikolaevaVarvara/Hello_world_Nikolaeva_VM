# Ввод днк и перевод в верхний регистр
dna = input("Введите последовательность ДНК: ")
DNA = dna.upper()
# Общая длина днк
dna_length = len(DNA)
#  Количество каждого нуклеотида
count_A = DNA.count("A")
count_T = DNA.count("T")
count_G = DNA.count("G")
count_C = DNA.count("C")
# Процентное содержание каждого нуклеотида
A = count_A / dna_length * 100
T = count_T / dna_length * 100
G = count_G / dna_length * 100
C = count_C / dna_length * 100
print("АНАЛИЗ ПОСЛЕДОВАТЕЛЬНОСТИ ДНК\n")
print(f"Последовательность в верхнем регистре: {DNA}\n")
print(f"Подсчёт нуклеотидов:\nA:\t{count_A}\nT:\t{count_T}\nG:\t{count_G}\nC:\t{count_C}\n")
print(f"Общая длина: {dna_length} нуклеотидов\n")
print(f"Процентное содержание каждого нуклеотида:\nA:\t{A}\nT:\t{T}\nG:\t{G}\nC:\t{C}\n")

