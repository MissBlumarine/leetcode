class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        if n == 1:
            return "1"
        else:
            previous = self.countAndSay(n - 1)

        result = ''
        counter = {}
        for i in range(0, len(previous)):
            digit = previous[i]

            if digit not in counter:
                for key, value in counter.items():
                    result += str(value) + key

                counter = {}
                counter[digit] = 1

            else:
                counter[digit] += 1

        for key, value in counter.items():
            result += str(value) + key

        return result