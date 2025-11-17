class CourierData:
    login_courier_body = {
        "login": "ninjasus",
        "password": "1234"
    }
    unregistred_courier_body = {
        "login": "shufel",
        "password": "1997"
    }
    response_success_create_courier = {
        "ok": True
    }
    response_message_after_unsuccess_create_courier_with_registered_login = "Этот логин уже используется"
    response_message_after_unsuccess_create_courier_without_param = "Недостаточно данных для создания учетной записи"
    response_message_after_unsuccess_login_courier_without_param = "Недостаточно данных для входа"
    response_message_after_unsuccess_login_courier_with_unregistred_data = "Учетная запись не найдена"


class OrderData:
    order_body = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": []
    }
