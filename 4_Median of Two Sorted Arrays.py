# -*- coding: utf-8 -*-
"""
Created on Sat May  4 18:09:47 2019

@author: Shreyans
"""

# =============================================================================
#    There are two sorted arrays nums1 and nums2 of size m and n respectively.
#    Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#    
#    You may assume nums1 and nums2 cannot be both empty.
#    
#    Example 1:
#    
#    nums1 = [1, 3]
#    nums2 = [2]
#    
#    The median is 2.0
#    Example 2:
#    
#    nums1 = [1, 2]
#    nums2 = [3, 4]
#    
#    The median is (2 + 3)/2 = 2.5
# =============================================================================

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
            len_arrays = len(nums1) + len(nums2)
            k=len_arrays//2
            if len_arrays%2==0:
                return (self.find_kth_element(nums1,nums2,k) + self.find_kth_element(nums1,nums2,k-1))/2
            else:
                return self.find_kth_element(nums1,nums2,k)
        
    def find_kth_element(self, a,b,k):
        if not a:
            return b[k]
        if not b:
            return a[k]
        ind_m_a, ind_m_b = len(a)//2, len(b)//2
        median_a, median_b = a[ind_m_a], b[ind_m_b]
        if ind_m_a + ind_m_b >= k:
            if median_a > median_b:
                return self.find_kth_element(a[:ind_m_a],b,k)
            else:
                return self.find_kth_element(a,b[:ind_m_b],k) 
        else:
            if median_a > median_b:
                return self.find_kth_element(a,b[ind_m_b+1:], k-ind_m_b-1)
            else:
                return self.find_kth_element(a[ind_m_a+1:],b, k-ind_m_a-1)
