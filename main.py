from package_validate_and_sort.Validator_module import Validator
from package_validate_and_sort.Sort import *


data = deserialize_validators_from_pickle(r'C:\Users\Altryd\PycharmProjects\FirstLab\valid_b.txt')
print(Validator.occupation_dict)
serialize_validators_to_pickle(data, r'C:\Users\Altryd\PycharmProjects\FirstLab\1710.txt')
data = deserialize_validators_from_pickle(r'C:\Users\Altryd\PycharmProjects\FirstLab\1710.txt')
serialize_validators_to_json(data_list=data, file=r'C:\Users\Altryd\PycharmProjects\FirstLab\1710.json')
