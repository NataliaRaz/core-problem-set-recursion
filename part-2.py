# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search

def search(array, query):
    if not array:
        return False
    
    if array[0] == query:
        return True
    
    return search(array[1:], query)
        

# is_palindrome

def is_palindrome(text):
    if len(text) <= 1:
        return True

    if text[0] != text[-1]:
        return False
        
    return(is_palindrome(text[1:-1]))
    

# digit_match

def digit_match(a: int, b: int):
    match = 1 if (a % 10) == (b % 10) else 0
    if a < 10 or b < 10:
        return match
    return match + digit_match(a // 10, b // 10)
