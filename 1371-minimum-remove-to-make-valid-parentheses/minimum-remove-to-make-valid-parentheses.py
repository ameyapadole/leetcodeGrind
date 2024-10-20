class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        output = []
        indexRemove = set()

        for i ,c in enumerate(s):   
            if c not in "()":
                continue
            if c == "(":
                stack.append(i)
            elif not stack:
                indexRemove.add(i)
            else:
                stack.pop()

        indexRemove = indexRemove.union(set(stack))

        for i, c in enumerate(s):
            if i not in indexRemove:
                output.append(c)

        return "".join(output)     