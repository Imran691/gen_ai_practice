# AWS Toolkit - Amazon Q, CodeWhisperer, and more

def add_two_nums(a, b):
    """
    this function adds two numbers
    :param a: first number
    :param b: second number
    :return: sum of a and b
    
    """
    return a + b

def add_three_nums(a, b, c):
    """
    this function adds three numbers
    :param a: first number
    :param b: second number
    :param c: third number
    :return: sum of a, b and c
    """
    return a + b + c

def add_four_nums(a, b, c, d):
    """
    this function adds four numbers
    :param a: first number
    :param b: second number
    :param c: third number
    :param d: fourth number
    :return: sum of a, b, c and d
    """
    return a + b + c + d

def add_five_nums(a, b, c, d, e):
    """
    this function adds five numbers
    :param a: first number
    :param b: second number
    :param c: third number
    :param d: fourth number
    :param e: fifth number
    :return: sum of a, b, c, d and e
    """
    return a + b + c + d + e

# create a function that takes a list of numbers and returns the sum

def sum_list(nums):
    """
    this function takes a list of numbers and returns the sum
    :param nums: list of numbers
    :return: sum of the numbers in the list
    """
    total = 0
    for num in nums:
        total += num
    return total


# create a login function that takes username and password and returns True if the username and password are correct, False otherwise
def login(username, password):
    """
    this function takes username and password and returns True if the username and password are correct, False otherwise
    :param username: username
    :param password: password
    :return: True if the username and password are correct, False otherwise
    """
    if username == "admin" and password == "admin":
        return True
    else:
        return False
    
# create a function that takes a list of numbers and returns the average
    
def average(nums):
    """
    this function takes a list of numbers and returns the average
    :param nums: list of numbers
    :return: average of the numbers in the list
    """
    total = 0
    for num in nums:
        total += num
    return total / len(nums)