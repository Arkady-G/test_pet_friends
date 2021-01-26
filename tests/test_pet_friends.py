from api import PetFriends
from settings import valid_email, valid_password, invalid_email, invalid_password, invalid_auth_key
import os

pf = PetFriends()


def test_get_api_key_for_user(email=valid_email, password=valid_password):
    """Вводим валидные email и password и проверяем наличие ключа API"""
    status, result = pf.get_api_key(email, password)

    # Проверяем соответствие ответа с ожидаемым результатом
    assert status == 200
    assert 'key' in result


def test_get_all_pets_with_valid_key(filter=''):
    """Вводим валидные email и password и получаем список питомцев"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    # Проверяем соответствие ответа с ожидаемым результатом
    assert status == 200
    assert len(result['pets']) > 0


def test_add_new_pet_with_valid_data(name='Барон', animal_type='кот', age='1', pet_photo='images/Maine_Coon_001.jpg'):
    """Проверяем добавление питомца"""
    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ API и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Проверяем соответствие ответа с ожидаемым результатом
    assert status == 200
    assert result['name']


def test_successfull_delete_self_pet():
    """Проверяем удаление пиомца по ID"""
    # Запрашиваем ключ auth_key и запрашиваем список моих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    # Проверяем список моих питомцев. Если список пустой - добавляем питомца и снова проверяем список моих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, 'Барон', 'кот', '1', 'images/Maine_Coon_001.jpg')
        _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    # Еще раз запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    # Проверяем статус ответа и отсутствие в списке id удаленного питомца
    assert status == 200
    assert pet_id not in my_pets.values()


def test_update_self_pet_with_valid_data(name='Баронесса', animal_type='Кошка', age='2'):
    """Проверяем возможность обновления информации о питомце"""
    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    # Проверяем список моих питомцев. Усли список пустой - добавляем питомца и снова проверяем список моих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, 'Барон', 'кот', '1', 'images/Maine_Coon_001.jpg')
        _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    status, result = pf.update_info_pet(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    # Проверяем статус ответа и имя питомца на соответствие заданному
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_without_photo_valid_data(name='Граф', animal_type='Кот', age='3'):
    """Проверяем добавление питомца без фотографии"""
    # Получаем ключ auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Проверяем соответствие ответа с ожидаемым результатом
    assert status == 200
    assert result['name']


def test_add_photo_pet_valid_data(pet_photo='images/Maine_Coon_001.jpg'):
    """Проверяем добавление фото питомца"""
    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    # Получаем ключ auth_key и запрашиваем список питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    # Проверяем список моих питомцев. если список пустой - добавляем питомца и снова проверяем список моих питомцев

    if len(my_pets['pets']) == 0:
        pf.add_new_pet_without_photo(auth_key, 'Гамлет', 'Кот', '3')
        _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    pet_id = my_pets['pets'][0]['id']
    status, result = pf.add_photo_pet(auth_key, pet_id, pet_photo)

    # Проверяем соответствие ответа с ожидаемым результатом
    assert status == 200
    assert result['pet_photo']
