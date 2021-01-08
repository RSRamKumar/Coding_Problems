"""
Reverse an input array inplace in constant space and linear time
"""

def reversing_array_inplace(array):
    front_index = 0
    back_index = len(array)-1

    while front_index < back_index:
        print(array[front_index],array[back_index])
        array[front_index],array[back_index]=array[back_index],array[front_index]
        front_index +=1
        back_index -= 1
    return array

print(reversing_array_inplace([1,2,3,4,5,6,7]))