# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 

def hello_name(user_name):
    return f"hello {user_name}"

username_input = "USER_NAME!"
print(hello_name(username_input))


# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    for number in range(1, 101, 2):  
        print(number)

first_odds()


# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list.

def max_num_in_list(a_list):
    return max(a_list)

numbers = [5, 8, 200, 10, 3]
result = max_num_in_list(numbers)
print(result)


# Question 4
# Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false).

def is_leap_year(a_year):
    if (a_year % 4 == 0 and a_year % 100 != 0) or (a_year % 400 == 0):
        return True
    else:
        return False

year_input = 2024
result = is_leap_year(year_input)
print(result)


# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type.

def is_consecutive(a_list):
    if not a_list or len(a_list) < 2:
        return False

    for i in range(len(a_list) - 1):
        if a_list[i + 1] - a_list[i] != 1:
            return False

    return True

list = [2, 3, 4, 5, 6, 7]

result = is_consecutive(list)

print(result)




