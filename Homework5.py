# Задача 1:
# Поиск элемента
# Пользователь вводит искомый ключ. Если он хочет, то может ввести
# максимальную глубину — уровень, до которого будет просматриваться
# структура.
# Напишите функцию, которая находит заданный пользователем ключ в словаре
# и выдаёт значение этого ключа на экран. По умолчанию уровень не задан. В
# качестве примера можно использовать такой словарь:
# site = {
# 'html': {
# 'head': {
# 'title': 'Мой сайт'
# },
# 'body': {
# 'h2': 'Здесь будет мой заголовок',
# 'div': 'Тут, наверное, какой-то блок',
# 'p': 'А вот здесь новый абзац'
# }
# }
# }
# def find_key(struct, key, max_depth=None, depth=1):
#      result = None # Переменная для хранения найденного значения
#      if max_depth and max_depth < depth:
#           return result

#      if key in struct:
#           return struct[key]
     
#      for sub_struct in struct.values():
#           if isinstance(sub_struct, dict):
#                result = find_key(sub_struct, key, max_depth, depth=depth + 1)
#                if result:
#                     break    
#      return result 

# site = {
# 'html': {
# 'head': {
# 'title': 'Мой сайт'
# },
# 'body': {
# 'h2': 'Здесь будет мой заголовок',
# 'div': 'Тут, наверное, какой-то блок',
# 'p': 'А вот здесь новый абзац'
# }
# }
# }

# while True:
#      key = input('Введите искомый ключ: ') 

#      if key.lower() == 'exit':  # Выход из цикла
#         print("Выход из программы.")
#         break

#      answer = input('Хотите ввести максимальную глубину? Y/N: ') 

#      if answer.lower() == 'y':
#           max_depth = int(input('Введите максимальную глубину: ')) #
#      else:
#           max_depth = None 
#      print('Значение ключа:', find_key(struct=site, max_depth=max_depth, key=key))

### Задание 2

# Глубокое копирование

# Вы сделали для заказчика структуру сайта по продаже телефонов:
# site = {
# 'html': {
# 'head': {
# 'title': 'Куплю/продам телефон недорого'
# },
# 'body': {
# 'h2': 'У нас самая низкая цена на iPhone',
# 'div': 'Купить',
# 'p': ‘Продать'
# }
# }
# }

# # Исходная структура сайта
# site = {
#      'html': {
#           'head': {
#                'title': 'Куплю/продам телефон недорого'
#           },
#           'body': {
#                'h2': 'У нас самая низкая цена на iPhone',
#                'div': 'Купить',
#                'p': 'Продать'
#           }
#      }
# }
# # Функция для замены значения в структуре словаря
# def change_value(struct, key, value):
#      if key in struct:
#           struct[key] = value
#      else:
#           for sub_struct in struct.values():
#                if isinstance(sub_struct, dict): change_value(sub_struct, key, value)
#      return struct
# # Функция для отображения структуры сайта
# def display_struct(struct, spaces=1):
#      for key, value in struct.items():
#           if isinstance(value, dict): 
#                print(' ' * spaces, key)
#                display_struct(value, spaces + 3)
#           else:
#                print("{}{} : {}".format(' ' * spaces, key, value))

# # Функция для создания сайта под конкретный продукт
# import copy
# def make_site(name):
#      struct_site = copy.deepcopy(site) # Глубокое копирование исходного сайта
#      new_title = 'Куплю/продам {} недорого'.format(name) # Изменяем заголовок
#      struct_site = change_value(struct_site, 'title', new_title)
#      new_h2 = 'У нас самая низкая цена на {}'.format(name) # Изменяем заголовок второго уровня
#      struct_site = change_value(struct_site, 'h2', new_h2)
#      return struct_site

# # Основная часть программы
# sites = []
# sites_count = int(input('Сколько сайтов: '))
# for _ in range(sites_count):  
#      product_name = input('Введите название продукта для нового сайта: ')
#      new_site = make_site(product_name)
#      sites.append(new_site)
#      for i_site in sites:
#           display_struct(i_site)