class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        for i in range(1, len(strs)):
            length = min(len(strs[0]), len(strs[i]))
            while length > 0 and strs[0][0:length] != strs[i][0:length]:
                length -= 1
                if length == 0:
                    return ""
            return strs[0][0:length]
