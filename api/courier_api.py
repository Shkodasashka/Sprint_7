import requests
import allure

from curl import Url


class CourierApi:
    @staticmethod
    @allure.step('Отправка запроса на создание нового курьера')
    def create_courier(body):
        return requests.post(Url.create_courier, json=body)

    @staticmethod
    @allure.step('Отправка запроса на логин курьера в системе')
    def login_courier(body):
        return requests.post(Url.login_courier, json=body)

    @staticmethod
    @allure.step('Отправка запроса на удаление курьера из системы')
    def delete_courier(courier_id):
        return requests.delete(f"{Url.delete_courier}{courier_id}")

    @staticmethod
    @allure.step('Отправка запроса на получение ID курьера после логина')
    def get_courier_id(login_data):
        response = CourierApi.login_courier(login_data)
        if response.status_code == 200:
            return response.json().get('id')
        return None



class OrderApi:
    @staticmethod
    @allure.step('Отправка запроса на создание заказа')
    def create_order(body):
        return requests.post(Url.create_order, json=body)

    @staticmethod
    @allure.step('Отправка запроса на получение списка заказов')
    def get_list_order():
        return requests.get(Url.create_order)
