import requests
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder


class PetFriends:
    def __init__(self):
        self.base_url = 'https://petfriends1.herokuapp.com/'

    def get_api_key(self, email: str, password: str) -> json:
        """ Метод отправляет запрос с указанием email и password к API сервера и возвращает статус ответа и результат -
        TOKEN с уникальным ключом пользователя в формате json """

        headers = {
            'email': email,
            'password': password
        }
        res = requests.get(self.base_url + 'api/key', headers=headers)
        status = res.status_code
        result = ''

        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def get_list_of_pets(self, auth_key: json, filter: str = '') -> json:
        """Метод отправляет запрос к API сервера и возвращает статус ответа  и результат в формате json со списком
        найденных по фильтру питомцев. Фильтр может иметь пустое значение для получения полного списка питомцевб либо
        'my_pets' - список собственных питомцев. """

        headers = {'auth_key': auth_key['key']}
        filter = {'filter': filter}

        res = requests.get(self.base_url + 'api/pets', headers=headers, params=filter)

        status = res.status_code
        result = ''

        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def add_new_pet(self, auth_key: json, name: str, animal_type: str, age: str, pet_photo: str) -> json:
        """Метод отправляет данные и создает нового питомца. Взвращает статус ответа и результат с данными нового
        питомца в формате json """

        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age,
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
            })
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}

        res = requests.post(self.base_url + 'api/pets', headers=headers, data=data)
        status = res.status_code
        result = ''

        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def delete_pet(self, auth_key: json, pet_id: str) -> json:
        """Метод отправляет запрос на удаление питомца по указанному ID и возвращает статус ответа сервера и
        результат в формате json с текстом об успешном удалении. """
        headers = {'auth_key': auth_key['key']}

        res = requests.delete(self.base_url + 'api/pets/' + pet_id, headers=headers)
        status = res.status_code
        result = ''

        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def update_info_pet(self, auth_key: json, pet_id: str, name: str, animal_type: str, age: str) -> json:
        """Метод отправляет запрос на сервер и обновляет данные питомца по указанному id, возвращает обновленные
        данные питомца result в формате json и статус ответа сервера. """
        headers = {'auth_key': auth_key['key']}

        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age}

        res = requests.put(self.base_url + 'api/pets/' + pet_id, headers=headers, data=data)
        status = res.status_code
        result = ''

        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def add_new_pet_without_photo(self, auth_key: json, name: str, animal_type: str, age: str) -> json:
        """Метод отправляет данные и создает нового питомца без фотографии. Возвращает статус ответа сервера и
        результат с данными нового питомца в формате json """

        data = {'name': name,
                'animal_type': animal_type,
                'age': age}

        headers = {'auth_key': auth_key['key']}

        res = requests.post(self.base_url + 'api/create_pet_simple', headers=headers, data=data)
        status = res.status_code
        result = ''

        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text

        return status, result

    def add_photo_pet(self, auth_key: json, pet_id: str, pet_photo: str) -> json:
        """Метод добавляет фото питомца по указанному id. Возвращает статус ответа сервера и результат в формате json"""

        data = MultipartEncoder(fields={
            'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
        })

        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}

        res = requests.post(self.base_url + 'api/pets/set_photo/' + pet_id, headers=headers, data=data)
        status = res.status_code
        result = ''

        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text

        return status, result




