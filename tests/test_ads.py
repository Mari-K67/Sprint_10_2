import pytest
import allure
import api_requests
import helpers
from data import Responses
#pytest tests/test_ads.py

class TestCreateCourier:
    @allure.title('Успешное создание объявления')
    @allure.description("""
                        1. запрос возвращает код ответа 201;
                        2. запрос возвращает id
                        """)
    def test_create_ad_succeed(self, created_ad_fixture):
        response = created_ad_fixture[0]

        assert response.status_code == 201
        assert "id" in response.text

    @allure.title('Успешное редактирование любого поля объявления')
    @allure.description("""
                        1. запрос возвращает код ответа 200;
                        2. запрос возвращает id
                        """)
    def test_edit_own_ad_succeed(self, created_ad_fixture):
        ad_id = created_ad_fixture[1]
        headers = created_ad_fixture[2]
        response = api_requests.edit_ad(ad_id, headers)

        assert response.status_code == 200

    @allure.title('Редактирование объявления, созданного не тем пользователем, под токеном которого производится редактирование')
    @allure.description("""
                        1. запрос возвращает код ответа 401;
                        2. запрос возвращает {'error': 'Unauthorized', "statusCode": 401, "message": "Оффер не найден или у вас нет прав на его редактирование"}
                        """)
    def test_edit_another_user_ad_succeed(self, created_ad_fixture):
        headers = created_ad_fixture[2]
        response = api_requests.edit_ad(37, headers)

        assert response.status_code == 401
        assert response.json() == Responses.UPDATE_AD_401

    @allure.title('Успешное удаление объявления')
    @allure.description("""
                        1. запрос возвращает код ответа 200;
                        2. запрос возвращает user id;
                        3. запрос возвращает access_token
                        """)
    def test_delete_ad_succeed(self, created_ad_fixture):
        ad_id = created_ad_fixture[1]
        headers = created_ad_fixture[2]
        response = api_requests.delete_ad(ad_id, headers)
        assert response.status_code == 200
        assert response.json() == Responses.DELETE_AD_200