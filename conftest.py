import pytest

from helper import Createnewcourier
from api.courier_api import CourierApi


@pytest.fixture(scope="function")
def create_courier_data():
    courier_payload = Createnewcourier.create_new_courier()
    return courier_payload


@pytest.fixture(scope="function")
def register_and_cleanup_courier():
    courier_data = Createnewcourier.create_new_courier()
    create_response = CourierApi.create_courier(courier_data)
    assert create_response.status_code == 201
    yield courier_data
    courier_id = CourierApi.get_courier_id(
        {"login": courier_data['login'], "password": courier_data['password']}
    )
    delete_response = CourierApi.delete_courier(courier_id)
    assert delete_response.status_code == 200
