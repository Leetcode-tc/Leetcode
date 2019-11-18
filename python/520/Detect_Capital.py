class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return re.match(r'([A-Z]+\b)|([a-z]+\b)|([A-Z][a-z]+\b)', word) is not None
