import pickle
import json
import package_validate_and_sort.Validator_module
from tqdm import tqdm


def key_value(some_list: list):
    return some_list[1]


def height_value(some_dict: dict):
    return some_dict['height']


def insertion_sort(list_to_sort: list, key_function) -> list:
    with tqdm(list_to_sort, desc='Сортируем считанные данные') as progressbar:
        for i in range(1, len(list_to_sort)):
            value = list_to_sort[i]
            j = i-1
            while j >= 0 and key_function(value) < key_function(list_to_sort[j]):
                list_to_sort[j+1] = list_to_sort[j]
                j -= 1
            list_to_sort[j+1] = value
            progressbar.update(1)
        progressbar.update(1)
    return list_to_sort


def read_valid_txt(file: str) -> list:
    with open(file, mode='rb') as read_from:
        _data = pickle.load(read_from)
        return _data


def serialize_data_to_pickle(data_to_serialize: list, path: str) -> None:
    with open(path, mode='wb') as write_to:
        pickle.dump(data_to_serialize, write_to)


def serialize_validators_to_pickle(data_list: list, file: str) -> None:
    data_to_serialize = []
    with tqdm(data_list, desc='Сериализуем данные в файл') as progressbar:
        for i in range(0, len(data_list)):
            elem = package_validate_and_sort.Validator_module.Validator(
                                                                        str(data_list[i]['email']),
                                                                        str(data_list[i]['height']),
                                                                        str(data_list[i]['snils']),
                                                                        str(data_list[i]['passport_number']),
                                                                        str(data_list[i]['occupation']),
                                                                        str(data_list[i]['age']),
                                                                        str(data_list[i]['political_views']),
                                                                        str(data_list[i]['worldview']),
                                                                        str(data_list[i]['address'])
                                                                        )
            data_to_serialize.append(elem)
            progressbar.update(1)
    serialize_data_to_pickle(data_to_serialize, file)


def serialize_validators_to_json(data_list: list, file: str) -> None:
    data_to_serialize = []
    with tqdm(data_list, desc='Сериализуем данные в файл JSON, преобразовываем классы в словари') as progressbar:
        for i in range(0, len(data_list)):
            data_to_serialize.append(data_list[i].__dict__)
            progressbar.update(1)
    with open(file, mode='w', encoding='utf-8') as fp:
        json.dump(data_to_serialize, fp, ensure_ascii=False, indent=1)


def deserialize_validators_from_pickle(file: str) -> list:
    with open(file, mode='rb') as read_from:
        data_deserialized = pickle.load(read_from)
        return data_deserialized
