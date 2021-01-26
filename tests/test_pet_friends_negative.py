from api import PetFriends
from settings import valid_email, valid_password, invalid_email, invalid_password, invalid_auth_key
import os

pf = PetFriends()


def test_get_api_key_for_user_invalid_email_negative(email=invalid_email, password=valid_password):
    """Вводим невалидный email и валидный password. Пробуем получить ключ API"""
    status, result = pf.get_api_key(email, password)

    # Проверяем соответствие ответа с ожидаемым результатом
    assert status == 403
    assert 'key' not in result


def test_get_api_key_for_user_invalid_password_negative(email=valid_email, password=invalid_password):
    """Вводим валидный email и невалидный password. Пробуем получить ключ API"""
    status, result = pf.get_api_key(email, password)

    # Проверяем соответствие ответа с ожидаемым результатом
    assert status == 403
    assert 'key' not in result


def test_get_all_pets_with_invalid_key_negative(filter=''):
    """Вводим невалидный ключ API и пробуем получить список питомцев"""
    status, result = pf.get_api_key(invalid_auth_key, filter)

    # Проверяем соответствие ответа с ожидаемым результатом
    assert status == 403
    assert 'pets' not in result


def test_add_new_pet_with_invalid_photo_negative(name='Милорд', animal_type='Кот', age='1', pet_photo='images/TestData-05.csv'):
    """Проверяем добавление питомца с pet_photo c расширением файла .csv"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ API и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Проверяем соответствие ответа с ожидаемым результатом
    assert status == 500
    assert 'pet_photo' not in result


def test_add_new_pet_without_photo_minus_age_negative(name='Граф', animal_type='Кот', age='-3'):
    """Пробуем добавить питомца. Возраст - отрицательное число"""
    # Получаем ключ API
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Проверяем соответствие ответа с ожидаемым результатом
    assert status == 500
    assert 'name' not in result


def test_add_new_pet_without_photo_incredible_age_negative(name='Граф', animal_type='Кот', age='1000'):
    """Пробуем добавить питомца. Возраст - 1000"""
    # Получаем ключ API
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Пробуем добавить питомца
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Проверяем соответствие ответа с ожидаемым результатом
    assert status == 500
    assert 'name' not in result


def test_add_new_pet_without_photo_symbol_age_negative(name='Граф', animal_type='Кот', age='%'):
    """Пробуем добавить питомца. Возраст - спецсимвол %."""
    # Получаем ключ API
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Пробуем добавить питомца
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Проверяем соответствие ответа с ожидаемым результатом
    assert status == 500
    assert 'name' not in result


def test_add_new_pet_without_photo_empty_field_age_negative(name='Милорд', animal_type='Кот', age=''):
    """Пробуем добавить питомца с незаполненным полем age."""
    # Получаем ключ API
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Пробуем добавить питомца
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Проверяем соответствие ответа с ожидаемым результатом
    assert status == 500
    assert 'name' not in result


def test_add_new_pet_without_photo_with_space_age_negative(name='Гамлет', animal_type='Кот', age='2 3'):
    """ Пробуем добавить питомца возраст указан числом с пробелом"""
    # Получаем ключ API
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Пробуем добавить питомца
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Проверяем соответствие результата с ожидаемым результатом
    assert status == 500
    assert 'name' not in result


def test_add_new_pet_without_photo_letters_age_negative(name='Гамлет', animal_type='Кот', age='полтора годика'):
    """Пробуем добавить питомца возраст указан словами"""
    # Получаем ключ API
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Пробуем добавить питомца
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Проверяем соответствие результата с ожидаемым результатом
    assert status == 500
    assert 'name' not in result
