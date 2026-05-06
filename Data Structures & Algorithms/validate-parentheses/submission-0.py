class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closedOnes = {")": "(",
                    "]": "[",
                    "}":"{"}
        
        for c in s:
            if c in closedOnes:
                if stack and stack[-1]==closedOnes[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

        