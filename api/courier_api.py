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


class OrderApi:
    @staticmethod
    @allure.step('Отправка запроса на создание заказа')
    def create_order(body):
        return requests.post(Url.create_order, json=body)
