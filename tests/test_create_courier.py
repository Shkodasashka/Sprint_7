from api.courier_api import CourierApi
from helper import Createnewcourier


class TestCreateCourier:
    def test_success_create_courier(self):
        create_courier_request = CourierApi.create_courier(Createnewcourier.create_new_courier())

        assert (create_courier_request.status_code == 201 and
                create_courier_request.json()['ok'] == True)
