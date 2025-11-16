import allure
import pytest

from api.courier_api import OrderApi
from helper import ChangeTestData
from data import OrderData


class TestOrder:
    @allure.title('Проверка выбора цвета самоката при офорлмении заказа')
    @allure.description('Проверка создания нового заказа при передаче в ручку /api/v1/orders 2-х цветов самоката, одного и без цвета')
    @pytest.mark.parametrize("colour_scooter", [["BLACK"], ["GREY"], ["BLACK", "GREY"], [""]])
    def test_success_select_colour_in_order(self, colour_scooter):
        data_order = ChangeTestData.change_value_of_key_in_dictionary_order(OrderData.order_body, "color",colour_scooter)
        create_order_request = OrderApi.create_order(data_order)
        assert (create_order_request.status_code == 201 and
                'track' in create_order_request.json())
