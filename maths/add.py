"""
Addition of N numbers.
"""


def add(*a):
    a=[*a]
    try:
        value=sum(a)
        print('Sum is ' + str(value))
    except:
        print('Addition is invalid')

add(2,3) # Output is 5
add(34,2,1) # Output is 37
add(5,6,8,1,3) # output is 23
