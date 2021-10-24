import json
import re


class File:
    """
    Класс File для чтения из текстового файла

    Attributes
    ----------
    __data : list
        Содержит список считанных данных из текстового файла
    """
    def __init__(self, filepath: str) -> None:
        """
        Инициализирует класс данных, считанных из файла

        Parameters
        -----------
          filepath: str
             Указывает путь к файлу с данными, которые необходиммо считать
        """
        try:
            with open(filepath, encoding='windows-1251') as path:
                self.__data = json.load(path)
        except BaseException:
            print("Файл имеет неверный формат данных или файла по данному пути не найдено")

    @property
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
    Класс Validator содержит статистику правильных и неправильных записей
    Объект класса Validator проверяет правильность считанных данных
    ----------
    Class Attributes
    ----------
    _valid_records:int
        Содержит количество правильных записей
    _invalid_email:int
        Содержит количество записей с ошибкой в email
    _invalid_height:int
        Содержит количество записей с ошибкой в height
    _invalid_snils:int
        Содержит количество записей с ошибкой в snils
    _invalid_passport_number:int
        Содержит количество записей с ошибкой в passport_number
    _invalid_occupation:int
        Содержит количество записей с ошибкой в occupation
    _invalid_age:int
        Содержит количество записей с ошибкой в age
    _invalid_political_views:int
        Содержит количество записей с ошибкой в political_views
    _invalid_worldview:int
        Содержит количество записей с ошибкой в worldview
    _invalid_address:int
        Содержит количество записей с ошибкой в address
    ----------
    Object Attributes
    ----------
    __email : str
        Содержит email
    __height : str
        Содержит рост
    __snils : str
        Содержит номер СНИЛС
    __passport_number : str
        Содержит номер паспорта
    __occupation : str
        Содержит профессию
    age:str
        Содержит возраст
    political_views:str
        Содержит политические взгляды
    worldview:str
        Содержит мировоззрение
    address:str
        Содержит адрес
    """

    _valid_records = 0
    _invalid_email = 0
    _invalid_height = 0
    _invalid_snils = 0
    _invalid_passport_number = 0
    _invalid_occupation = 0
    _invalid_age = 0
    _invalid_political_views = 0
    _invalid_worldview = 0
    _invalid_address = 0

    def __init__(self, email: str, height: str, snils: str, passport_number: str, occupation: str,
                 age: str, political_views: str, worldview: str, address: str) -> None:
        """
        Инициализирует объект класса Validator для последующих проверок в методах
        Parameters:
        -----------
        :param email:str
        email человека
        :param height:str
        рост человека
        :param snils:str
        СНИЛС человека
        :param passport_number:str
        номер паспорта человека
        :param occupation:str
        Профессия человека
        :param age:str
        Возраст человека
        :param political_views:str
        Политические взгляды человека
        :param worldview:str
        Мировоззрение человека
        :param address:str
        Адрес человека
        """
        self.__email = email
        self.__height = height
        self.__snils = snils
        self.__passport_number = passport_number
        self.__occupation = occupation
        self.__age = age
        self.__political_views = political_views
        self.__worldview = worldview
        self.__address = address

    def __is_email_correct(self) -> bool:
        """
        Проверяет email, записанный в объекте класса Validator, на корректность
        :return:
            bool
                True, если email записан корректно
                False, если email некорректен
        """
        if re.match(r"^[\w.]+@(\w+\.[^.;,])\w+$", self.__email) is None:
            return False
        return True

    def __is_height_correct(self) -> bool:
        """
        Проверяет height, записанный в объекте класса Validator, на корректность
        :return:
            bool
                True, если height записан корректно
                False, если height некорректен
        """
        if re.match(r"^[0-9]+\.[0-9]+$", self.__height) is None:
            return False
        return True

    def __is_snils_correct(self) -> bool:
        """
        Проверяет snils, записанный в объекте класса Validator, на корректность
        :return:
            bool
                True, если snils записан корректно
                False, если snils некорректен
        """
        if re.match(r"^\d{11}$", self.__snils) is None:
            return False
        return True

    def __is_passport_number_correct(self) -> bool:
        """
        Проверяет passport_number, записанный в объекте класса Validator, на корректность
        :return:
            bool
                True, если passport_number записан корректно
                False, если passport_number некорректен
        """
        if re.match(r"^\d{6}$", self.__passport_number) is None:
            return False
        return True

    def __is_occupation_correct(self) -> bool:
        """
        Проверяет occupation, записанный в объекте класса Validator, на корректность
        :return:
            bool
                True, если occupation записан корректно
                False, если occupation некорректен
        """
        if re.match(r"^([А-яA-z]+[-]?\s?)+$", self.__occupation) is None:
            return False
        return True

    def __is_age_correct(self) -> bool:
        """
        Проверяет age, записанный в объекте класса Validator, на корректность
        :return:
            bool
                True, если age записан корректно
                False, если age некорректен
        """
        if re.match(r"^[0-9]{1,3}$", self.__age) is None:
            return False
        return True

    def __is_political_views_correct(self) -> bool:
        """
        Проверяет political_views, записанный в объекте класса Validator, на корректность
        :return:
            bool
                True, если political_views записан корректно
                False, если political_views некорректен
        """
        if re.match(r"^([А-яA-z]+[-]?\s?)+$", self.__political_views) is None:
            return False
        return True

    def __is_worldview_correct(self) -> bool:
        """
        Проверяет worldview, записанный в объекте класса Validator, на корректность
        :return:
            bool
                True, если worldview записан корректно
                False, если worldview некорректен
        """
        if re.match(r"^([А-яA-z]+[-]?\s?)+$", self.__worldview) is None:
            return False
        return True

    def __is_address_correct(self) -> bool:
        """
        Проверяет address, записанный в объекте класса Validator, на корректность
        address считается корректным лишь тогда, когда он записан по формату:
        "ул. <название улицы> <номер дома>"

        :return:
            bool
                True, если address записан корректно
                False, если address некорректен
        """
        if re.match(r"^ул\.\s[\w .-]+\d+$", self.__address) is None:
            return False
        return True

    def is_record_correct(self) -> None:
        """
        Проверяет полностью запись в объекте класса Validator, на корректность

        В случае нахождения ошибки, соответствующий атрибут класса Validator увеличивается на 1
        После нахождения ошибки проверка сразу же завершается после увеличения атрибута

        В случае, если ошибок не найдено, атрибут класса Validator _valid_records увеличивается на 1
        """
        if not self.__is_email_correct():
            Validator._invalid_email += 1
        elif not self.__is_height_correct():
            Validator._invalid_height += 1
        elif not self.__is_snils_correct():
            Validator._invalid_snils += 1
        elif not self.__is_passport_number_correct():
            Validator._invalid_passport_number += 1
        elif not self.__is_occupation_correct():
            Validator._invalid_occupation += 1
        elif not self.__is_age_correct():
            Validator._invalid_age += 1
        elif not self.__is_political_views_correct():
            Validator._invalid_political_views += 1
        elif not self.__is_worldview_correct():
            Validator._invalid_worldview += 1
        elif not self.__is_address_correct():
            Validator._invalid_address += 1
        else:
            Validator._valid_records += 1

    @staticmethod
    def print_statistics() -> None:
        """
        Выводит статистику о правильных записях и найденных ошибках
        """
        print("Статистика о валидации:")
        print(f"Верных записей: {Validator._valid_records}")
        print(f"Ошибок в email: {Validator._invalid_email}")
        print(f"Ошибок в height: {Validator._invalid_height}")
        print(f"Ошибок в snils: {Validator._invalid_snils}")
        print(f"Ошибок в passport_number: {Validator._invalid_passport_number}")
        print(f"Ошибок в _invalid_occupation: {Validator._invalid_occupation}")
        print(f"Ошибок в age: {Validator._invalid_age}")
        print(f"Ошибок в political_views: {Validator._invalid_political_views}")
        print(f"Ошибок в worldview: {Validator._invalid_worldview}")
        print(f"Ошибок в address: {Validator._invalid_address}")


file = File("C:\\Users\\Altryd\\Downloads\\91.txt")
for record in file.data:
    validate = Validator(str(record['email']), str(record['height']), str(record['snils']),
                         str(record['passport_number']), str(record['occupation']), str(record['age']),
                         str(record['political_views']), str(record['worldview']), str(record['address']))
    validate.is_record_correct()
Validator.print_statistics()
