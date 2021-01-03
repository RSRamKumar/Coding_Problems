"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""

def finding_two_number(input_list,k):
    """function for finding whether 2 elements in the list adds to give k or not"""
    for i in range(0,len(input_list)):
        first_value=input_list[i]
        for j in range(i+1,len(input_list)):
            second_value=input_list[j]
            #print(first_value, second_value)
            if first_value + second_value == k:
                return first_value, second_value
    return None

print(finding_two_number([10, 15, 3, 7],25))
print(finding_two_number([10, 15, 3, 7],18))
print(finding_two_number([10, 15, 3, 7],17))
print(finding_two_number([10, 15, 3, 7],13))
print(finding_two_number([10, 15, 3, 7],22))
print(finding_two_number([10, 15, 3, 7],20))


def FindPairs(arr, k):
    for i in range(0, len(arr)):
        if k - arr[i] in arr:
            return True
    return False
A = [1, 4, 45, 6, 10, 8]
n = 18
print(FindPairs(A, n))
print(FindPairs([10, 15, 3, 7],20))