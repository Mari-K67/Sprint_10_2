import random
import string
from faker import Faker
from requests_toolbelt import MultipartEncoder
from data import AdBody

def generate_random_string_EN(length=7):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string


#универсальный метод для создания body для create user  
def create_user_payload(**fields):
    email = (
        fields["email"]
        if ("email" in fields and fields["email"] is not None)
        else f"{generate_random_string_EN()}@mail.ru"
    )

    password = (
        fields["password"]
        if ("password" in fields and fields["password"] is not None)
        else generate_random_string_EN()
    )

    return {
        "email": email,
        "password": password,
        "submitPassword": password,
    }

#универсальный метод для создания body для ad  
def create_ad_payload():
    fake = Faker("la")

    category = random.choice(AdBody.category)
    condition = random.choice(AdBody.condition)
    city = random.choice(AdBody.city)

    ad_data = MultipartEncoder(
        fields={
            'name': fake.word(),
            'category': category,
            'condition': condition,
            'city': city,
            'description': fake.word(),
            'price': str(fake.random_int(min=10, max=10000)),
        }
    )
    return ad_data