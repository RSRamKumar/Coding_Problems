"""
Reverse an input array inplace in constant space and linear time
"""

def reversing_array_inplace(array):
    front_index = 0
    back_index = len(array)-1

    while front_index < back_index:
       # print(array[front_index],array[back_index])
        array[front_index],array[back_index]=array[back_index],array[front_index]
        front_index +=1
        back_index -= 1
    return array

print(reversing_array_inplace([1,2,3,4,5,6,7]))



def reversing_array_inplace_using_forloop(array):
    end = len(array) - 1
    limit = int(end / 2) + 1
    for i in range(limit):
        array[i], array[end] = array[end], array[i]
        end-=1
    return array

print(reversing_array_inplace_using_forloop([1,2,3,4,5,6,7]))
print(reversing_array_inplace_using_forloop([1,2,3,4,5,6,7,8]))
print(reversing_array_inplace([1,2,3,4,5,6,7]))


#https://www.youtube.com/watch?v=p0VD9Fdlx5A
#https://codereview.stackexchange.com/questions/155619/reversing-an-array-in-python