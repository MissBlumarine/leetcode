class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        not_repeated = []
        repeated = []
        for i in s:
            if i in not_repeated:
                repeated.append(i)
            else:
                not_repeated.append(i)
        for index, char in enumerate(s):
            if char not in repeated:
                return index
        return -1


a = Solution()
print(a.firstUniqChar("lletcode"))