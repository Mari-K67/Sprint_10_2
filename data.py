class Url: 
    MAIN_URL = "https://qa-desk.education-services.ru"
    CREATE_USER = f'{MAIN_URL}/api/signup'
    USER_LOGIN = f'{MAIN_URL}/api/signin'
    CREATE_AD = f'{MAIN_URL}/api/create-listing'
    UPDATE_AD = f'{MAIN_URL}/api/update-offer'
    DELETE_AD = f'{MAIN_URL}/api/listings'

class User:
    EXIST_USER = {
    "email": "fggf@mail.ru", 
    "password": "1234567"
    }

    USER_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NDIsImVtYWlsIjoiZmdnZkBtYWlsLnJ1IiwibmFtZSI6IlVzZXIiLCJpYXQiOjE3ODMyNTMxMDIsImV4cCI6MTc4MzMzOTUwMn0.eok7fv6Hwwk1tsdaytSsoLx5PPLJlRTKNoELObXwMQA"

class Responses: 
    CREATE_USER_TWICE_400 = {"statusCode": 400, "message": "Почта уже используется"}
    DELETE_AD_200 = {"message":"Объявление удалено успешно"}
    UPDATE_AD_401 = {"error": "Unauthorized", "statusCode": 401, "message": "Оффер не найден или у вас нет прав на его редактирование"}

class AdBody:
    city = [
        'Москва',
        'Санкт-Петербург',
        'Новосибирск',
        'Екатеринбург',
        'Нижний Новгород',
        'Казань'
    ]
    category = [
        'Авто',
        'Книги',
        'Садоводство',
        'Хобби',
        'Технологии'
    ]
    condition = [
        'Новый',
        'Б/У'
    ]

    UPDATE_AD_BODY = {
            'name': 'ТАК НАДО',
            'category': 'Книги',
            'condition': 'Новый',
            'city': 'Нижний Новгород',
            'description': 'HGHGHHGGHHHD',
            'price': 30999,
        }