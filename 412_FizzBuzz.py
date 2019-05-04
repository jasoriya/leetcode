# -*- coding: utf-8 -*-
"""
Created on Sat May  4 12:29:24 2019

@author: Shreyans
"""

# =============================================================================
#   Write a program that outputs the string representation of numbers from 1 to n.
#   But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
#    
#    Example:
#    
#    n = 15,
#    
#    Return:
#    [
#        "1",
#        "2",
#        "Fizz",
#        "4",
#        "Buzz",
#        "Fizz",
#        "7",
#        "8",
#        "Fizz",
#        "Buzz",
#        "11",
#        "Fizz",
#        "13",
#        "14",
#        "FizzBuzz"
#    ]
# =============================================================================

#Solution 1
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        l = []
        for i in range(1, n+1):
            divBy3, divBy5 = i%3, i%5
            if divBy3==0 and divBy5==0:
                l.append("FizzBuzz")
            elif divBy3 == 0:
                l.append("Fizz")
            elif divBy5 == 0:
                l.append("Buzz")
            else:
                l.append(str(i))
        return l