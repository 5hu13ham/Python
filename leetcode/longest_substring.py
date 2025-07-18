"""
Given a string s, find the length of the longest substring without duplicate characters.


"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        my_list = []
        result = 0
        for char in s:
            if char in my_list:
                index = my_list.index(char)
                my_list = my_list[index + 1:]

            my_list.append(char)
            result = max(result, len(my_list))

        return result


if __name__ == "__main__":
    solution = Solution()
    str = input("Enter string: ")
    result = solution.lengthOfLongestSubstring(str)
    print(result)