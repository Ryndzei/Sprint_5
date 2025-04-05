import random

def random_login():
    name = 'anton'
    surname = 'rineyskiy'
    cohort = '19'
    random_digits = random.randint(100, 999)
    login = name + surname + cohort + str(random_digits) + "@yandex.ru"
    return login

def random_password():
    password = random.randint(100000, 999999)
    return password