# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import zipfile
    import os
    import hashlib
    import re
    import requests

    # директория извлечения файлов архива
    directory_to_extract_to = 'C:\\Users\\Altryd\\Downloads\\lab1_python_borisychev_'

    arch_file = 'C:\\Users\\Altryd\\Downloads\\tiff-4.2.0_lab1.zip'  # путь к архиву
    os.mkdir("C:\\Users\\Altryd\\Downloads\\lab1_python_borisychev_")
    needed_zip_file = zipfile.ZipFile(arch_file)
    needed_zip_file.extractall(directory_to_extract_to)
    needed_zip_file.close()

    # Задание №2.1
    # Получить список файлов (полный путь) формата txt,
    # находящихся в directory_to_extract_to. Сохранить полученный список в txt_files
    txt_files = []
    for root, dirs, files in os.walk(directory_to_extract_to):
        for file in files:
            if file.endswith(".txt"):
                txt_files.append(os.path.join(root, file))

    for file in txt_files:
        target_file_data = open(file, 'rb').read()
        result = hashlib.md5(target_file_data).hexdigest()
        print("filename:\t", file, "\thash:", result)

    target_hash = "4636f9ae9fef12ebd56cd39586d33cfb"
    target_file = ''  # полный путь к искомому файлу
    target_file_data = ''  # содержимое искомого файла
    for root, dirs, files in os.walk(directory_to_extract_to):
        for file in files:
            file_path = os.path.join(root, file)
            file_to_compare = open(file_path, 'rb').read()
            result = hashlib.md5(file_to_compare).hexdigest()
            if target_hash == result:
                target_file = os.path.abspath(file_path)
                target_file_data = open(target_file, 'r').read()

    print(target_file)
    print(target_file_data)

    # Задание №4
    # Ниже представлен фрагмент кода парсинга HTML страницы с помощью регулярных выражений.
    # Возможно выполнение этого задания иным способом (например, с помощью сторонних модулей).

    r = requests.get(target_file_data)

    result_dct = {}  # словарь для записи содержимого таблицы
    counter = 0

    # Получение списка строк таблицы
    lines = re.findall(r'<div class="Table-module_row__3TH83">.*?</div>.*?</div>.*?</div>.*?</div>.*?</div>', r.text)
    headers = []
    for line in lines:
        # извлечение заголовков таблицы
        if counter == 0:
            # Удаление тегов
            headers = re.findall('([А-Яа-я]+ ?[А-Яа-я]*)+', line)
            assert headers.__len__() == 4
            counter += 1
            continue
        # Удаление тегов
        temp = re.sub('<.*?>', ';', line)
        # Значения в таблице, заключенные в скобках, не учитывать. Для этого удалить скобки и символы между ними.
        temp = re.sub('\(.*?\)', '', temp)
        temp = temp.replace(u"\xa0", u'')
        # Замена последовательности символов ';' на одиночный символ
        temp = re.sub(';+', ';', temp)
        # Удаление символа ';' в начале и в конце строки
        temp = re.sub("^;*", '', temp)
        temp = re.sub(";$", '', temp)
        temp = re.sub(";Всего", 'Всего', temp)
        # Разбитие строки на подстроки
        tmp_split = re.split(";", temp)
        # Извлечение и обработка (удаление "лишних" символов) данных из первого столбца
        start_position = 0
        for i in tmp_split[0]:
            if i == " ":
                start_position = tmp_split[0].index(i)+2
                break
        country_name = tmp_split[0][start_position::]
        # Извлечение данных из оставшихся столбцов. Данные из этих столбцов
        # должны иметь числовое значение (прочерк можно заменить на -1).
        # Некоторые строки содержат пробелы в виде символа '\xa0'.
        col_val = []
        for i in range(1, 5, 1):
            if tmp_split[i].count('*') or tmp_split[i].count('_'):
                col_val.append(-1)
            else:
                col_val.append(int(tmp_split[i]))

        # Запись извлеченных данных в словарь
        result_dct[country_name] = {}
        result_dct[country_name][headers[0]] = col_val[0]
        result_dct[country_name][headers[1]] = col_val[1]
        result_dct[country_name][headers[2]] = col_val[2]
        result_dct[country_name][headers[3]] = col_val[3]

    # Задание №5
    # Запись данных из полученного словаря в файл
    output = open('C:\\Users\\Altryd\\Downloads\\lab1_python_borisychev\\data.csv', 'w')
    counter = 0
    headers_string = ';'.join(headers)
    for key in result_dct.keys():
        if counter == 0:
            headers_string = "Название страны;" + headers_string
            output.write(headers_string)
            output.write('\n')
            counter += 1
        output.write(key+';')
        col_values_string = ""
        for i in range(0, 4):
            col_values_string = col_values_string + str(result_dct[key][headers[i]]) + ';'
        output.write(col_values_string)
        output.write('\n')

    output.close()

    # Задание №6
    # Вывод данных на экран для указанного первичного ключа (первый столбец таблицы)
    target_country = input("Введите название страны: ")
    print(result_dct.__getitem__(target_country))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
