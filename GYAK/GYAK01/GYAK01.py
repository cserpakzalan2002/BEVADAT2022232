# %%
def contains_odd(input_list):
    for i in input_list:
        if i % 2 != 0:
            return True
    return False

# %%
list=[2,3,4]
def is_odd(input_list):
    answer=[]
    for i in input_list:
        answer.append(i % 2 != 0)
    return answer

# %%
def element_wise_sum(input_list_1, input_list_2):
    if len(input_list_1) != len(input_list_2):
        return None  # lists must be of equal length

    answer=[]
    for i in range(len(input_list_1)):
        answer.append(input_list_1[i] + input_list_2[i])

    return answer

# %%
def dict_to_list(input_dict):
    answer=[]
    for key, value in input_dict.items():
        answer.append((key, value))
    return answer


