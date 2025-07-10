from functools import wraps
import time

def count_iterations(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        wrapper.iterations = 0
        result = func(*args, **kwargs)
        count = getattr(func, 'iteratoins', 0)
        print(f'Кол-во итераций: {wrapper.iterations}, '
              f'число: {result},'
              f'\nфункция отработала за {round(time.time() - start, 2)}'
              f'\n----------------------------------')
        return result
    return wrapper


@count_iterations
def binary_search(arr: list, number: int) -> int:
    low = 0
    hign = len(arr) - 1

    while low <= hign:
        binary_search.iterations += 1

        mid = (low + hign) // 2
        if number == arr[mid]:
            return arr[mid]
        elif number > arr[mid]:
            low = mid + 1
        else:
            hign = mid - 1
    return -1


@count_iterations
def line_search(arr: list, number: int) -> int:
    for item in arr:
        line_search.iterations += 1
        if item == number:
            return item
    return -1





