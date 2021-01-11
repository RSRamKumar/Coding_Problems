"""
Given an array of length n having integers 1 to n with some elements being repeated. Count frequencies of all elements from 1 to n.

Example:
Input Array: {2, 3, 3, 2, 5}
Output:
1 0
2 2
3 2
4 0
5 1
"""
def count_freq_1_to_n(array):
    return [(i,array.count(i)) for i in range(1,max(array)+1)]

def count_freq_1_to_n_using_while_loop(array):
    i=0
    count = {}
    while i<len(array):
        #print(array[i],array[i]-1,array[i]-1 in array)  # current index element, previous value, True or False
        if array[i] in count:
            count[array[i]]+=1
        elif array[i] not in count:
            count[array[i]]=1
        prev = array[i] - 1
        while prev >= 1:
            if prev not in array:
                count[prev] = 0
            prev-=1
        i=i+1

    return count

if __name__ == "__main__":
    print(count_freq_1_to_n([2,3,3,2,5]))
    print(count_freq_1_to_n([1]))
    print(count_freq_1_to_n([ 4, 4, 4, 4 ]))
    print(count_freq_1_to_n([ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ]))
    print(count_freq_1_to_n([ 11, 10, 9, 8, 7, 6, 5, 4, 3, 2,  1 ]))

    print("*"*50)
    print(count_freq_1_to_n_using_while_loop([2,3,3,2,5,11]))
    print(count_freq_1_to_n_using_while_loop([1,9,14]))
    print(count_freq_1_to_n_using_while_loop([4,4,4,4]))
    print(count_freq_1_to_n_using_while_loop([1,2,3,4,5,6,7,8,9]))