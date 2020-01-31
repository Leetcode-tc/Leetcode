class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # a = dict(collections.Counter(ransomNote)) 
        # b = dict(collections.Counter(magazine))
        def myCounter(s):
            d = collections.defaultdict(int)
            for c in s:
                d[c] += 1
            return d
        a, b = myCounter(ransomNote), myCounter(magazine)
        for k,v in a.iteritems():
            if k not in b or v > b[k]:
                return False
        return True