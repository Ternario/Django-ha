from pydantic import BaseModel, EmailStr, conint, constr, field_validator, model_validator
import json


class Address(BaseModel):
    city: constr(min_length=2)
    street: constr(min_length=3)
    house_number: conint(gt=0)


class User(BaseModel):
    name: str
    age: conint(ge=0, le=120)
    email: EmailStr
    is_employed: bool
    address: Address

    @staticmethod
    @field_validator('name')
    def validate_name(value):
        if len(value) < 2 or not value.isalpha():
            raise ValueError('Name must be at least 2 characters long and contain only letters.')
        return value.title()

    @staticmethod
    @model_validator(mode='before')
    def validate_age(values):
        age = values.get('age')
        is_employed = values.get('is_employed')
        if is_employed and age < 18:
            raise ValueError('Employed users must be at least 18 years old.')
        return values

    @staticmethod
    @field_validator('email')
    def validate_email(value):
        if not value.endswith('.com'):
            raise ValueError('Email must end with .com')
        return value


def process_user_json(string: str) -> str:
    try:
        user = User.parse_raw(string)
        return user.json()
    except (ValueError, json.JSONDecodeError) as e:
        return json.dumps({"error": str(e)})


valid_json = json.dumps({
    "name": "Alex",
    "age": 24,
    "email": "alex@example.com",
    "is_employed": True,
    "address": {
        "city": "Berlin",
        "street": "Berlinerplatz",
        "house_number": 15
    }
})

age_error_json = json.dumps({
    "name": "Alina",
    "age": 15,
    "email": "alina@example.com",
    "is_employed": True,
    "address": {
        "city": "Hannover",
        "street": "Alexanderplatz",
        "house_number": 1
    }
})

email_error_json = json.dumps({
    "name": "Maks",
    "age": 35,
    "email": "maks@examplecom",
    "is_employed": False,
    "address": {
        "city": "Hamburg",
        "street": "Reeperbahn",
        "house_number": 1
    }
})

address_error_json = json.dumps({
    "name": "Aniya",
    "age": 29,
    "email": "aniya@example.com",
    "is_employed": True,
    "address": {
        "city": "Bremen",
        "street": "A",
        "house_number": 6
    }
})

print("Valid JSON Response:")
print(process_user_json(valid_json))

print("\nAge Error JSON Response:")
print(process_user_json(age_error_json))

print("\nEmail Error JSON Response:")
print(process_user_json(email_error_json))

print("\nAddress Error JSON Response:")
print(process_user_json(address_error_json))
