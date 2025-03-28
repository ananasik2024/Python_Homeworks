#Задание1
# # import os

# numbers_file = open("numbers.txt", "r", encoding="utf-8") # Открываем входной файл для чтения

# total_sum = 0 # Инициализируем переменную для хранения суммы чисел

# # Читаем файл построчно
# for line in numbers_file: # Разбиваем строку на части, используя пробелы и новые строки в качестве разделителей
#      numbers = [int(num) for num in line.split() if num] # Преобразуем каждую часть в целое число и накапливаем сумму
#      total_sum += sum(numbers)

# # Закрываем файл после чтения
# numbers_file.close()

# # Открываем выходной файл для записи
# sum_file = open("answer.txt", "w", encoding="utf-8")
# sum_file.write(str(total_sum)) # Записываем сумму в выходной файл

# # Закрываем выходной файл
# sum_file.close()

#////////////////////////////////////////////////////////////////
#Задание2
#Первый вариант решение (эталонное решение)
# Открываем файл для чтения
# philosophical_text = open("zen.txt", "r")
# lines = philosophical_text.readlines() # Считываем все строки в список
# philosophical_text.close() # Закрываем файл после чтения

# # Проходим по строкам в обратном порядке и выводим каждую строку без символа новой строки в конце
# for line in reversed(lines):
#      print(line.strip())

#2 вариант решения (предложенный чато gpt как лучший вариант)
# with open("zen.txt", "r", encoding="utf-8") as file:
#     lines = file.readlines()  

# for line in reversed(lines):
#     print(line.strip())

#////////////////////////////////////////////////////////////////

# Задание 3

# # Открываем файл first_tour.txt для чтения
# with open("first_tour.txt", "r") as file:
#      lines = file.readlines()
#      K = int(lines[0]) # Первая строка содержит число K
#      participants = {} # Словарь для хранения данных участников
#      filter_player = {} # Словарь для хранения участников, прошедших во второй тур
#      filter_player = {}
#      count = 1

# # Обрабатываем оставшиеся строки
# for line in lines[1:]:
#      data = line.strip().split() # Разделяем строку на части
#      name = f"{data[1][0]}. {data[0]}" # Формируем имя участника с инициалом
#      score = int(data[-1]) # Получаем количество баллов
#      participants[name] = score # Сохраняем участника и его баллы

# # Фильтруем участников, набравших более K баллов
# for player, score in participants.items():
#      if score > K:
#           filter_player[player] = score

# # Сортируем участников по убыванию баллов
# sorted_filter_player = dict(sorted(filter_player.items(), key=lambda
# x: x[1], reverse=True))

# # Открываем файл second_tour.txt для записи
# with open("second_tour.txt", "w") as file:
#      file.write(f"{len(sorted_filter_player)}\n") # Записываем количество участников второго тура
#      for player, score in sorted_filter_player.items(): # Записываем данные участников с нумерацией
#           file.write(f"{count}) {player} {score}\n")
#           count += 1

# //////////////////////////////////

# Задача 4
# Определяем английский алфавит
english_alphabet = 'abcdefghijklmnopqrstuvwxyz'
total_letters = 0

with open("text.txt", "r") as file: # Открываем файл text.txt и считываем текст
     text = file.read().lower() # Приводим текст к нижнему регистру

# Создаем словарь для подсчета количества каждой буквы
letter_count = {letter: 0 for letter in english_alphabet}

# Подсчитываем количество вхождений каждой буквы
for char in text:
     if char in english_alphabet:
          letter_count[char] += 1
          total_letters += 1
     
# Вычисляем частоту встречаемости каждой буквы
letter_freq = {letter: (count / total_letters) for letter, count in
letter_count.items() if count > 0}

# Сортируем буквы по убыванию частоты и по алфавиту при равенстве частоты
sorted_letters = sorted(letter_freq.items(), key=lambda x: (-x[1],
x[0]))

# Записываем результат в файл analysis.txt
with open("analysis.txt", "w") as file:
     for letter, freq in sorted_letters:
          file.write(f"{letter} {freq:.3f}\n")