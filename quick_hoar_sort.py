"""Сортировка Тонни Хоара"""


def hoar_sort(A):
    if len(A) <= 1:
        return
    barrier = A[0]
    L = []
    R = []
    M = []
    for x in A:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else:
            R.append(x)
    hoar_sort(L)
    hoar_sort(R)
    k = 0
    for x in L + M + R:
        A[k] = x
        k += 1
    return A


A = [2, 4, 7, 1, 3, 5, 6]
print(hoar_sort(A))


"""Проверка отсорированности за О(len(A))"""


def check_sorted(A, ascending=True):
    flag = True
    N = len(A)
    s = 2 * int(ascending) - 1
    for i in range(0, N-1):
        if s * A[i] > s * A[i+1]:
            flag = False
            break
    return flag


A = [1, 2, 3, 4, 5, 6, 7]
print(check_sorted(A))
