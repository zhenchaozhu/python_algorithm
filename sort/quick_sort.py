# coding: utf-8

def quick_sort(arr):

    less = []
    more = []
    pivot_arr = []

    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivot_arr.append(pivot)

            less = quick_sort(less)
            more = quick_sort(more)

        return less + pivot_arr + more


if __name__=="__main__":
    a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
    print quick_sort(a)