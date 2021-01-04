"""
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
"""
import numpy as np
def finding_array_multiplication_except_index_try1(input_array:list)->list:
    new_array = []   # output
    product_value = [] # list to hold new values for doing product
    for i in range(len(input_array)):
        index_to_pop = i
        new_index_list=[i for i in range(len(input_array))]
        new_index_list.pop(index_to_pop)
        for index in new_index_list:
            product_value.append(input_array[index])
        new_array.append(np.product(product_value))
        product_value.clear()
    return new_array

def finding_array_multiplication_except_index_try2(input_array:list)->list:
    new_array = [1 for i in range(len(input_array))]  # output
    for i in range(len(input_array)):
        right_index=[j for j in range(i+1,len(input_array))]
        left_index = [j for j in range(i)]
        all_index= right_index + left_index
        for index in all_index:
            new_array[i] *= input_array[index]
    return (new_array)

def finding_array_multiplication_except_index_try3(input_array:list)->list:
    new_array=[1 for i in range(len(input_array))]
    for i in range(len(input_array)):
        for j in range(len(input_array)):
            if i != j:
                #print(i, j) #i,j is 0,1 ; 0,2 ; 0,3 ; 0,4; 1,0; 1,2 ...
                new_array[i] *= input_array[j]
    return new_array

def finding_array_multiplication_except_index_try4(input_array:list)->list:
    new_array = []
    for num in input_array:
        copy_array=input_array.copy()
        copy_array.remove(num)
        new_array.append(np.product(copy_array))
    return new_array

print(finding_array_multiplication_except_index_try1([1, 2, 3, 4, 5]))
print(finding_array_multiplication_except_index_try2([4,2,1]))
print(finding_array_multiplication_except_index_try3([3,4,7]))
print(finding_array_multiplication_except_index_try4([2,4,8]))

