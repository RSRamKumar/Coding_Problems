"""
Given a list of repetitive elements: all elements occur even time except one. find that
"""
from collections import Counter
arr = [1,4,6,4,1,]
print( (Counter(arr)).items())        #dict_items([(1, 2), (4, 2), (6, 1)])
odd_occurence = list(filter(lambda x : x[1] %2!=0, (Counter(arr)).items()))
print(odd_occurence)     #[(6, 1)] (element, count)
 

#https://stackoverflow.com/questions/33077274/lambda-in-python-can-iterate-dict