import json
import re
import os


class File:
    """
    Класс File для чтения из текстового файла

    Attributes
    ----------
    __data : list
        Содержит список считанных данных из текстового файла
    """
    __data: list

    def __init__(self, filepath: str) -> None:
        """
        Инициализирует класс данных с файла

        Parameters
        -----------
          filepath: str
             Указывает путь к файлу с данными, которые необходиммо считать
        """
        try:
            self.__data = json.load(open(filepath, encoding='windows-1251'))
        except BaseException:
            print("Файл имеет неверный формат данных или файла по данному пути не найдено")

    def data(self) -> list:
        """
        Возвращает считанные данные, хранящиеся в __data

        Returns
        -------
            list:
                Данные, хранящиеся в __data
        """
        return self.__data


class Validator:
    """
    Объект класса Validator проверяет правильность считанных данных
    Attributes
    ----------
    __email : str
        Содержит email
    __height : str
        Содержит рост
    __snils : str
    __passport_number : str
    __occupation : str
    age:str
    political_views:str
     worldview:str
    address:str
    """
    __email: str
    __height: str
    __snils: str
    __passport_number: str
    __occupation: str
    __age: str
    __political_views: str
    __worldview: str
    __address: str

def is_email_correct(email):
    if re.match(r"^[\w.]+@(\w+\.[^.;,])\w+$", email) is None:
        return False
    return True


def is_height_correct(height):
    if re.match(r"^[0-9]+\.[0-9]+$", height) is None:
        return False
    return True


def is_snils_correct(height):
    if re.match(r"^\d{11}$", height) is None:
        return False
    return True


def is_passport_number_correct(passport_number):
    if re.match(r"^\d{6}$", passport_number) is None:
        return False
    return True


def is_occupation_correct(occupation):
    if re.match(r"^([А-яA-z]+[-]?\s?)+$", occupation) is None:
        return False
    return True


def is_age_correct(age):
    if re.match(r"^[0-9]{1,3}$", age) is None:
        return False
    return True


def is_political_views_correct(political_views):
    if re.match(r"^([А-яA-z]+[-]?\s?)+$", political_views) is None:
        return False
    return True


def is_worldview_correct(worldview):
    if re.match(r"^([А-яA-z]+[-]?\s?)+$", worldview) is None:
        return False
    return True


def is_address_correct(address):
    if re.match(r"^ул\.\s[\w .-]+\d+$", address) is None:
        return False
    return True


"""
path = 'C:\\Users\\Altryd\\Downloads\\91.txt'
data = json.load(open(path, encoding='windows-1251'))
print(is_email_correct("tenons2036@yahoo.com"))
for element in data:
    if not is_worldview_correct(element['worldview']):
        print(element)
"""
file = File("C:\\Users\\Altryd\\Downloads\\91.txt")
print(type(file.data()))




"""
     "email": "tenons2036@yahoo.com",
        "height": "1.58",
        "snils": "84442064798",
        "passport_number": 586167,
        "occupation": "Зоолог",
        "age": 29,
        "political_views": "Коммунистические",
        "worldview": "Секулярный гуманизм",
        "address": "Аллея Акулово 150"
    """