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

if __name__ == "__main__":
    print(count_freq_1_to_n([2,3,3,2,5]))
    print(count_freq_1_to_n([1]))
    print(count_freq_1_to_n([ 4, 4, 4, 4 ]))
    print(count_freq_1_to_n([ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ]))
    print(count_freq_1_to_n([ 11, 10, 9, 8, 7, 6, 5, 4, 3, 2,  1 ]))
