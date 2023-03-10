# create a rectangle with width=3 and height=4
r = Rectangle(3, 4)

# get the width and height properties
print(r.width)  # output: 3
print(r.height)  # output: 4

# set the width and height properties
r.width = 5
r.height = 6

# get the area and perimeter
print(r.area())  # output: 30
print(r.perimeter())  # output: 22

# print the rectangle
print(str(r))  # output: 
              # #####
              # #####
              # #####
              # #####
              # #####

# create a new rectangle by using eval(repr(r))
new_r = eval(repr(r))

# check if the new rectangle is equal to the original one
print(new_r.width == r.width and new_r.height == r.height)  # output: True

