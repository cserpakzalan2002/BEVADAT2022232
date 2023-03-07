# %%
def column_swap(arr):
    for i in range(len(arr)):
        arr[i] = arr[i][::-1]
    return arr

arr = [[1, 2], [3, 4]]
result = column_swap(arr)
print(result)  


# %%
def compare_two_array(arr1, arr2):
    equal_indices = []
    for i in range(len(arr1)):
        if arr1[i] == arr2[i]:
            equal_indices.append(i)
    return equal_indices

arr1 = [7, 8, 9]
arr2 = [9, 8, 7]
result = compare_two_array(arr1, arr2)
print(result)  


# %%
def get_array_shape(arr):
    shape = []
    while isinstance(arr, list):
        shape.append(len(arr))
        arr = arr[0]
    return ", ".join([f"{dim}" for dim in shape]) + f", melyseg: {arr.ndim - len(shape)}"


arr = [[1, 2, 3], [4, 5, 6]]
result = get_array_shape(arr)
print(result)  


# %%
import numpy as np

def encode_Y(Y, num_classes):
    encoded_Y = np.zeros((len(Y), num_classes))
    for i in range(len(Y)):
        encoded_Y[i, Y[i]] = 1
    return encoded_Y



# %%
def decode_Y(encoded_Y):
    return np.argmax(encoded_Y, axis=1)

encoded_Y = np.array([[0,1,0,0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1]])
decoded_Y = decode_Y(encoded_Y)
print(decoded_Y)


# %%
def eval_classification(classes, probabilities):
    return classes[np.argmax(probabilities)]

classes = ['alma', 'körte', 'szilva']
probabilities = np.array([0.2, 0.2, 0.6])
predicted_class = eval_classification(classes, probabilities)
print(predicted_class) 


# %%
def replace_odd_numbers(arr):
     return np.where(arr % 2 == 1, -1, arr)

# %%
def replace_by_value(arr, num):
    
    result = []
    for elem in arr:
        if elem < num:
            result.append(-1)
        else:
            result.append(1)
    return result


arr = [1, 2, 5, 0]
num = 2
print(replace_by_value(arr, num)) 


# %%
def array_multi(arr):
    result = 1
    for elem in arr:
        if type(elem) == list:
            result *= array_multi(elem) # Rekurzió a több dimenziós tömbök esetére
        else:
            result *= elem
    return result

arr = [1, 2, 3, 4]
print(array_multi(arr)) 





# %%


def add_border(arr):
    rows, cols = arr.shape
    new_arr = np.zeros((rows+2, cols+2), dtype=arr.dtype)
    new_arr[1:-1, 1:-1] = arr
    return new_arr


arr = np.array([[1,2],[3,4]])
print(add_border(arr))


# %%

from datetime import datetime, timedelta

def list_days(start_date, end_date):
    start = datetime.strptime(start_date, '%Y-%m')
    end = datetime.strptime(end_date, '%Y-%m')
    num_days = (end - start).days + 1
    date_array = np.array([start + timedelta(days=i) for i in range(num_days)])
    return np.array([date.strftime('%Y-%m-%d') for date in date_array])


start_date = '2023-03'
end_date = '2023-04'
days_array = list_days(start_date, end_date)
print(days_array)


# %%



def current_date():
    now = datetime.now()
    date_str = now.strftime('%Y-%m-%d')
    return np.datetime64(date_str)

date = current_date()
print(date)


# %%
import time

def sec_from_1970():
    start_time = time.mktime((1970, 1, 1, 0, 2, 0, 0, 0, 0))
    current_time = time.time()
    elapsed_time = current_time - start_time
    return int(elapsed_time)

print(sec_from_1970)


