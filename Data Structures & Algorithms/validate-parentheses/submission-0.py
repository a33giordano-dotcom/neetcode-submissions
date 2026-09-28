class Solution:
    def isValid(self, s: str) -> bool:
        mapper = {")":"(", "}":"{", "]":"["}
        stack = []

        
        for c in s:
            if c in mapper:
                if stack and stack[-1] == mapper[c]:
                    stack.pop()
                else:
                    return False 
            else:
                stack.append(c)
        return True if not stack else False 