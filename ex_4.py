"""
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
你可以假设 nums1 和 nums2 不会同时为空。
nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        if n < m:
            nums1, nums2, m, n = nums2, nums1, n, m
        if n == 0:
            raise ValueError
        i_min = 0
        i_max = m
        # max_left_part = 0
        # min_right_part = 0
        while i_min <= i_max:
            i = (i_min+i_max)//2
            j = (m + n + 1) // 2 - i
            if i > 0 and nums1[i - 1] > nums2[j]:
                i_max = i - 1
            elif i < m and nums2[j - 1] > nums1[i]:
                i_min = i + 1
            else:
                if i == 0:
                    max_left_part = nums2[j - 1]
                elif j == 0:
                    max_left_part = nums1[i - 1]
                else:
                    max_left_part = max(nums1[i - 1], nums2[j - 1])
                if (n + m) % 2 == 1:
                    return max_left_part
                if i == m:
                    min_right_part = nums2[j]
                elif j == n:
                    min_right_part = nums1[i]
                else:
                    min_right_part = min(nums1[i], nums2[j])
                return (max_left_part + min_right_part) / 2