from collections import defaultdict


class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        words_sum = 0

        for word in words:
            # chars_dict = {}
            chars_dict = defaultdict(int)
            for char in chars:
                chars_dict[char] += 1
            all_found_letters = True

            for index, letter in enumerate(word):
                if letter in chars_dict:
                    if chars_dict[letter] > 1:
                        chars_dict[letter] -= 1
                    else:
                        del chars_dict[letter]
                else:
                    all_found_letters = False
                    break
            if all_found_letters is True:
                words_sum += len(word)
        return words_sum
