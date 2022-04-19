
# быстрая сортировка array по возрастанию
def qsort(array, left, right):
    middle = (left + right) // 2
    p = array[middle]
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)
    return array

# возвращает индекс элемента в списке s, который меньше x, а следующий за ним больше или равен x
# None - если таких нет
def el_find(s, x):
    res = None
    for i in range(len(s)):
        if s[i] >= x:
            if i == 0 or i == len(s)-1:
                break
            else:
                res = i-1
                break
    return res



while True:
    int_list = input('Введите последовательность чисел, разделенных пробелами: ')
    try:
        if not int_list:
            raise ValueError                         # если список пуст - вызываем исключение
        int_list = list(map(int, int_list.split()))  # делим строку, преобразуем в список чисел
        break
    except:
        print('Необходимо ввести числа!')

while True:
    x = input('Введите любое число: ')
    try:
        x = int(x)
        break
    except:
        print('Необходимо ввести число!')

print("Введенный список чисел: ", int_list)
int_list = qsort(int_list, 0, len(int_list)-1)
print("Отсортированный список чисел: ", int_list)

idx = el_find(int_list, x)
if idx is None:
    print('Элемента, удовлетворяющего условию, в списке нет')
else:
    print('Искомый индекс: ', idx)