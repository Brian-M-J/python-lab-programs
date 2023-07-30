# Insertion and merge sort
from random import randint

def merge_sort(lst: list[int]) -> None:
    if len(lst) <= 1:
        return
    mid: int = len(lst) // 2
    left_half: list[int] = lst[:mid]
    right_half: list[int] = lst[mid:]
    merge_sort(left_half)
    merge_sort(right_half)
    i = j = k = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            lst[k] = left_half[i]
            i += 1
        else:
            lst[k] = right_half[j]
            j += 1
        k += 1
    while i < len(left_half):
        lst[k] = left_half[i]
        i += 1
        k += 1
    while j < len(right_half):
        lst[k] = right_half[j]
        j += 1
        k += 1

def insertion_sort(arr: list[int]) -> None:
    for i in range(len(arr)):
        key: int = arr[i]
        j: int = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def main() -> None:
    my_list: list[int] = [randint(0, 999) for _ in range(10)]
    print(f'Unsorted list: {my_list}')
    insertion_sort(my_list)
    print(f"Sorted list (using insertion sort): {my_list}")
    my_list: list[int] = [randint(0, 999) for _ in range(10)]
    print(f"\nUnsorted list: {my_list}")
    merge_sort(my_list)
    print(f"Sorted list (using merge sort): {my_list}")

if __name__ == '__main__':
    main()
