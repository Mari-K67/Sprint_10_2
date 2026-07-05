import pytest
import allure
import api_requests
import helpers
from data import Responses
#pytest tests/test_create_user.py

class TestCreateCourier:
    @allure.title('Успешное создание пользователя')
    @allure.description("""
                        1. запрос возвращает код ответа 201;
                        2. запрос возвращает user id;
                        3. запрос возвращает access_token
                        """)
    def test_create_user_succeed(self):
        response = api_requests.create_user(helpers.create_user_payload(email=None, password=None))
        assert response.status_code == 201
        assert "id" in response.text
        assert "access_token" in response.text

    @allure.title('Повторная регистрация пользователя')
    @allure.description("""
                        1. запрос возвращает код ответа 400;
                        2. запрос возвращает {"statusCode": 400, "message": "Почта уже используется"}
                        """)
    def test_create_two_identical_users(self):
        body = helpers.create_user_payload(email=None, password=None)
        api_requests.create_user(body)
        response_2 = api_requests.create_user(body)

        assert response_2.status_code == 400
        assert response_2.json() == Responses.CREATE_USER_TWICE_400