geo_logs = [
  {'visit1': ['Москва', 'Россия']},
  {'visit2': ['Дели', 'Индия']},
  {'visit3': ['Владимир', 'Россия']},
  {'visit4': ['Лиссабон', 'Португалия']},
  {'visit5': ['Париж', 'Франция']},
  {'visit6': ['Лиссабон', 'Португалия']},
  {'visit7': ['Тула', 'Россия']},
  {'visit8': ['Тула', 'Россия']},
  {'visit9': ['Курск', 'Россия']},
  {'visit10': ['Архангельск', 'Россия']}
]
for visit in geo_logs:
  country = visit.values()
  for city in country:
    if city[1] == 'Россия':
      print(city)

ids = {'user1': [213, 213, 213, 15, 213],
      'user2': [54, 54, 119, 119, 119],
      'user3': [213, 98, 98, 35]}
id = (ids.values())
for list in id:
  logs = []
  logs.append(list)
  print(set(list))

queries = [
  'смотреть сериалы онлайн',
  'навости спорта',
  'афиша кино',
  'курс доллара',
  'сериалы этим летом'
  'курс по питону',
  'сериалы про спорт'
]
storage = {}

for tv in queries:
    words = tv.split()
    if len(words) in storage.keys():
        storage[len(words)] += 1
    else:
        storage.update({
            len(words): 1
        })

for key, value in storage.items():
    percent = round((value / len(queries)) * 100, 2)
    print(f'Поисковых запросов из {key} слов: {percent}%')

stats = {'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
max = max(stats.items())
print(max[0])

slovar = ['2018-01-01', 'yandex', 'cpc', 100]
order = {slovar[-2]: slovar[-1]}
for check in slovar[:-2][::-1]:
  order = {check: order}
print(order)