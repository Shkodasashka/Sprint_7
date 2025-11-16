import allure
import pytest

from api.courier_api import CourierApi
from helper import Createnewcourier
from data import CourierData


class TestCourier:
    @allure.title('Проверка создания нового курьера')
    @allure.description('Проверка создания нового курьера при передаче в ручку /api/v1/courier логина, пароля и имени')
    def test_success_create_courier(self):
        create_courier_request = CourierApi.create_courier(Createnewcourier.create_new_courier())
        assert (create_courier_request.status_code == 201 and
                str(create_courier_request.json()['ok']) == 'True')

    @allure.title('Проверка невозможности создания двух курьеров с одинаковыми параметрами')
    @allure.description('Проверка невозможности создания двух курьеров при передаче в ручку /api/v1/courier одинаковых логина, пароля и имени')
    def test_unsuccess_create_two_identical_couriers(self):
        first_courier = Createnewcourier.create_new_courier()
        create_courier_request = CourierApi.create_courier(first_courier)
        create_courier_request_2 = CourierApi.create_courier(first_courier)       
        assert (create_courier_request_2.status_code == 409 and
                create_courier_request_2.json()['message'] == "Этот логин уже используется")

    @allure.title('Проверка невозможности создания курьера без обязательного поля')
    @allure.description('Проверка невозможности создания курьера при не передаче в ручку /api/v1/courier логина, пароля или имени')
    @pytest.mark.parametrize('param', ["login", "password", "firstName"])
    def test_unsuccess_create_couriers_without_required_param(self, param):
        data_courier = Createnewcourier.create_new_courier()
        data_courier[param] = ''
        create_courier_request = CourierApi.create_courier(data_courier)    
        assert (create_courier_request.status_code == 400 and
                create_courier_request.json()['message'] == "Недостаточно данных для создания учетной записи")

    @allure.title('Проверка невозможности создания двух курьеров с одинаковым логином')
    @allure.description('Проверка невозможности создания двух курьеров при передаче в ручку /api/v1/courier одинаковых логинов')    
    def test_unsuccess_create_courier_with_identical_logins(self):
        first_courier = Createnewcourier.create_new_courier()
        create_courier_request = CourierApi.create_courier(first_courier)
        second_courier = Createnewcourier.create_new_courier()
        second_courier['login'] = first_courier ['login']
        create_courier_request_2 = CourierApi.create_courier(second_courier)       
        assert (create_courier_request_2.status_code == 409 and
                create_courier_request_2.json()['message'] == "Этот логин уже используется")

    @allure.title('Проверка авторизации курьера в системе')
    @allure.description('Проверка авторизации курьера при передаче в ручку /api/v1/courier/login зарегестированных логина и пароля')
    def test_success_login_courier(self):
        login_courier_request = CourierApi.login_courier(CourierData.login_courier_body)
        assert (login_courier_request.status_code == 200 and
                login_courier_request.json()['id'] == 654347)

    @allure.title('Проверка невозможности авторизации курьера в системе без обязательного поля')
    @allure.description('Проверка невозможности авторизации курьера при не передаче в ручку /api/v1/courier логина или пароля')
    @pytest.mark.parametrize('param', ['login', 'password'])
    def test_unsuccess_login_courier_without_required_param(self, param):
        data_courier = CourierData.login_courier_body
        data_courier[param] = ''
        login_courier_request = CourierApi.login_courier(data_courier)
        assert (login_courier_request.status_code == 400 and
                login_courier_request.json()['message'] == "Недостаточно данных для входа")

    @allure.title('Проверка невозможности авторизации курьера в системе при вводе логина/пароля с ошибкой')
    @allure.description('Проверка невозможности авторизации курьера при передаче в ручку /api/v1/courier логина или пароля с ошибкой')
    @pytest.mark.parametrize('param', ['login', 'password'])
    def test_unsuccess_login_courier_with_mistake_in_field(self, param):
        data_courier = CourierData.login_courier_body
        data_courier[param] = str(data_courier[param]) + '4'
        login_courier_request = CourierApi.login_courier(data_courier)
        assert (login_courier_request.status_code == 404 and
                login_courier_request.json()['message'] == "Учетная запись не найдена") 

    @allure.title('Проверка невозможности авторизации курьера в системе при вводе незарегестрированных данных пароля/логина')
    @allure.description('Проверка невозможности авторизации курьера при передаче в ручку /api/v1/courier незарегестрированных логина или пароля')
    def test_unsuccess_login_courier_with_unregistred_data(self):
        login_courier_request = CourierApi.login_courier(CourierData.unregistred_courier_body)
        assert (login_courier_request.status_code == 404 and
                login_courier_request.json()['message'] == "Учетная запись не найдена")
