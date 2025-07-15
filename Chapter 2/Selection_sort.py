import time


def time_polise(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{result}, {round(end - start, 3)}')
        return result
    return wrapper



@time_polise
def select_sort(arr: list) -> list:
    for i in range(len(arr)):
        min_index: int = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index: int = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

