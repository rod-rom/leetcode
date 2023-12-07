# https://leetcode.com/problems/valid-parentheses/description/

def is_valid(s: str) -> bool:
    stack = []
    opening = ["(", "{", "["]
    for char in s:
        if char in opening:
            stack.append(char)
        else:
            if not stack:  # if stack is empty
                return False
            elif char == ")" and stack[-1] == "(":
                stack.pop()
            elif char == "]" and stack[-1] == "[":
                stack.pop()
            elif char == "}" and stack[-1] == "{":
                stack.pop()
            else:
                return False
    return not stack  # true, if stack is empty

# Alternative solution
# Time complexity: O(n)
# Space complexity: O(n)
# Trick: Use a stack to keep track of the opening brackets
def is_valid_alt(s: str) -> bool:
    stack = []
    bracket_map = {"(": ")", "[": "]", "{": "}"}

    for char in s:
        if char in bracket_map:  # if the character is an 'open' bracket
            stack.append(char)
        elif (
            not stack or bracket_map[stack.pop()] != char
        ):  # if the stack is empty or the top element does not match the 'close' bracket
            return False

    return not stack  # return True if stack is empty, False otherwise