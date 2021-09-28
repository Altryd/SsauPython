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
    directory_to_extract_to = 'C:\\Users\\Altryd\\Downloads\\lab1_python_borisychev'

    """
    arch_file = 'C:\\Users\\Altryd\\Downloads\\tiff-4.2.0_lab1.zip'  # путь к архиву
    os.mkdir("C:\\Users\\Altryd\\Downloads\\lab1_python_borisychev")
    needed_zip_file = zipfile.ZipFile(arch_file)
    needed_zip_file.extractall(directory_to_extract_to)
    needed_zip_file.close()

    # Получаем абсолютный путь до ЭТОГО Jupyter Notebook
    notebook_path = os.path.abspath("1lab.ipynb")
    # Получаем путь до файла test_text.txt, находящегося в той же директории
    test_text = os.path.join(os.path.dirname(notebook_path), "test_text.txt")
    print(test_text)
    """
    # Задание №2.1
    # Получить список файлов (полный путь) формата txt,
    # находящихся в directory_to_extract_to. Сохранить полученный список в txt_files
    txt_files = []
    for root, dirs, files in os.walk(directory_to_extract_to):
        for file in files:
            if file.endswith(".txt"):
                txt_files.append(os.path.join(root, file))
    # for text_file in txt_files:
        # print(text_file, end="\n")
    print(end="\n\n")
    for file in txt_files:
        target_file_data = open(file, 'rb').read()
        result = hashlib.md5(target_file_data).hexdigest()
        print(result)
    print(end="\n\n")
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
    # print(lines)


    for line in lines:
        # извлечение заголовков таблицы
        if counter == 0:
            # Удаление тегов
            #cleanr = re.compile('<.*?>')
            #headers = re.sub(cleanr, '!', line)
            # Извлечение списка заголовков
            #headers = re.findall("[А-я]+\s?", headers)
            #headers[-2] = headers[-2] + headers[-1]
            #headers.__delitem__(-1)
            headers = re.findall('([А-Яа-я]+ ?[А-Яа-я]*)+',line)
            print(headers)
            counter += 1
            continue

            # TODO
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
    for key in result_dct.keys():
        output.write(key)
        output.write(result_dct[key].__str__())
        output.write('\n')

    output.close()

    # Задание №6
    # Вывод данных на экран для указанного первичного ключа (первый столбец таблицы)
    target_country = input("Введите название страны: ")
    print(result_dct.__getitem__(target_country))
    """
    #задание1
    a = [1, 2, 5, 10, 15]
    b = [11, 22, 33, 66, 99]
    # for i in range(len(a)):
    # print(a[i],b[i])

    zipped_values = zip(a, b)
    zipped_list = list(zipped_values)

    print(zipped_list)
    print(type(zipped_list))
    print(type(zipped_list[0]))

    #задание 2
    testing = "авава"
    is_palindrome = True
    for i in range(len(testing)):
        if testing[i] != testing[len(testing)-1-i]:
            is_palindrome = False
    print("палиндром" if is_palindrome else "нет")

    #задание 2 вариант через другое
    a = "мадам"
    a == a[::-1]

    #задание 3
    seconds = int(input())
    days = seconds // 86400
    seconds %= 86400
    hours = seconds // (86400/24)
    seconds %= (86400/24)
    minutes = seconds // (86400/24/60)
    seconds %= (86400/24/60)
    print(days, hours, minutes, seconds, sep=' : ')

    #задание 9
    list_comprehensions = [i for i in range(100)]
    print (list_comprehensions)
    """
    """
    array = ['agfkd.,f', 'Qksdf;sb&..', 'asdoo*', 'bgf...d', 're54()kj[]].']
    counting_points = [array[i].count('.') for i in range(len(array))]
    print(counting_points)

    array_with_two_and_more_points = [array[i].count('.') if array[i].count('.')>=2  for i in range(len(array) )]
    N = int(input())
    A = [True]*(N+1)
    A[0] = A[1] = False
    for k in range(2, N):
        if A[k]:
            for m in range(2*k, N+1, k):
                A[m] = False
    print(A[N])
    print(A)
    """


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
