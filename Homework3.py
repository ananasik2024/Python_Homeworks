# Задание 1
# Видеокарты
# В базе магазина электроники есть список видеокарт компании NVIDIA 
# разных поколений. Вместо полных названий хранятся только числа, 
# которые обозначают модель и поколение видеокарты. Недавно компания 
# выпустила новую линейку видеокарт. Самые старшие поколения разобрали 
# за пару дней. Напишите программу, которая удаляет наибольшие элементы 
# из списка видеокарт.

# num_of_models = int(input('Введите количество видеокарт: '))
# nvidias_models = []

# for _ in range(num_of_models):
#      model = int(input('Введите модель видеокарты: '))
#      nvidias_models.append(model)

# print('Список всех видеокарт: ', nvidias_models)

# maxItem = max(nvidias_models)  # Находим максимальное значение
# updates_models = [model for model in nvidias_models if model != maxItem]  # Генератор списка
# print('Список видеокарт после обновления:', updates_models)