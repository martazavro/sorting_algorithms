'''
This module contains Insertion, Merge, Selection and Shell sorting algorithms.
'''

def insertion_sort(array):
    '''
    The function implements the insertion sorting algorithm.
    '''
    counter = 0
    for i in range(1, len(array)):  
        j = i - 1 
        value = array[i]   
        flag = True
        while j >= 0 and value < array[j]:  
            array[j + 1] = array[j]  
            j -= 1  
            counter += 1
            flag = False
        array[j + 1] = value  
        if flag: 
            counter += 1
    return counter


def merge_sort(array):
    '''
    The function
    implements the merge sorting algorithm. Must return a sorted array.
    '''
    counter = 0
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        merge_sort(left)
        merge_sort(right)
        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            counter += 1
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        counter += 1

        while i < len(left):
            counter += 1
            array[k] = left[i]
            i += 1
            k += 1
        counter += 1

        while j < len(right):
            counter += 1
            array[k] = right[j]
            j += 1
            k += 1
        counter += 1
    return counter


def selection_sort(array):
    '''
    The function implements the selection sorting algorithm.
    '''
    counter = 0
    for i in range(len(array)):
        min_idx = i
        for j in range(i+1, len(array)):
            counter += 1
            if array[min_idx] > array[j]:
                min_idx = j

        array[i], array[min_idx] = array[min_idx], array[i]

    return counter


def shell_sort(array):
    '''
    The function implements the Shell sorting algorithm.
    '''
    interval = len(array) // 2
    counter = 0
    while interval > 0:
        for i in range(interval, len(array)):
            current = array[i]
            j = i
            while j >= interval and j >= 0 and array[j - interval] > current:
                array[j] = array[j - interval]
                j -= interval
                counter +=1
            array[j] = current
            if j - interval >= 0:
                counter += 1
        interval //= 2
    return counter