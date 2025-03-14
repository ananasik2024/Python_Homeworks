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

# Задание 2: Илья зашёл на любительский киносайт, на котором пользователи оставляют
# рецензии на фильмы. Их список: 
# films = [‘Крепкий орешек’, ‘Назад в будущее’, ‘Таксист’, ‘Леон’, 
# ‘Богемская рапсодия’, ‘Город грехов’, ‘Мементо’, ‘Отступники’, ‘Деревня’]
# Илья на сайте в первый раз. Он хочет зарегистрироваться и сразу добавить
# часть фильмов в список любимых, чтобы позже прочитать рецензии на них.
# Напишите программу, в которой пользователь вводит фильм. Если кинокартина
# есть в перечне, то добавляется в список любимых. Если её нет, то выводится
# ошибка. В конце выведите весь список любимых фильмов.
# Пример:
# Сколько фильмов хотите добавить? 3
# Введите название фильма: Леон
# Введите название фильма: Безумный Макс
# Ошибка: фильма Безумный Макс у нас нет :(
# Введите название фильма: Мементо
# Ваш список любимых фильмов: Леон, Мементо

# films = ['Леон' , 'Титаник', 'Отступники', 'Обитель зла', 'Зеленая миля', 'Достучаться до небес']
# my_list = []
 
# num_of_films = int(input('Сколько фильмов хотите добавить? '))
 
# for _ in range (num_of_films):
# 	while True:  # Бесконечный цикл, пока не введут правильный фильм
#           movie = input('Введите название фильма: ')
        
#           if movie in films:
#                my_list.append(movie)  # Добавляем фильм в список
#                break  # Выходим из while, если фильм найден
#           else:
#                print(f'Ошибка: фильма {movie} у нас нет :( Введите другой фильм.')
		
# print('Список ваших любимых фильмов:', ', '.join(my_list))

### Задача 3. Сортировка
# Дан список из N чисел. Напишите программу, которая сортирует элементы
# списка по возрастанию и выводит их на экран. Дополнительный список
# использовать нельзя.
# Также нельзя использовать готовые функции sorted/min/max и метод sort
# Постарайтесь придумать и написать как можно более эффективный алгоритм
# сортировки.
# Пример:
# Изначальный список: [1, 4, –3, 0, 10]
# Отсортированный список: [–3, 0, 1, 4, 10]

# list_3 = [1, 4, -3, 0, 10]
# print('Изначальный список: ', list_3)

# for i in range (len(list_3) - 1):
# 	for j in range (len(list_3) - 1 - i):
# 		if list_3[j] > list_3[j + 1]:
# 		     list_3[j], list_3[j + 1] = list_3[j + 1], list_3[j] #меняем местами текущий элемент со следующим
			
# print('Отсортированный список: ', list_3)