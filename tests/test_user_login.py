import pytest
import allure
import api_requests
import helpers
from data import Responses
#pytest tests/test_user_login.py

class TestUserLogin:
    @allure.title('Успешная авторизация ранее зарегистрированного пользователя')
    @allure.description("""
                        1. запрос возвращает код ответа 201;
                        2. запрос возвращает user id;
                        3. запрос возвращает access_token
                        """)
    def test_user_login_succeed(self):
        response = api_requests.user_login()
        assert response.status_code == 201
        assert "id" in response.text
        assert "access_token" in response.text