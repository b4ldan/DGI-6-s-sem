DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}


friend_city = ''
unique_cities = set(DATABASE.values())
for city in list(unique_cities):
        friend_city += str(city) + ' '

print(friend_city)



