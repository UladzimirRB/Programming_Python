def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return right  # значит элемент отсутствует, берем индекс ближайшего

    middle = (right + left) // 2  # находим середину
    if array[middle] == element:  # если элемент в середине,
        return middle
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # в противном случаи - в правой
        return binary_search(array, element, middle + 1, right)

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

while True:
    try:
        array = list(map(int, input("Введите список чисел через пробел: ").split()))
        break
    except ValueError:
        print('Это не число. Введите пожалуйста числа через пробел.')

array = qsort(array,0,len(array)-1)

element = int(input("Введите число чтобы найти индекс меньшего элемента и индекс больше или равного элемента: "))
print("Введенный масив: ", array)

# запускаем алгоритм на левой и правой границе
if element > array[0] and element <= array[len(array)-1]:
    if element in array:
        print(f"индекс числа меньшего чем {element} равен {(binary_search(array, element, 0, len(array) - 1))-1}")
        print(f"индекс числа больше или равного чем {element} равен {binary_search(array, element, 0, len(array) - 1)}")
    else:
        print(f"индекс числа меньшего чем {element} равен {binary_search(array, element, 0, len(array)-1)}")
        print(f"индекс числа больше или равного чем {element} равен {binary_search(array, element, 0, len(array) - 1) +1}")

if element == array[0]:
    print(f"введенное число является минимальным числом в списке, поэтому в списке нет числа меньшего чем он")

if element < array[0]:
    print(f"введенное число меньше минимального в списке")

if element > array[len(array)-1]:
    print(f"введенное число больше максимального в списке")
