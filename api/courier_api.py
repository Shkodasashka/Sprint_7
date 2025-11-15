import requests

from curl import Url


class CourierApi:
    @staticmethod
    def create_courier(body):
        return requests.post(Url.create_courier, body)
