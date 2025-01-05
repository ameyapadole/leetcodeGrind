class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        res = []
        indexRemove = set()

        for i, c in enumerate(s):
            if c not in "()":
                continue 
            if c == "(":
                stack.append(i)
            elif not stack:
                indexRemove.add(i)
            else:
                stack.pop()
        
        indexRemove = indexRemove.union(set(stack))

        for i,c in enumerate(s):
            if i not in indexRemove:
                res.append(c)
        return "".join(res)
        