# Word Length Mapping
def word_length_mapping(words):
    result={}
    for word in words:
        result[word] = len(word)
    return result
words = ["apple", "banana", "apple"]
print(word_length_mapping(words))

# Two Sum- leetcode
def two_sum(nums, target):
    result={}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in result:
            return [result[diff], i]
        result[num] = i
print(two_sum([2, 7, 11, 15], 9))     
print(two_sum([3, 2, 4], 6))           
print(two_sum([3, 3], 6))  

# Filter List by Type
def filter_by_type(mixed_list):
    int_list = [item for item in mixed_list if isinstance(item, int)]
    str_list = [item for item in mixed_list if isinstance(item, str)]
    return int_list, str_list
list = [1, "a", 2.5]
ints, strs = filter_by_type(list)
print("Integer:", ints)
print("String:", strs)

# Find Duplicate Elements
def find_duplicates(lst):
    duplicate=[]
    for item in lst:
        if lst.count(item) > 1 and item not in duplicate:
            duplicate.append(item)
    return duplicate
print(find_duplicates([1, 2, 2, 3]))        
print(find_duplicates([4, 5, 6, 5, 4]))      
print(find_duplicates(['a', 'b', 'a', 'c']))

# Dictionary Value Multiplier
def multiply_dict_value(original_dict, multiplier):
    result = {key: value * multiplier for key, value in original_dict.items()}
    return result
print(multiply_dict_value({"a": 2, "b": 3}, 2))