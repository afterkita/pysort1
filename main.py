from random import randint

#Сортировка методом прочёсывания
def sort1(arr):
    ##print(arr)
    n = len(arr)
    p = n
    while p > 1 or q:
        q = False
        if p > 1:
            p -= 3
        i = 0
        while i + p < n:
            if arr[i] > arr[i + p]:
                arr[i], arr[i + p] = arr[i + p], arr[i]
                q = True
            i += p
    return arr

#Сортировка вставками
def sort2(arr):
    n = len(arr)
    new_arr = [arr[0]]
    for i in range(1, len(arr)):
        ##print(i , new_arr)
        q = False
        for j in range(0, len(new_arr)):
            if arr[i] <= new_arr[j]:
                new_arr.insert(j, arr[i])
                q = True
                break
        if q == False:
            new_arr.append(arr[i])
    return new_arr
#Сортировка вставками
def sort3(arr):
    n = len(arr)
    last = n
    for i in range(last, 1, -1):
        g = arr[0]
        gi = 0
        for j in range(1,n):
            if g <= arr[j]:
                g = arr[j]
                gi = j
            if j == i:
                arr[i], arr[gi] = arr[gi], arr[i]
                break
    return arr
#Сортировка шела с выбором центрального элемента
def sort4(arr):
    n = len(arr)
    last = n//2
    while last > 0:
        for i in range(last, n):
            j = i
            o = j - last
            while o >= 0 and arr[o] > arr[j]:
                arr[o], arr[j] = arr[j], arr[o]
                j = o
                o = j - last
        last //= 2
    return arr

arr_1 = [randint(1,100) for a in range(10)]
print(arr_1)
print(sort1(arr_1),  'Comb sort')
arr_2 = [randint(1,100) for a in range(10)]
print(arr_2)
print(sort2(arr_2), 'Insertion sort')
arr_3 = [randint(1,100) for a in range(10)]
print(arr_3)
print(sort3(arr_3), 'Selection sort')
arr_4 = [randint(1,100) for a in range(10)]
print(arr_4)
print(sort4(arr_4), 'Shell sort')
