import pickle
from Validator import Validator
from tqdm import tqdm


def key_value(some_list):
    return some_list[1]


def height_value(some_dict):
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
    return list_to_sort


def read_valid_txt(file: str) -> list:
    with open(file, mode='rb') as read_from:
        _data = pickle.load(read_from)
        return _data


def serialize_data(data_to_serialize: list, path: str) -> None:
    with open(path, mode='wb') as write_to:
        pickle.dump(data_to_serialize, write_to)


def serialize_validators(data_list: list, file: str) -> None:
    data_to_serialize = []
    with tqdm(data_list, desc='Сериализуем данные в файл') as progressbar:
        for i in range(0, len(data_list)):
            elem = Validator(str(data_list[i]['email']),
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
    serialize_data(data_to_serialize, file)


def deserialize_validators(file) -> list:
    with open(file, mode='rb') as read_from:
        data_deserialized = pickle.load(read_from)
        return data_deserialized


data = read_valid_txt(r"C:\Users\Altryd\PycharmProjects\FirstLab\valid_b.txt")
data = insertion_sort(data, height_value)
serialize_validators(data, r"C:\Users\Altryd\PycharmProjects\FirstLab\serialized_validators.txt")
# data = deserialize_validators(r"C:\Users\Altryd\PycharmProjects\FirstLab\serialized_validators.txt")
# for elem in data:
# elem.print_validator()
