import pytest

from helper import Createnewcourier


@pytest.fixture(scope="function")
def create_courier_data():
    courier_payload = Createnewcourier.create_new_courier()
    return courier_payload
