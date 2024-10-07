def input_to_bits(string):
    # создаем список из 0 и 1 делим строку на отдельные символы
    # и отдельно работаем с каждым символом через map
    return list(map(int, list(string)))
# Возвращает список 0 и 1
def s(arr):
    # Вычисляет значения у s1, s2, s3.
    s1 = (arr[0] + arr[2] + arr[4] + arr[6]) % 2
    s2 = (arr[1] + arr[2] + arr[5] + arr[6]) % 2
    s3 = (arr[3] + arr[4] + arr[5] + arr[6]) % 2
    return (s1, s2, s3)
# Проверка на ошибки
def has_error(arr):
    return s(arr) != (0, 0, 0)
# Определяет индекс ошибки
def error_index(arr):
    return int(''.join(map(str, s(arr)[::-1])), 2)
# Изменяет индекс ошибки в название символа
def error_symbol(arr):
    return { 1: 'r1', 2: 'r2', 3: 'i1', 4: 'r3', 5: 'i2', 6: 'i3', 7: 'i4' }[error_index(arr)]
# Возвращает список информационных значений(битов)
def inf_bits(arr):
    return [arr[2], arr[4], arr[5], arr[6]]
# Заново изменяем список битов в строку
def make_result_message(bits):
    return ''.join(map(str, bits))
#Если есть ошибка исправляет в битах.
#Если ошибок нет или ошибка в контрольном бите (r1, r2, r3)
#просто возвращает информационные биты.
def fixed_message(arr):
    if not has_error(arr) or error_symbol(arr)[0] == 'r':
        return make_result_message(inf_bits(arr))
    ind = int(error_symbol(arr)[1]) - 1
    result = inf_bits(arr)
    result[ind] = (result[ind] + 1) % 2
    return make_result_message(result)

inp = input()
# ПРОВЕРЯЕМ ГДЕ БЫЛА ОШИБКА ДЛЯ ПРАВИЛЬНОГО ОТВЕТА
bits = input_to_bits(inp)
if has_error(bits):
    print(f'В сообщении ошибка!\nОшибка в символе {error_symbol(bits)}')
else:
    print('В сообщении нет ошибок!')
print(f'Правильное сообщение: {fixed_message(bits)}')
