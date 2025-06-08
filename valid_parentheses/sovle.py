class Solution:
    def isValid(self, s: str) -> bool:
        """
        Determine if the input string of parentheses is valid.
        
        A string is considered valid if:
        - Open brackets are closed by the same type of brackets.
        - Open brackets are closed in the correct order.

        Args:
            s (str): The input string containing only '(', ')', '{', '}', '[' and ']'.

        Returns:
            bool: True if the input string is valid, False otherwise.
        """
        stack = []  # Initialize an empty stack to keep track of opening brackets
        for i in range(len(s)):
            # Check if character is an opening bracket
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                stack.append(s[i])  # Push the opening bracket onto the stack
            else:
                # Check if the stack is non-empty and the top of the stack matches the closing bracket
                if stack and (
                    (stack[-1] == "(" and s[i] == ")")
                    or (stack[-1] == "{" and s[i] == "}")
                    or (stack[-1] == "[" and s[i] == "]")
                ):
                    stack.pop()  # Pop the top of the stack if the brackets match
                else:
                    return False  # Return False if the brackets do not match
        return len(stack) == 0  # Return True if stack is empty, indicating a valid string


solution = Solution()


print(solution.isValid("{([])}"))
