# Set - неупорядоченный массив неповторяющихся элементов
s = {1, 2, None, 'print', 1, 2}
b = set('qwerty')  # разбивает строку на символы
c = set([1, 2, 3, 4, 5, 6, 7])  # разбивает список на элементы
s.add(4)  # добавляет элемент в список
c.update([5, 7, 9, 12])  # добавляет элементы списка в сет
c.discard(3)  # удаляет элемент
c.remove(5)  # удаляет элемент но ошибка если элемента нет
c.pop(5) # выводит элемент и одновременно удаляет его
# сеты можно сравнивать друг с другом

# dict - словари, неупорядоченная коллекция с доступом по ключу
d = {
    1: 'one',
    2: 'two',
    3: 'three'
}
d1 = dict(four=4, five=5, six=6)  # только для ключей-строк
d2 = dict.fromkeys(['a', 'b', 'c', 'd'])  # передает ключи в создаваемый словарь,
d2 = dict.fromkeys(['a', 'b', 'c', 'd'], 10)  # можно также передать значение по умолчанию
d[5] = 'five' # новый ключ - новое значение

person = {}
s = 'Ivanov Ivan Ivanovich'
s1 = s.split()
person['first_name'] = s1[0]
person['name'] = s1[1]
# print(person)
# print(d.get(2)) # выводит значение ключа
# setdefault(key) - создает пару ключ-значение с None