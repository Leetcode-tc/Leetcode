ass Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl',
                 '6':'mno', '7': 'pqrs', '8':'tuv', '9':'wxyz'}
        ret = []
        if len(digits) == 0:
            return ret 
        def dfs(digits, s):
            if len(digits) == 0:
                ret.append(s)
            else:
                for letter in phone[digits[0]]:
                    # s += letter
                    # dfs(digits[1:], s)
                    # s = s[:-1]
                    dfs(digits[1:], s+letter)
        dfs(digits, '')
        return ret
