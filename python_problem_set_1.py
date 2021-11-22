# 1. Set the variable `given_name` to the string "Addison".
given_name = 'addison'
# ------------------------------------------------------------------------------
# 2. You have 20 candies that you must divide equally among 6 people. How many candies will be left over?
# Set variables for `candies`, `people`, `left_over` to make your tests pass.
candies = 20
people = 6
left_over = candies / people 
# ------------------------------------------------------------------------------
# 3. Create a function called `greeting` that returns "Hello, <name>!",
# where <name> is the name given as an argument to the function.
def greeting(name):
    return "Hello, "+ name +", nice to meet you."

# ------------------------------------------------------------------------------
# 4. Create a function called `is_odd` that, given a number, will
# return true if the number is odd and false if it is not. An odd number is a
# number which, when divided by 2, has a remainder of 1 or -1.
def is_odd(number):
    if number / 2 == 1 or number / 2 == -1:
        return True
    else: 
        return False

 # ------------------------------------------------------------------------------
# 5. Create a function called `is_even` that, given a number, will
# return true if the number is even and false if it is not. An even number is a
# number which, when divided by 2, has a remainder of 0.
def is_even(number):
    if number / 2 == 0:
        return True
    else:
        return False