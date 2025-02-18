### Задание 1: Поставьте оценку!
# Вася выложил своё новое приложение на платформу для начинающих 
# разработчиков,на ней пользователи могут ставить оценку приложению: 
# от −100 до 100. Ему захотелось сравнить количество положительных и 
# отрицательных отзывов, для этого он заранее отфильтровал все отзывы 
# так, чтобы в конце были те, которые равны нулю. Напишите программу, 
# которая находит количество положительных и количество отрицательных 
# чисел в последовательности. Последовательность заканчивается на 
# числе 0.
# Пример
# Введите число: −4
# Введите число: −90
# Введите число: 6
# Введите число: 0
# Кол-во положительных чисел: 1
# Кол-во отрицательных чисел: 2

# positive = 0
# negative = 0

# n = int(input('Введите оценку приложения: '))

# while n != 0:
# 	if n > 0:
# 		positive += 1
# 	else:
# 		negative += 1

# 	n = int(input('Введите оценку приложения: '))

# print (f'Кол-во отрицательных чисел: {negative}')
# print (f'Кол-во положительных чисел: {positive}')

# Задача 2. Обычный день на работе
# Максим программирует целый день на работе и вечером идёт домой. 
# Каждый час начальство кидает ему несколько задач, которые нужно 
# решить до следующего рабочего часа. Вдобавок каждый час Максиму 
# звонит супруга. Он знает, что если он возьмёт трубку, то жена попросит 
# зайти вечером в магазин. Напишите программу, в которой считается, 
# сколько задач выполнил Максим за день (восемь часов). Если он хотя 
# бы раз взял трубку, то в конце дополнительно выводите сообщение: 
# «Нужно зайти в магазин».

# task_sum = 0
# go_to_store = False
# hours = 0 

# print('Начался 8-часовой рабочий день')

# while hours < 8:
# 	hours += 1
# 	print (hours, 'час')

# 	solved_tasks = int(input('Сколько задач решит максим?: '))
# 	task_sum += solved_tasks
	
# 	call = int(input('Звонит жена. Взять трубку? (1 - да, 0 - нет): '))
# 	if call == 1:
# 		go_to_store = True

# print ('Рабочий день закончился. Всего выполнено задач: ', task_sum)
# if go_to_store:
# 	print ('Нужно зайти в магазин')

### Задача 3. Игра «Угадай число»

# Папа-программист написал для сына программу, которая просит 
# его угадать число. Недостаток программы был в том, что бедному 
# сыну приходилось её каждый раз перезапускать, чтобы угадывать число. 
# Теперь, когда мы знаем гораздо больше, пришло время исправить этот 
# недостаток и заодно немного улучшить саму игру. Напишите программу-игру, 
# которая запрашивает у пользователя число до тех пор, пока он его не 
# отгадает. Выводите сообщения в соответствии с примером.

# guess_count = 0
# number = int(input('Загадайте число: '))

# while True:
# 	n = int(input('Введите число: '))
# 	if n > number:
# 		print ('Число больше, чем нужно. Попробуйте ещё раз!')
# 		guess_count += 1
# 	elif n < number:
# 		print ('Число меньше, чем нужно. Попробуйте ещё раз!')
# 		guess_count += 1
# 	else:
# 		print ('Вы угадали! Число попыток: ', guess_count)
# 		break

### Задача 4. Посчитай чужую зарплату...

# Бухгалтер устала постоянно считать вручную среднегодовую 
# зарплату сотрудников компании и, чтобы облегчить себе жизнь, 
# обратилась к программисту. Напишите программу, которая принимает 
# от пользователя зарплату сотрудника за каждый из 12 месяцев и выводит 
# на экран среднюю зарплату за год.

# salary_year = 0

# for i in range (12):
# 	while True:
# 		try:
# 			salary = int(input(f'Введите зарплату за {i+1} месяц: '))
# 			if salary < 0:
# 				print ('Зарплата не может быть отрицательной, попробуйте снова')
# 				continue
# 			break
# 		except ValueError:
# 			print ('Введено не число, попробуйте снова')
			
# 	salary_year += salary
	
# average_salary = salary_year // 12
# print('Среднегодовая заработная плата сотрудника:', average_salary)

### Задача 5. Пропавшая карточка

# Для настольной игры используются карточки с номерами от 1 до N. 
# Одна карточка потерялась. Напишите программу, которая поможет найти 
# потерянную карточку, если номера оставшихся известны. Найдите её, зная 
# номера оставшихся карточек. Введите число карточек — N. Затем введите 
# N − 1 номера оставшихся карточек. Они могут быть введены в любом порядке.

# total_sum = 0

# N = int(input('Введите число карточек: '))

# total_sum = N * (N + 1) // 2 
	
# for i in range (N - 1):
# 	card_number = int(input('Введите номер оставшейся карточки: '))
# 	total_sum -= card_number
	
# print ('Потерявшаяся карточка №: ', total_sum)
	