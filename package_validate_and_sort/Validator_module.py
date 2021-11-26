import json
import re
import os
from tqdm import tqdm
import argparse
import pickle


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
        with open(filepath, encoding='windows-1251') as path:
            self.__data = json.load(path)

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
    _processed_records:int
        Содержит количество обработанных записей
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
    world_view_dict : dict
        Словарь
            Ключ - определенный worldview
            Значение - количество записей с таким worldview
    political_views_dict : dict
        Словарь
            Ключ - определенный political_view
            Значение - количество записей с таким political_view
    occupation_dict : dict
        Словарь
            Ключ - определенный occupation
            Значение - количество записей с таким occupation
    count_of_all_records_in_dicts : int
        Количество всех записей во всех словарях (сумма значений во всех словарях)
    number_of_dict : int
        Количество словарей
    ----------
    Object Attributes
    ----------
    __email : str
        Содержит email
    __height : float
        Содержит рост
    __snils : str
        Содержит номер СНИЛС
    __passport_number : int
        Содержит номер паспорта
    __occupation : str
        Содержит профессию
    age:int
        Содержит возраст
    political_views:str
        Содержит политические взгляды
    worldview:str
        Содержит мировоззрение
    address:str
        Содержит адрес
    """

    _processed_records = 0
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
    world_view_dict = {}
    political_views_dict = {}
    occupation_dict = {}
    count_of_all_records_in_dicts = 0
    number_of_dict = 3

    def __init__(
            self,
            email: str,
            height: str,
            snils: str,
            passport_number: str,
            occupation: str,
            age: str,
            political_views: str,
            worldview: str,
            address: str) -> None:
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
        try:
            self.__height = float(height)
        except ValueError:
            self.__height = -1
        self.__snils = snils
        try:
            self.__passport_number = int(passport_number)
        except ValueError:
            self.__passport_number = 0
        self.__occupation = occupation
        try:
            self.__age = int(age)
        except ValueError:
            self.__age = -1
        self.__political_views = political_views
        self.__worldview = worldview
        self.__address = address

    def print_validator(self):
        print(f"email : {self.__email}  , heigth: {self.__height}")
        print(f"snils : {self.__snils}  , passport_number: {self.__passport_number}")
        print(f"occupation: {self.__occupation} age: {self.__age}")
        print(f"political_views: {self.__political_views} worldview: {self.__worldview}")
        print(f"address: {self.__address}", end='\n\n')

    def fill_political_views_dict(self) -> None:
        """
        Заполняет словарь political_views_dict
            Если ключа с таким __political_views не найдено, добавляет пару (__political_views:1)
            Если ключ найден, увеличивает значение на 1
        """
        if re.match(r"^([А-яA-z]+[-]?\s?)+$", self.__political_views) is None:
            return
        if self.__political_views in Validator.political_views_dict:
            Validator.political_views_dict[self.__political_views] += 1
            Validator.count_of_all_records_in_dicts += 1
        else:
            Validator.political_views_dict[self.__political_views] = 1
            Validator.count_of_all_records_in_dicts += 1

    def fill_world_view_dict(self) -> None:
        """
        Заполняет словарь world_view_dict
            Если ключа с таким __worldview не найдено, добавляет пару (__worldview:1)
            Если ключ найден, увеличивает значение на 1
        """
        if re.match(r"^([А-яA-z]+[-]?\s?)+$", self.__worldview) is None:
            return
        if self.__worldview in Validator.world_view_dict:
            Validator.world_view_dict[self.__worldview] += 1
            Validator.count_of_all_records_in_dicts += 1
        else:
            Validator.world_view_dict[self.__worldview] = 1
            Validator.count_of_all_records_in_dicts += 1

    def fill_occupation_view_dict(self) -> None:
        """
        Заполняет словарь occupation_dict
            Если ключа с таким __occupation не найдено, добавляет пару (__occupation:1)
            Если ключ найден, увеличивает значение на 1
        """
        if re.match(r"^([А-яA-z]+[-]?\s?)+$", self.__occupation) is None:
            return
        if self.__occupation in Validator.occupation_dict:
            Validator.occupation_dict[self.__occupation] += 1
            Validator.count_of_all_records_in_dicts += 1
        else:
            Validator.occupation_dict[self.__occupation] = 1
            Validator.count_of_all_records_in_dicts += 1

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
        if re.match(r"^[0-9]+\.[0-9]+$", str(self.__height)) is None:
            return False
        return 2.30 > self.__height > 1.00

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
        if re.match(r"^\d{6}$", str(self.__passport_number)) is None:
            return False
        return True

    def __is_occupation_correct(self) -> bool:
        """
        Проверяет occupation, записанный в объекте класса Validator, на корректность
        Корректность зависит от формы записи, а также от количества записей с таким occupation
        Если таких записей меньше определенного процента, то профессия считается некорректной
        :return:
            bool
                True, если occupation записан корректно
                False, если occupation некорректен
        """
        if re.match(r"^([А-яA-z]+[-]?\s?)+$", self.__occupation) is None:
            return False
        if Validator.occupation_dict[self.__occupation] < (Validator.count_of_all_records_in_dicts /
                                                           (700 * Validator.number_of_dict)):
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
        if re.match(r"^[0-9]{1,3}$", str(self.__age)) is None:
            return False
        return 14 < self.__age < 120

    def __is_political_views_correct(self) -> bool:
        """
        Проверяет political_views, записанный в объекте класса Validator, на корректность
        Корректность зависит от формы записи, а также от количества записей с таким political_views
        Если таких записей меньше определенного процента, то political_views считаются некорректным
        :return:
            bool
                True, если political_views записан корректно
                False, если political_views некорректен
        """
        if re.match(r"^([А-яA-z]+[-]?\s?)+$", self.__political_views) is None:
            return False
        if Validator.political_views_dict[self.__political_views] < (Validator.count_of_all_records_in_dicts /
                                                                     (100*Validator.number_of_dict)):
            return False
        return True

    def __is_worldview_correct(self) -> bool:
        """
        Проверяет worldview, записанный в объекте класса Validator, на корректность
        Корректность зависит от формы записи, а также от количества записей с таким worldview
        Если таких записей меньше определенного процента, то worldview считается некорректным
        :return:
            bool
                True, если worldview записан корректно
                False, если worldview некорректен
        """
        if re.match(r"^([А-яA-z]+[-]?\s?)+$", self.__worldview) is None:
            return False
        if Validator.world_view_dict[self.__worldview] < (Validator.count_of_all_records_in_dicts /
                                                          (100*Validator.number_of_dict)):
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
        if re.match(r"^[A-я.]+\s[\w .()-]+\d+$", self.__address) is None:
            return False
        return True

    def statistic_is_record_correct(self) -> bool:
        """
        Проверяет полностью запись в объекте класса Validator на корректность и обновляет статистику
        о обработанных записях а также возвращает информацию о корректности записи

        В случае нахождения ошибки, соответствующий атрибут класса Validator увеличивается на 1
        После нахождения ошибки проверка сразу же завершается после увеличения атрибута

        В случае, если ошибок не найдено, атрибут класса Validator _valid_records увеличивается на 1

        Во всех случаях атрибут класса Validator _processed_records увеличивается на 1
        :return:
            bool
                True, если запись корректна
                False, если в записи найдены ошибки
        """
        Validator._processed_records += 1
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
            return True
        return False

    def is_record_correct(self) -> bool:
        """
        Проверяет полностью запись в объекте класса Validator на корректность
        -----------
        :return:
            bool
                True, если запись корректна
                False, если в записи найдены ошибки
        """
        if (self.__is_email_correct() and self.__is_height_correct() and self.__is_snils_correct() and
                self.__is_passport_number_correct() and self.__is_occupation_correct() and
                self.__is_age_correct() and self.__is_political_views_correct() and self.__is_worldview_correct() and
                self.__is_address_correct()):
            return True
        return False

    @staticmethod
    def print_statistics() -> None:
        """
        Выводит статистику о правильных записях и найденных ошибках
        """
        print("\tОбщая статистика о валидации:")
        print(f"Верных записей: {Validator._valid_records}")
        print(
            f"Ошибочных записей: {Validator._processed_records-Validator._valid_records}")
        print("\tСтатистика по ошибкам:")
        print(f"Ошибок в email: {Validator._invalid_email}")
        print(f"Ошибок в height: {Validator._invalid_height}")
        print(f"Ошибок в snils: {Validator._invalid_snils}")
        print(
            f"Ошибок в passport_number: {Validator._invalid_passport_number}")
        print(f"Ошибок в occupation: {Validator._invalid_occupation}")
        print(f"Ошибок в age: {Validator._invalid_age}")
        print(
            f"Ошибок в political_views: {Validator._invalid_political_views}")
        print(f"Ошибок в worldview: {Validator._invalid_worldview}")
        print(f"Ошибок в address: {Validator._invalid_address}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Validator_module.py')
    parser.add_argument(
        '-i',
        '-input',
        type=str,
        help='Аргумент, указывающий путь к файлу, который требуется проверить на валидность',
        required=True,
        dest='file_input')
    parser.add_argument(
        '-o',
        '-output',
        type=str,
        help='Аргумент, указывающий путь к файлу, в который требуется записать валидные данные',
        required=True,
        dest='file_output')
    args = parser.parse_args()
    read_data_from = os.path.realpath(args.file_input)
    write_valid_data_to = os.path.realpath(args.file_output)
    try:
        file = File(read_data_from)
        with tqdm(file.data, desc='Заполняем словари мировоззрений, политических взглядов, профессий') as progressbar:
            with open(write_valid_data_to, mode='w', encoding='windows-1251') as write_to_file:
                for record in file.data:
                    validate = Validator(
                        str(
                            record['email']), str(
                            record['height']), str(
                            record['snils']), str(
                            record['passport_number']), str(
                            record['occupation']), str(
                                record['age']), str(
                                    record['political_views']), str(
                                        record['worldview']), str(
                                            record['address']))
                    validate.fill_political_views_dict()
                    validate.fill_world_view_dict()
                    validate.fill_occupation_view_dict()
                    progressbar.update(1)
        data_to_save = []
        with tqdm(file.data, desc='Проверяем записи на соответствие критериям и записываем их в файл') as progressbar:
            with open(write_valid_data_to, mode='wb') as write_to_file:
                for record in file.data:
                    validate = Validator(
                        str(
                            record['email']), str(
                            record['height']), str(
                            record['snils']), str(
                            record['passport_number']), str(
                            record['occupation']), str(
                                record['age']), str(
                                    record['political_views']), str(
                                        record['worldview']), str(
                                            record['address']))
                    if validate.statistic_is_record_correct():
                        record['height'] = float(record['height'])
                        data_to_save.append(record)
                    progressbar.update(1)
                pickle.dump(data_to_save, write_to_file)
        Validator.print_statistics()
    except BaseException as ex:
        print(ex)
        print("Произошла ошибка, проверьте пути к файлам")
