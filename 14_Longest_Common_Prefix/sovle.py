class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        Finds the longest common prefix in a list of strings.

        This function takes a list of strings as an argument and returns
        the longest common prefix of all strings in the list.

        Args:
            strs (List[str]): A list of strings.

        Returns:
            str: The longest common prefix of all strings in the list.
        """
        # Sort the list of strings by length
        strs.sort(key=len)
        first = strs[0]
        last = strs[-1]
        
        # Find the minimum length of the first and last strings
        min_len = min(len(first), len(last))
        
        # Iterate through the characters of the first and last strings
        for i in range(min_len):
            # If the characters at the same index are different
            if first[i] != last[i]:
                # Return the substring of the first string up to the index
                return first[:i]
        # If the characters at the same index are the same for all strings
        # return the first string
        return first
            
solution = Solution()

print(solution.longestCommonPrefix(["flower", "flow", "flight"]))
