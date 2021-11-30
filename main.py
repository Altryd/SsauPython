import argparse
import time
from multiprocessing import Pool


parser = argparse.ArgumentParser(description='dispersion.py')
parser.add_argument(
    '-f',
    '-first_number',
    type=int,
    help='Первое число',
    required=True,
    dest='first_number')
parser.add_argument(
    '-s',
    '-second_number',
    type=int,
    help='Второе число',
    required=True,
    dest='second_number')
parser.add_argument(
    '-t',
    '-third_number',
    type=int,
    help='Третье число',
    required=True,
    dest='third_number'
)
parser.add_argument(
    '-n',
    '-process_number',
    type=int,
    help='Количество процессов',
    required=True,
    dest='process_number'
)


def square(x: int or float) -> int or float:
    return x*x


def to_the_power(x: int or float, n: int) -> int or float:
    return x**n


def expected_math_value(list_of_numbers: list, list_of_possibilities: list, power_of_moment: int) -> float:
    mx = 0
    if len(list_of_numbers) != len(list_of_possibilities):
        raise ValueError('The length of lists are not equal')
    list_of_numbers = list(map(lambda x: x**power_of_moment, list_of_numbers))

    for i in range(len(list_of_numbers)):
        mx += list_of_numbers[i]*list_of_possibilities[i]
    return mx


def dispersion(list_of_numbers: list, list_of_possibilities: list) -> float:
    m2x = expected_math_value(list_of_numbers, list_of_possibilities, 2)
    mx2 = expected_math_value(list_of_numbers, list_of_possibilities, 1)**2
    return m2x - mx2


def expected_mx(list_of_numbers: list) -> float:
    sum_of_numbers = sum(list_of_numbers)
    return sum_of_numbers/len(list_of_numbers)


def minus_expected(x):
    return (x - expected_mx_) ** 2


args = parser.parse_args()
first_number = args.first_number
second_number = args.second_number
third_number = args.third_number
process_number = args.process_number
numbers = [first_number, second_number, third_number]
expected_mx_ = expected_mx(numbers)


if __name__ == '__main__':
    start_time = time.time()
    n = process_number
    print(f'Количество процессов:{n}')
    with Pool(n) as p:
        # print(p.map(lambda x: (x - expected_mx_)**2, [first_number, second_number, third_number]))
        res = p.map(minus_expected, numbers)
    result = sum(res)/len(res)

    print(f"Введенные числа: {first_number} , {second_number}, {third_number}")
    print(f'Дисперсия введенных чисел: {result}')
    print("--- Программа выполнена за: %s ---" % (time.time() - start_time))
