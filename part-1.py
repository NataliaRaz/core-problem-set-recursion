# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    return n * factorial(n - 1)


# reverse
def reverse(text):

    return text[::-1]


# bunny

def bunny(count):
    if count < 0:
        raise ValueError("Number of bunnies cannot be negative")
    if count == 0:
        return 0
    return 2 + bunny(count - 1)

# is_nested_parens

def is_nested_parens(parens):
    count = 0
    for ch in parens:
        if ch == "(":
            count += 1
        else:
            count -= 1
        if count < 0:
            return False

    return (count == 0)
