# %%
#Készíts egy függvényt ami létre hoz egy nullákkal teli numpy array-t.\n",
#Paraméterei: mérete (tuple-ként), default mérete pedig legyen egy (2,2)\n",
#Be: (2,2)\n",
#Ki: [[0,0],[0,0]]\n",
#create_array()"

import numpy as np

def create_array(size=(2,2)):
    return np.zeros(size).tolist()




# %%
#Készíts egy függvényt ami a paraméterként kapott array-t főátlóját feltölti egyesekkel\n",
#Be: [[1,2],[3,4]]\n",
#Ki: [[1,2],[3,1]]\n",
#set_one()"


def set_one(arr):
    np.fill_diagonal(arr, 1)
    return arr

#arr = np.array([[1,2],[3,4]])




# %%
# Készíts egy függvényt ami transzponálja a paraméterül kapott mártix-ot:\n",
# Be: [[1, 2], [3, 4]]\n",
# Ki: [[1, 3], [2, 4]]\n",
# do_transpose()"



def do_transpose(arr):
    return arr.T

#arr = np.array([[1, 2], [3, 4]])
#print(do_transpose(arr))


# %%
 # Készíts egy olyan függvényt ami az array-ben lévő értékeket N tizenedjegyik kerekíti, ha nincs megadva ez a paraméter, akkor legyen az alapértelmezett a kettő \n",
 # Be: [0.1223, 0.1675], 2\n",
 # Ki: [0.12, 0.17]\n",
 # round_array()"



def round_array(arr, N=2):
    return np.around(arr, N)

#arr = np.array([0.1223, 0.1675])




# %%
# Készíts egy olyan függvényt, ami a bementként kapott 0 és 1 ből álló tömben a 0 - False-ra, az 1 True-ra cserélni\n",
# Be: [[1, 0, 0], [1, 1, 1],[0, 0, 0]]\n",
# Ki: [[ True False False], [ True  True  True], [False False False]]\n",
# bool_array()"


def bool_array(arr):
    return np.array(arr, dtype=bool)

#arr = [[1, 0, 0], [1, 1, 1], [0, 0, 0]]



# %%
# Készíts egy olyan függvényt, ami a bementként kapott 0 és 1 ből álló tömben a 1 - False-ra az 0 True-ra cserélni\n",
# Be: [[1, 0, 0], [1, 1, 1],[0, 0, 0]]\n",
# Ki: [[ False True True], [ False  False  False], [True True True]]\n",
# invert_bool_array()"


def invert_bool_array(arr):
    return np.logical_not(arr)

#arr = [[1, 0, 0], [1, 1, 1], [0, 0, 0]]

# %%
# Készíts egy olyan függvényt ami a paraméterként kapott array-t kilapítja\n",
# Be: [[1,2], [3,4]]\n",
# Ki: [1,2,3,4]\n",
# flatten()\n"

def flatten(arr):
    return arr.flatten()

#arr = np.array([[1,2], [3,4]])





