"""
Given a string, find the first non-repeating character in that string.

Example:
Input: ADBCGHIEFKJLADTVDERFSWVGHQWCNOPENSMSJWIERTFB

Output:
K
""" 

string="ADBCGHIEFKJLADTVDERFSWVGHQWCNOPENSMSJWIERTFB"
print([i for i in string if string.count(i)==1][0])