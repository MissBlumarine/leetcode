# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.


class Solution(object):

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        list_3sum = []
        nums = sorted(nums)

        for i in range(0, len(nums) - 2):

            if nums[i] > 0:
                break
            if nums[i] == nums[i - 1] and i > 0:
                continue

            min_index = i + 1
            max_index = len(nums) - 1

            while min_index < max_index:

                sum = nums[i] + nums[min_index] + nums[max_index]

                if sum == 0:
                    list_3sum.append((nums[i], nums[min_index], nums[max_index]))

                if sum <= 0:
                    min_index += 1
                    while (nums[min_index] == nums[min_index - 1] and min_index < max_index):
                        min_index += 1

                else:
                    max_index -= 1

        return list_3sum
