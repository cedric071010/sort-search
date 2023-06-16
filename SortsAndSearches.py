import time
import random


def linear_search(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while high >= low:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


user_input = input(">")
while user_input.lower() != "q":

    if user_input.lower() == "n":
        input_numbers = input("Enter the elements of the array (space-separated)>")
        array = list(map(int, input_numbers.split()))
        user_input = input(">")

    if user_input.lower() == "p":
        print(f"array is {array}")
        user_input = input(">")

    elif user_input.lower() == "random number":
        r = int(input("numbers of number you want>"))
        array = [random.randint(1, 100000) for _ in range(r)]
        print(f"random numbers are {array}")
        user_input = input(">")
    elif user_input.lower() == "s":
        r = int(input("numbers of number you want>"))
        array = numbers = list(range(r, -1, -1))
        print(f"numbers are {array}")
        user_input = input(">")

    elif user_input.lower() == "linear search":
        target_number = int(input("target number>"))
        start_time = time.time()
        result = linear_search(array, target_number)
        end_time = time.time()
        if result != -1:
            print(f"The target number {target_number} is found at index {result}.")
        else:
            print(f"The target number {target_number} is not found in the array.")
        print(f"Time taken to linear search: {end_time - start_time} seconds")
        user_input = input(">")
    elif user_input.lower() == "binary search":
        target_number = int(input("target number>"))
        start_time = time.time()
        result = binary_search(array, target_number)
        end_time = time.time()
        if result != -1:
            print(f"The target number {target_number} is found at index {result}.")
        else:
            print(f"The target number {target_number} is not found in the array.")
        print(f"Time taken to binary search: {end_time - start_time} seconds")
        user_input = input(">")

    elif user_input.lower() == "bubble sort":
        start_time = time.time()
        bubble_sort(array)
        end_time = time.time()
        print(f"{array} is the bubble sort")
        print(f"Time taken to bubble sort: {end_time - start_time} seconds")
        user_input = input(">")
    elif user_input.lower() == "merge sort":
        start_time = time.time()
        array = merge_sort(array)
        end_time = time.time()
        print(f"{array} is the merge sort")
        print(f"Time taken to merge sort: {end_time - start_time} seconds")
        user_input = input(">")
    elif user_input.lower() == "":
        print("easter egg - did u 4got 2 input something")
        user_input = input(">")
    else:
        print(f"{user_input} is invalid input")
        user_input = input(">")
