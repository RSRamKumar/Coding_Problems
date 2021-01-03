def finding_first_recurring_char(input_string):
    """identifies the first recurring char in the string"""
    count_dict={}
    for char in input_string:
        if char in count_dict:
            return char
        else:
            count_dict[char]=1

print(finding_first_recurring_char("ABCA")) # A
print(finding_first_recurring_char("BCABA")) # B
print(finding_first_recurring_char("BBACXZX")) #B

print(finding_first_recurring_char("ABX")) # None

from collections import Counter
print((Counter("ABCA").most_common(1))[0][0])
print((Counter("BCABA").most_common(1))[0][0])
print(list(Counter("CBACXZX").elements() )[0])