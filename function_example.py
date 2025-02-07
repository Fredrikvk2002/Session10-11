def greet():
    """

    :return:
    """

    print("Hello!")
    return 0

def greet_improved(name):
    """

    :param name: the name of the person to greet
    :return: none
    """
    print("Hello",name)

greet_improved("John")
greet_improved("Jane")

def custom_op(x=0,y=0):
    """
    custom op: 10x + y
    :param x: the first number
    :param y: the second number
    :return: number, 10x + y
    """

    result = 10*x + y
    return result

print(custom_op(5,9))
x = custom_op(5,9)
print(f"the result of custom_op is {x}")
x = custom_op(y=9,x=5)
print(f"the result of custom_op is {x}")
print(custom_op(5))
print(custom_op(y=5))
print(custom_op())

def bond_intro(name):
    print("the name is:",name)

def bond