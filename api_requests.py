import requests
import allure
from data import Url, User, AdBody
import helpers


@allure.step('запрос на создание user')
def create_user(body):
    return requests.post(Url.CREATE_USER, data=body)

@allure.step('запрос на авторизацию пользователя')
def user_login():
    return requests.post(Url.USER_LOGIN, data=User.EXIST_USER)

@allure.step('получение токена')
def get_user_token():
        response = requests.post(Url.USER_LOGIN, data=User.EXIST_USER)
        return "Bearer " + response.json()["token"]["access_token"]

@allure.step('запрос на создание объявления')
def create_ad():
        body = helpers.create_ad_payload()
        headers = {"Authorization": get_user_token(),
                   "Content-Type": body.content_type}
        response = requests.post(Url.CREATE_AD, data=body, headers= headers)
        data = response.json()
        ad_id = data['id']
        return response, ad_id, headers

@allure.step('запрос на изменение объявления')
def edit_ad(ad_id, headers):
    patch_headers = {
        "Authorization": headers["Authorization"],
        "Content-Type": "application/json",
    }

    return requests.patch(f'{Url.UPDATE_AD}/{ad_id}', json=AdBody.UPDATE_AD_BODY, headers=patch_headers)

@allure.step('запрос на удаление объявления')
def delete_ad(ad_id, headers):
        return requests.delete(f'{Url.DELETE_AD}/{ad_id}', headers=headers)