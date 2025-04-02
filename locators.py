from selenium.webdriver.common.by import By


# Регистрация
NAME_INPUT = (By.XPATH, './/fieldset[1]/div/div/input') # Поле ввода имени
EMAIL_INPUT = (By.XPATH, './/fieldset[2]/div/div/input') # Поле ввода email
PASSWORD_INPUT = (By.XPATH, './/fieldset[3]/div/div/input')  # Поле ввода пароля
REGISTER_BUTTON = (By.XPATH, './/button[text()="Зарегистрироваться"]')  # Кнопка регистрации
REGISTER_LINK = (By.XPATH, './/p[1]/a[@href="/register"]')  # Ссылка на регистрацию с формы входа
PASSWORD_ERROR = (By.XPATH, './/fieldset[3]/div/p[text()="Некорректный пароль"]')  # Сообщение об ошибке пароля

# Вход
LOGIN_EMAIL_INPUT = (By.XPATH, './/fieldset[1]/div/div/input[@name="name"]')  # Поле email для входа
LOGIN_PASSWORD_INPUT = (By.XPATH, './/fieldset[2]/div/div/input[@name="Пароль"]')  # Поле пароля для входа
LOGIN_BUTTON = (By.XPATH, './/button[text()="Войти"]')  # Кнопка входа
LOGIN_ACCOUNT_BUTTON = (By.XPATH, './/button[text()="Войти в аккаунт"]')  # Кнопка входа на главной
PERSONAL_CABINET_LINK = (By.XPATH, './/nav/a/p[text()="Личный Кабинет"]')  # Ссылка на личный кабинет
LOGIN_FROM_REGISTER = (By.XPATH, './/div/p/a[@href="/login"]')  # Кнопка входа на форме регистрации
LOGIN_FROM_RECOVERY = (By.XPATH, './/div/div/p/a[text()="Войти"]')  # Кнопка входа на форме восстановления

# Личный кабинет
LOGOUT_BUTTON = (By.XPATH, './/ul/li[3]/button')  # Кнопка выхода

# Конструктор
CONSTRUCTOR_LINK = (By.XPATH, './/li[1]/a/p[text()="Конструктор"]')  # Ссылка на конструктор
LOGO_LINK = (By.XPATH, './/nav/div/a[@href="/"]')  # Логотип Stellar Burgers
BUNS_SECTION = (By.XPATH, './/section[1]/div[1]/div[1]/span[text()="Булки"]')  # Раздел "Булки"
SAUCES_SECTION = (By.XPATH, './/section[1]/div[1]/div[2]/span[text()="Соусы"]')  # Раздел "Соусы"
FILLINGS_SECTION = (By.XPATH, './/section[1]/div[1]/div[3]/span[text()="Начинки"]')  # Раздел "Начинки"