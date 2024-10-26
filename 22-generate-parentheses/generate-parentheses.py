class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        1. Base Case : N == OpenN == ClosedN return 
        2. Add OpenBrackets: OpenN < n
        3. Add closedBrackets: ClosedN < openN
        """
        stack = []
        res = []
        def backtrack(openN, closedN):
            if openN == closedN == n: 
                res.append(("".join(stack)))
                return
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
        backtrack(0,0)
        return res