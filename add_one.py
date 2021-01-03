def add_num(n):
    """adds 1 to the number 1"""
    return list(map(int,str(int("".join(map(str,n)))+1))) #type("".join(map(str,n))) str

print(add_num([1,9,1]))  # 192
print(add_num([9,9,9]))  # 1000
print(add_num([0]))
print(add_num([1,8]))