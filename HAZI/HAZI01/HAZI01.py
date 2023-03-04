# %%


def subset(input_list, start, end):
    return input_list[start:end]

    
input_list = [1, 2, 3, 4, 5]
result = subset(input_list, 1, 4)
print(result)



# %%
def every_nth(input_list, n):
    return input_list[::n]



input_list=[1,2,3,4,5,6,7,8,9]
result = every_nth(input_list,3)
print(result)

# %%
def unique(input_list):
    return len(set(input_list)) == len(input_list)

input_list=[1,2,3,4,5,6,7]
result = unique(input_list)
print(result)

# %%
def flatten(lst):
    flat_list = []
    for sublist in lst:
        for item in sublist:
            flat_list.append(item)
    return flat_list

lst = [[1,2],[3,4],[5,6]]
flatten(lst)
[1, 2, 3, 4, 5, 6]

# %%
def merge_lists(*args):
    result = []
    for lst in args:
        result.extend(lst)
    return result

lista_1 = [1,2,3]
lista_2 = [4,5,6]
lista_3 = [7,8,9]
merged = merge_lists(lista_1, lista_2, lista_3)
print(merged)

# %%
def reverse_tuples(input_list):
    return [(t[1], t[0]) for t in input_list]

input_list = [(1,2),(3,4)]
output_list = reverse_tuples(input_list)
print(output_list)   

# %%
def remove_duplicates(input_list):
    unique_list = list(set(input_list))
    return unique_list

input_list = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
print(remove_duplicates(input_list))

# %%
def transpose(matrix):
    return [list(row) for row in zip(*matrix)]

matrix = [[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]
print(transpose(matrix))

# %%
def split_into_chunks(lst, chunk_size):
    return [lst[i:i+chunk_size] for i in range(0, len(lst), chunk_size)]

lst = [1, 2, 3, 4, 5, 6, 7, 8]
chunk_size = 3
split_into_chunks(lst, chunk_size)
[[1, 2, 3], [4, 5, 6], [7, 8]]

# %%
def merge_dicts(*args):
    result = {}
    for dictionary in args:
        result.update(dictionary)
    return result

dict_1 = {"one":1, "two":2}
dict_2 = {"four":4, "three":3}
merge_dicts(dict_1, dict_2)
{"one":1, "two":2, "four":4, "three":3}    
 



# %%
def by_parity(lst):
    result = {"even": [], "odd": []}
    for num in lst:
        if num % 2 == 0:
            result["even"].append(num)
        else:
            result["odd"].append(num)
    return result

by_parity([1, 2, 3, 4, 5, 6])
{'even': [2, 4, 6], 'odd': [1, 3, 5]}

# %%
def mean_key_value(d):
    result = {}
    for key, value in d.items():
        result[key] = sum(value) / len(value)
    return result

mean_key_value({"some_key":[1,2,3,4],"another_key":[1,2,3,4]})
{'some_key': 2.5, 'another_key': 2.5}


