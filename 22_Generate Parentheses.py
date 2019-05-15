# -*- coding: utf-8 -*-
"""
Created on Wed May 15 13:26:06 2019

@author: Shreyans
"""

"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

from random import choice

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parantheses_map = {'(':n-1, ')':n}
        combinations = []
        i=0
        while i < 2**n: #how to end this while loop?
            i+=1
            string = '('
            temp_map = parantheses_map.copy()
            while list(temp_map.values()) != [0, 0]:
                append_this = choice(list(parantheses_map.keys()))
                val = temp_map[append_this]
                if val > 0 and (temp_map['('] < temp_map[')'] or append_this is '('):
                    temp_map[append_this] = val - 1
                    string+=append_this
            if string not in combinations:
                combinations.append(string)
