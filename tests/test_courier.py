import allure
import pytest

from api.courier_api import CourierApi
from helper import Createnewcourier, ChangeTestData
from data import CourierData


class TestCreateCourier:
    @allure.title('Проверка создания нового курьера')
    @allure.description('Проверка создания нового курьера при передаче в ручку /api/v1/courier логина, пароля и имени')
    def test_success_create_courier(self, create_courier_data):
        create_courier_request = CourierApi.create_courier(create_courier_data)
        assert (create_courier_request.status_code == 201 and
                create_courier_request.json() == CourierData.response_success_create_courier)

    @allure.title('Проверка невозможности создания двух курьеров с одинаковыми параметрами')
    @allure.description('Проверка невозможности создания двух курьеров при передаче в ручку /api/v1/courier одинаковых логина, пароля и имени')
    def test_unsuccess_create_two_identical_couriers(self, register_and_cleanup_courier):
        create_courier_request_2 = CourierApi.create_courier(register_and_cleanup_courier)
        assert (create_courier_request_2.status_code == 409 and
                create_courier_request_2.json()['message'] == CourierData.response_message_after_unsuccess_create_courier_with_registered_login)

    @allure.title('Проверка невозможности создания курьера без обязательного поля')
    @allure.description('Проверка невозможности создания курьера при не передаче в ручку /api/v1/courier логина, пароля или имени')
    @pytest.mark.parametrize("param", ["login", "password", "firstName"])
    def test_unsuccess_create_couriers_without_required_param(self, param, create_courier_data):
        create_courier_request = CourierApi.create_courier(ChangeTestData.change_data_field_on_empty(create_courier_data, param))
        assert (create_courier_request.status_code == 400 and
                create_courier_request.json()['message'] == CourierData.response_message_after_unsuccess_create_courier_without_param)

    @allure.title('Проверка невозможности создания двух курьеров с одинаковым логином')
    @allure.description('Проверка невозможности создания двух курьеров при передаче в ручку /api/v1/courier одинаковых логинов')    
    def test_unsuccess_create_courier_with_identical_logins(self,register_and_cleanup_courier):
        create_courier_request_2 = CourierApi.create_courier(ChangeTestData.create_data_with_existing_login(register_and_cleanup_courier['login']))
        assert (create_courier_request_2.status_code == 409 and
                create_courier_request_2.json()['message'] == CourierData.response_message_after_unsuccess_create_courier_with_registered_login)


class TestLoginCourier:
    @allure.title('Проверка авторизации курьера в системе')
    @allure.description('Проверка авторизации курьера при передаче в ручку /api/v1/courier/login зарегестированных логина и пароля')
    def test_success_login_courier(self):
        login_courier_request = CourierApi.login_courier(CourierData.login_courier_body)
        assert (login_courier_request.status_code == 200 and
                'id' in login_courier_request.json())

    @allure.title('Проверка невозможности авторизации курьера в системе без обязательного поля')
    @allure.description('Проверка невозможности авторизации курьера при не передаче в ручку /api/v1/courier логина или пароля')
    @pytest.mark.parametrize('param', ['login', 'password'])
    def test_unsuccess_login_courier_without_required_param(self, param):
        login_courier_request = CourierApi.login_courier(ChangeTestData.change_data_field_on_empty(CourierData.login_courier_body, param))
        assert (login_courier_request.status_code == 400 and
                login_courier_request.json()['message'] == CourierData.response_message_after_unsuccess_login_courier_without_param)

    @allure.title('Проверка невозможности авторизации курьера в системе при вводе логина/пароля с ошибкой')
    @allure.description('Проверка невозможности авторизации курьера при передаче в ручку /api/v1/courier логина или пароля с ошибкой')
    @pytest.mark.parametrize('param', ['login', 'password'])
    def test_unsuccess_login_courier_with_mistake_in_field(self, param):
        login_courier_request = CourierApi.login_courier(ChangeTestData.input_mistake_in_field_of_registred_user(CourierData.login_courier_body, param))
        assert (login_courier_request.status_code == 404 and
                login_courier_request.json()['message'] == CourierData.response_message_after_unsuccess_login_courier_with_unregistred_data)

    @allure.title('Проверка невозможности авторизации курьера в системе при вводе незарегестрированных данных пароля/логина')
    @allure.description('Проверка невозможности авторизации курьера при передаче в ручку /api/v1/courier незарегестрированных логина или пароля')
    def test_unsuccess_login_courier_with_unregistred_data(self):
        login_courier_request = CourierApi.login_courier(CourierData.unregistred_courier_body)
        assert (login_courier_request.status_code == 404 and
                login_courier_request.json()['message'] == CourierData.response_message_after_unsuccess_login_courier_with_unregistred_data)
