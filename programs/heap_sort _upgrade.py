#!usr/bin/env python3
# -*- coding: utf-8 -*-


import timeit
import matplotlib.pyplot as plt
import random
import numpy as np
from scipy.optimize import curve_fit
import heapq


def find_coeffs_bin(x, time):
    params, _ = curve_fit(n_log_n, np.array(x),
                          np.array(time))
    a, b = params
    return a, b


def n_log_n(x, a, b):
    return a*x*np.log(x) + b


def heapify(nums, n, i):
        end = n
        new = nums[i]
        child = 2*i + 1

        while child < end:
            right = child + 1

            if right < end and not nums[right] < nums[child]:
                child = right

            if nums[i] < nums[child]:
                nums[i] = nums[child]
                i = child
                child = 2*i + 1

            else:
                break

        nums[i] = new


def heap_sort_upgrade(nums):
    n = len(nums)
    heapq._heapify_max(nums)

    for i in range(n-1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i] 
        heapify(nums, i, 0)


def random_list(n):
    arr = []

    for i in range(1,n):
        arr.append(random.randint(0,500))

    return arr


def good_list(n):
    return [i for i in range(1,n)]


def bad_list(n):
    return [i for i in range(n-1,0, -1)]


if __name__ == "__main__":
    x = []
    heap_sort_bad = []
    heap_sort_rnd = []
    heap_sort_good = []

    for i in range(1,301):
        x.append(i)
        arr = random_list(i)
        sort_time = (timeit.timeit(lambda: heap_sort_upgrade(arr),
                                      number=50))/50
        heap_sort_rnd.append(sort_time)

        arr = bad_list(i)  
        sort_time = (timeit.timeit(lambda: heap_sort_upgrade(arr),
                                      number=50))/50
        heap_sort_bad.append(sort_time)

        arr = good_list(i)  
        sort_time = (timeit.timeit(lambda: heap_sort_upgrade(arr),
                                      number=50))/50
        heap_sort_good.append(sort_time)


    plt.figure(1)
    a, b = find_coeffs_bin(x, heap_sort_rnd)
    y = n_log_n(np.array(x), a, b)
    plt.plot(x, y, color='red')
    plt.title("Время сортировки при\n"+
              "заполнении массива рандомными элементами")
    plt.scatter(x,heap_sort_rnd,s=3)
    plt.xlabel('Размер массива')
    plt.legend([f"y = {a}*x*log(x)" +
                f" + ({b})"])
    plt.ylabel("Время сортировки массива")

    plt.figure(2)
    a, b = find_coeffs_bin(x, heap_sort_bad)
    y = n_log_n(np.array(x), a, b)
    plt.plot(x, y, color='red')
    plt.title("Время сортировки в\n"+
              "худшем случае")
    plt.scatter(x,heap_sort_bad,s=3)
    plt.xlabel('Размер массива')
    plt.legend([f"y = {a}*x*log(x)" +
                f" + ({b})"])
    plt.ylabel("Время сортировки массива")

    plt.figure(3)
    a, b = find_coeffs_bin(x, heap_sort_good)
    y = n_log_n(np.array(x), a, b)
    plt.plot(x, y, color='red')
    plt.title("Время сортировки\n"+
              " в лучшем случае")
    plt.scatter(x,heap_sort_good,s=3)
    plt.xlabel('Размер массива')
    plt.legend([f"y = {a}*x*log(x)" +
                f" + ({b})"])
    plt.ylabel("Время сортировки массива")

    plt.show()