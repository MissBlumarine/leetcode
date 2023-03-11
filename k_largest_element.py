# Given an integer array nums and an integer k, return the kth largest element in the array.
#
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# You must solve it in O(n) time complexity.

from typing import List


class Solution:
    def findkthlargest(nums: List[int], k: int) -> int:
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        k = len(nums) - k

        def quick_select(l: int, r: int):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1

            nums[p], nums[r] = nums[r], nums[p]
            if p > k:
                return quick_select(l, p-1)
            if p < k:
                return quick_select(p+1, r)
            else:
                return nums[p]

        return quick_select(0, len(nums)-1)


