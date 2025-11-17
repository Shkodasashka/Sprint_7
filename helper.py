import allure
import random
import string


class Createnewcourier:
    @staticmethod
    @allure.step('Генерация данных для нового курьера')
    def create_new_courier():
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
            }
        return payload


class ChangeTestData:
    @staticmethod
    @allure.step('Замена данных поля на пустое значение')
    def change_data_field_on_empty(testdata, key):
        data = testdata.copy()
        data[key] = ""
        return data

    @staticmethod
    @allure.step('Внесение ошибки в данные поля зарегестрированного пользователя')
    def input_mistake_in_field_of_registred_user(testdata, key):
        data = testdata.copy()
        data[key] = data[key] + str(random.randint(0, 9))
        return data

    @staticmethod
    @allure.step('Замена значения ключа в словаре заказа')
    def change_value_of_key_in_dictionary_order(testdata, key, value):
        data = testdata.copy()
        data[key] = value
        return data

    @staticmethod
    @allure.step('Генерация новых данных курьера с использованием логина уже зарегестрированного')
    def create_data_with_existing_login(existing_login):
        new_data = Createnewcourier.create_new_courier()
        new_data['login'] = existing_login
        return new_data
