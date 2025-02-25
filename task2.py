import random
import requests

url = "https://rickandmortyapi.com/api/"
response = requests.get(url)
print(response.json())
print()

# Можно узнать о персонажах, локациях и эпизодах мультсериала через поля /character, /location, /episode
# Каждый обработанный запрос содержит info - объект с информацией об ответе: count - количество запросов,
# pages - количество страниц, next - ссылка на следующую страницу, prev - ссылка на предыдущую страницу

# Примеры для /character

print("Случайный персонаж из всех")
url = f"https://rickandmortyapi.com/api/character/{random.randint(1, 826)}"
response = requests.get(url)
print(response.json())
print()

print("Персонаж по имени")
url = f"https://rickandmortyapi.com/api/character/?name=pickle"
response = requests.get(url)
print(response.json())
print()

print("Персонаж, содержащий в имени rick вида неизвестный")
url = f"https://rickandmortyapi.com/api/character/?name=rick&'species': 'unknown'"
response = requests.get(url)
print(response.json())
print()

# Примеры для /location

print("Случайная локация из всех")
url = f"https://rickandmortyapi.com/api/location/{random.randint(1, 126)}"
response = requests.get(url)
print(response.json())
print()

print("Локация типа планета ")
url = f"https://rickandmortyapi.com/api/location/?type=planet"
response = requests.get(url)
print(response.json())
print()

# Примеры для /episode

print("Последний эпизод, 51-ый")
url = f"https://rickandmortyapi.com/api/episode/51"
response = requests.get(url)
print(response.json())
print()

# Не только получение всей информации в json, но и ее обработка
print("Эпизоды пятого сезона:")
url = f"https://rickandmortyapi.com/api/episode/?episode=S05"
response = requests.get(url)
data = response.json()['results']
for i in data:
    print(i['name'])
