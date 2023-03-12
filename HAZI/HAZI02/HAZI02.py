# %%
import numpy as np

def column_swap(arr):
    # megnézzük, hogy az array valóban 2D-e
    if arr.ndim != 2:
        raise ValueError('Az input array-nek 2 dimenziójúnak kell lennie!')
    
    # oszlopok megfordítása
    return arr[:, ::-1]


arr = np.array([[1, 2], [3, 4]])
swapped_arr = column_swap(arr)
print(swapped_arr)


# %%


def compare_two_array(arr1, arr2):
    if arr1.shape != arr2.shape:
        raise ValueError('Az input array-k méreteinek megegyezőnek kell lenniük!')
    
    # azonos elemek keresése
    equal_idx = np.where(arr1 == arr2)[0]
    
    return equal_idx


arr1 = np.array([7, 8, 9])
arr2 = np.array([9, 8, 7])
equal_idx = compare_two_array(arr1, arr2)
print(equal_idx)


# %%
def get_array_shape(arr):
    shape = arr.shape
    ndim = arr.ndim
    
    if ndim == 1:
        return f'hossz: {shape[0]}, melyseg: 1'
    elif ndim == 2:
        return f'sor: {shape[0]}, oszlop: {shape[1]}, melyseg: 1'
    elif ndim == 3:
        return f'sor: {shape[0]}, oszlop: {shape[1]}, melyseg: {shape[2]}'
    else:
        raise ValueError('Az input array nem 1D, 2D vagy 3D!')

arr = np.array([[1, 2, 3], [4, 5, 6]])
shape_str = get_array_shape(arr)
print(shape_str)


# %%


def encode_Y(y, num_classes):
    y_pred = np.zeros((len(y), num_classes))
    
    for i in range(len(y)):
        y_pred[i, y[i]] = 1
        
    return y_pred


y = np.array([1, 2, 0, 3])
num_classes = 4

y_pred = encode_Y(y, num_classes)
print(y_pred)


# %%


def decode_Y(Y_enc):
    return np.argmax(Y_enc, axis=1)



# %%


def eval_classification(classes, predictions):
    max_index = np.argmax(predictions)
    result = classes[max_index]
    print("A legvalószínűbb osztály: ", result)
    return result



# %%


def replace_odd_numbers(arr):
    return np.where(arr % 2 == 1, -1, arr)


# %%
# Készíts egy olyan függvényt, ami egy array értékeit -1 és 1-re változtatja, attól függően, hogy az adott elem nagyobb vagy kisebb a paraméterként megadott számnál.\n",
    "# Ha a szám kisebb mint a megadott érték, akkor -1, ha nagyobb vagy egyenlő, akkor pedig 1.\n",
    "# Be: [1, 2, 5, 0], 2\n",
    "# Ki: [-1, 1, 1, -1]\n",
    "# replace_by_value()"

# %%
def replace_by_value(arr, val):
    return np.where(arr < val, -1, 1)


# %%


def array_multi(arr):
    return np.prod(arr)


input_arr = [1,2,3,4]
output = array_multi(input_arr)
print("Input array:", input_arr)
print("Output:", output)

# %%
def array_multi_2d(arr):
 row_products = np.array([np.prod(row) for row in arr])
 return row_products

arr = [[1, 2], [3, 4]]
print(array_multi_2d(arr)) # Kiír [2, 12]

# %%


def add_border(arr):
    m, n = arr.shape
    res = np.zeros((m+2, n+2))
    res[1:m+1, 1:n+1] = arr
    return res


arr = np.array([[1,2],[3,4]])
new_arr = add_border(arr)
print(new_arr) # [[0. 0. 0. 0.]

# %%
from datetime import datetime, timedelta

def list_days(start_date, end_date):
    start = datetime.strptime(start_date, '%Y-%m')
    end = datetime.strptime(end_date, '%Y-%m')
    num_days = (end - start).days + 1
    days = np.array([start + timedelta(days=i) for i in range(num_days)])
    days_str = np.array([d.strftime('%Y-%m-%d') for d in days])
    return days_str
    
start_date = '2023-03'
end_date = '2023-04'
result = list_days(start_date, end_date)
print(result)

# %%


def get_act_date():
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    return np.datetime64(date_str)

print(get_act_date())


# %%


import time

def sec_from_1970():
    return int(time.time())

print(sec_from_1970())




