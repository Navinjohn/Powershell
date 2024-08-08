"""function to find the occurences in the list or strings or elements
Args: 
    s -> Input data that can be list or strings or elements
Returns:
    r -> Dictionary: returns the count of the elements in the dictionary
"""
def f(s):
    r = {}
    for i in s:
        if i in r:
            r[i] += 1
        else:
            r[i] = 0  #we can change this to 1 instead of 0
    return r