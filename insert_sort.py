# coding: utf-8

def insert_sort(arr):

    n = len(arr)
    if n == 1:
        return arr

    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j-1], arr[j] = arr[j], arr[j-1]

    return arr


if __name__=="__main__":
    a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
    print insert_sort(a)