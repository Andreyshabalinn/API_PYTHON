import json

from requests import Response


class Checking():


    @staticmethod
    def check_status_code(response : Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print("Успешно, Статус код = " + str(response.status_code))
        else:
            print("Провал, Статус код = " + str(response.status_code))


    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("Все поля присутствуют")


    @staticmethod
    def check_json_value(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(field_name + " верен")

    @staticmethod
    def check_json_word(response: Response, field_name, word):
        check = response.json()
        check_info = check.get(field_name)
        if word in check_info:
             print("Слово " + word + " присутствует")
        else:
            print("Слово " + word + " отсутствует")