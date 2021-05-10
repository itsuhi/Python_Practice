# -*- coding: utf-8 -*-
"""
Created on Sat May 30 09:20:08 2020

@author: henry
"""
import numpy as np


def Bubble_Sort(lst):
    offset = 0
    for n in range(len(lst)):
        for i in range(len(lst) - 1 - offset):
            index_1 = i
            index_2 = i + 1
            temp = lst[index_1]
            if lst[index_1] > lst[index_2]:
                lst[index_1] = lst[index_2]
                lst[index_2] = temp
        offset = offset + 1
    return lst


def insertion_sort(lst):
    for i in range(1, len(lst)):
        value = lst[i]
        temp = i
        while temp > 0 and lst[temp - 1] > value:
            lst[temp] = lst[temp - 1]
            temp = temp - 1
        lst[temp] = value
    return lst


def merge_sort(items):
    if len(items) <= 1:
        return items

    middle_index = len(items) // 2
    left_split = items[:middle_index]
    right_split = items[middle_index:]

    left_sorted = merge_sort(left_split)
    right_sorted = merge_sort(right_split)

    return merge(left_sorted, right_sorted)


def merge(left, right):
    result = []

    while left and right:
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)

    if left:
        result += left
    if right:
        result += right

    return result


def radix_sort(to_be_sorted):
    maximum_value = max(to_be_sorted)
    max_exponent = len(str(maximum_value))
    being_sorted = to_be_sorted[:]

    for exponent in range(max_exponent):
        position = exponent + 1
        index = -position

        digits = [[] for i in range(10)]

        for number in being_sorted:
            number_as_a_string = str(number)
            try:
                digit = number_as_a_string[index]
            except IndexError:
                digit = 0
            digit = int(digit)

            digits[digit].append(number)

        being_sorted = []
        for numeral in digits:
            being_sorted.extend(numeral)

    return being_sorted


my_list = [2, 7, 1, 6, 5, 3, 10, 9]
large_array = np.random.randint(0, 10000, 10000)
large_list = list(large_array)
# print(Bubble_Sort(my_list))
# print(insertion_sort(large_array))
print(merge_sort(large_list))
