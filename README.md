Тестовый проект к 19 модулю Задание 19.7.2.

В директории /tests располагается файл с тестами.

В директории /tests/images лежит картинка и файл для теста добавления питомца и теста добавления картинки.

В корневой директории лежит файл settings.py - содержит информацию о валидных и невалидных логинах и паролях и невалидный ключ API.

В корневой директории лежит файл api.py, который является библиотекой к REST api сервису веб приложения Pet Friends.

Библиотека api написана в классе, что соответствует принципам ООП и позволяет удобно пользоваться её методами.

При инициализации библиотеки объявляется переменная base_url которая используется при формировании url для запроса.

Методы имеют подробное описание.

Тесты проверяют работу методов используя api библиотеку.
