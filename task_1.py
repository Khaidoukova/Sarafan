# 1. Напишите программу, которая выводит n первых элементов последовательности 122333444455555…
# (число повторяется столько раз, чему оно равно).
# Данное задание можно решить двумя способами:
# Способ №1 (через генератор)

def generate_row(n: int):
    i = 1
    count = 1
    while count <= n:
        for _ in range(i):
            yield i
        count += 1

        i += 1


# Способ №2 (без генератора)

def generate_raw_2(n: int):
    raw = []
    for i in range(1, n + 1):
        raw.extend([i] * i)
        i += 1
    return raw


if __name__ == "__main__":
    n = int(input("Введите нужное количество элементов последовательности: "))
    raw1 = generate_row(n)
    lst = []
    while True:
        try:
            lst.append(next(raw1))
        except StopIteration:
            break
    print(lst)
    result2 = generate_raw_2(n)
    print(result2)
