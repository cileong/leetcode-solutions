"""
Solution:

For each character in the input string,
push the character into the stack if it is an opening bracket,
otherwise pops a character from the stack and check if they match,
return false if they don't.
"""


class Solution:

    def isValid(self, s: str) -> bool:
        stack = []

        for bracket in s:
            if bracket == '(' or bracket == '[' or bracket == '{':
                stack.append(bracket)
            else:
                if stack:
                    opening_bracket = stack.pop()
                else:
                    return False

                if opening_bracket == '(' and bracket != ')':
                    return False
                elif opening_bracket == '[' and bracket != ']':
                    return False
                elif opening_bracket == '{' and bracket != '}':
                    return False
        
        return len(stack) == 0