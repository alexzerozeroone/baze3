import random

def generateNrSeq():
    """ Return a sequence of numbers """
    # Empty array
    seq = [
        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
    ]
    # Return result
    return seq

def generateLtSeq():
    """ Generates a sequence of default letters"""
    # Default letters
    l = "abcdefgh"
    # Default upper leters
    ll = l.upper()
    # Combine
    lll = l + ll
    
    # Turn into array
    l4 = [l for l in lll]
    # Return result, randomized
    return l4
    