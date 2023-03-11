class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        dict_frequent = {}
        frequent_numbers = {}

        for i in nums:
            if i not in dict_frequent:
                dict_frequent[i] = 1
            else:
                dict_frequent[i] += 1
        print(dict_frequent)
        for key, value in dict_frequent.items():
            if value not in frequent_numbers:
                frequent_numbers[value] = [key]
            else:
                frequent_numbers[value].append(key)
        print(frequent_numbers)
        result = []
        for i in range(len(nums), 0, -1):
            if i in frequent_numbers:
                print(i)
                result.extend(frequent_numbers[i])
                print(result)
            if len(result) >= k:
                break
        return result


a = Solution()
print(a.topKFrequent([6, 6, 1, 1, 1, 2, 2, 3, 5, 22, 22, 22, 22], 2))
