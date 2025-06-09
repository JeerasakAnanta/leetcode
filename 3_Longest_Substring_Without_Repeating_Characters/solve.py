# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without duplicate characters.
# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.


class Solution:
    """
    Given a string s, find the length of the longest substring without duplicate characters.

    Returns:
        int: The length of the longest substring without duplicate characters.
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        The function takes a string s and returns the length of the longest substring
        without duplicate characters.
        """
        # The number of characters in the string
        num_of_str = len(s)

        # The result of the longest substring without duplicate characters
        res = 0

        # Iterate over the string
        for i in range(num_of_str):
            # A boolean array to store the characters we have seen
            vis = [False] * 26

            # Iterate over the string from i to the end
            for j in range(i, num_of_str):
                # If we have seen the character before, break the loop
                if vis[ord(s[j]) - ord("a")]:
                    break
                # If not, mark the character as seen
                else:
                    vis[ord(s[j]) - ord("a")] = True
                    # Update the result if we have seen a longer substring
                    res = max(res, j - i + 1)
        # Return the result
        return res


test = Solution()
print(test.lengthOfLongestSubstring("abcabcbb"))  # 3
print(test.lengthOfLongestSubstring("bbbbb"))  #  1
print(test.lengthOfLongestSubstring("pwwkew"))  #  3
print(test.lengthOfLongestSubstring("geeksforgeeks"))  #  7
