def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
print(find_max([4, 2, 8, 7, 9]))

def count_even(numbers):
    count_num = 0
    for num in numbers:
        if num % 2 == 0:
            count_num += 1
    return count_num
print(count_even([1, 2, 3, 4]))

def list_rotate(num, k):
    k = k % len(num)
    return num[-k:] + num[:-k]
print(list_rotate([1, 2, 3, 4], 2))

def chunk_list(num, n):
    return [num[i:i+n] for i in range(0, len(num), n)]
print(chunk_list([1, 2, 3, 4], 2))

def is_palindrome_list(num):
    return num == num[::-1]
print(is_palindrome_list([1, 2, 2, 1]))