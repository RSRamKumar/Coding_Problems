 def cylinder_volume(height,radius):
    pi=3.14
    return height * pi * radius **2
    
print(cylinder_volume(1,4))
print(cylinder_volume(2,3))
print(cylinder_volume(3,2))
print(cylinder_volume(4,1))
print()
print(cylinder_volume(3,4))
print(cylinder_volume(4,2))

print()


l=[(3,4),(4,2)]
 
print([cylinder_volume(i[0],i[1]) for i in l])

# map function takes function name , list of arguments
# [3,4] is the list of height, [4,2] is the list of radius
print(list(map(cylinder_volume,[3,4],[4,2])))

print(list(map(cylinder_volume,[1,2,3,4],[4,3,2,1] )))

print(list(map(lambda h,r: h*r*r*3.14,[1,2,3,4],[4,3,2,1] )))

"""
50.24
56.52
37.68
12.56

150.72
50.24

[150.72, 50.24]
[150.72, 50.24]
[50.24, 56.52, 37.68, 12.56]
[50.24, 56.52, 37.68, 12.56]
"""
