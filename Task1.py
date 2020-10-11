import numpy as np
import unittest

def product_three_largest_integers(list_of_integers):
    # Returns the highest product between three of the numbers
    list_of_integers.sort()

    # Check that the list contain at least three numbers, returns false otherwise
    if not all(isinstance(item, int) for item in list_of_integers) or not len(list_of_integers) >= 3:
        return False 

    # After sorting, highest product either consists of two most negative numbers pluss highest remaining, or it consists of the three highest numbers
    negative_numbers_answer = np.prod(list_of_integers[:2]) * list_of_integers[-1]
    positive_numbers_answer = np.prod(list_of_integers[-3:])
    
    # returns the biggest of our options
    if negative_numbers_answer > positive_numbers_answer:
        return negative_numbers_answer
    else:
        return positive_numbers_answer



# Test cases
test_list1 = [1, 10, 2, 6, 5, 3]
test_list2 = [0, -5, -13, -1, -3]
test_list3 = [2, -1, -4, -18, -17]
test_list4 = [1,2]

assert product_three_largest_integers(test_list1) == 300 # 10*6*5, Case with normal numbers
assert product_three_largest_integers(test_list2) == 0 # Case where largest product is zero
assert product_three_largest_integers(test_list3) == 612 # -18*-17*2, Case where you multiply two negative numbers and one positive
assert product_three_largest_integers(test_list4) is False