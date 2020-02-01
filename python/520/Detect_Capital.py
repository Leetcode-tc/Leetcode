class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return re.match(r'([A-Z]+\b)|([a-z]+\b)|([A-Z][a-z]+\b)', word) is not None


class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        cnt = 0
        for c in word:
            if c.isupper():
                cnt += 1
        return cnt == len(word) or cnt == 0 or (cnt ==1 and word[0].isupper())
        
