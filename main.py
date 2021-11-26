from package_validate_and_sort.Validator_module import Validator
from package_validate_and_sort.Validator_module import File
from package_validate_and_sort.Sort import *
import argparse
import os
import json


parser = argparse.ArgumentParser(description='Sort.py')
parser.add_argument(
    '-i',
    '-input',
    type=str,
    help='Аргумент, указывающий путь к файлу, который требуется отсортировать/проверить на валидность',
    required=True,
    dest='file_input')
parser.add_argument(
    '-o',
    '-output',
    type=str,
    help='Аргумент, указывающий путь к файлу, в который требуется записать обработанные данные',
    required=True,
    dest='file_output')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument(
    '-v'
    '-validate',
    type=str,
    help='Аргумент, показывающий, что необходимо проверить данные на корректность',
    dest='validate'
)
group.add_argument(
    '-s'
    '-sort',
    type=str,
    help='Аргумент, показывающий, что необходимо отсортировать данные',
    dest='sort'
)
parser.add_argument(
    '-c',
    '-count',
    type=int,
    help='Аргумент, показывающий, сколько записей, начиная с начала нужно отсортировать и поместить в новый файл',
    dest='count'
)
args = parser.parse_args()
read_data_from = os.path.realpath(args.file_input)
write_valid_data_to = os.path.realpath(args.file_output)
validate_flag = args.validate
sort_flag = args.sort
count = args.count

if sort_flag:
    try:
        data = read_valid_txt(read_data_from)
        if count:
            data = data[0:count]
        data = insertion_sort(data, height_value)
        serialize_validators_to_pickle(data, write_valid_data_to)
        data = deserialize_validators_from_pickle(write_valid_data_to)
        if write_valid_data_to.endswith('.txt'):
            write_valid_data_to = write_valid_data_to.removesuffix('.txt')
            write_valid_data_to = write_valid_data_to + '.json'
        serialize_validators_to_json(data_list=data, file=write_valid_data_to)
    except FileNotFoundError:
        print('Файл не найден, проверьте пути к файлам')
    except BaseException as ex:
        print(ex)
        print('Неизвестная ошибка, повторите попытку, перед этим проверив пути к файлам и формат записей в них')
    else:
        print("Программа успешно завершена")
elif validate_flag:
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
        with tqdm(file.data, desc='Проверяем записи на соответствие критериям и записываем их в файлы') as progressbar:
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
            if write_valid_data_to.endswith('.txt'):
                write_valid_data_to = write_valid_data_to.removesuffix('.txt')
                write_valid_data_to = write_valid_data_to + '.json'
            with open(write_valid_data_to, mode='w') as write_to_file:
                json.dump(data_to_save, write_to_file, ensure_ascii=False, indent=1)
        Validator.print_statistics()
    except BaseException as ex:
        print(ex)
        print("Произошла ошибка, проверьте пути к файлам")
else:
    raise SystemExit(1)
