class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        wordList = ['QWERTYUIOP', 'ASDFGHJKL', 'ZXCVBNM']
        res = []
        for x in words:
            line = 0
            for i in range(3):
                if x[0].upper() in wordList[i]:
                    line = i
                    break
            flag = True
            for c in x:
                if c.upper() not in wordList[line]:
                    flag = False
                    break
            if flag:
                res.append(x)
        return res



class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        wordList = [set('QWERTYUIOP'),set('ASDFGHJKL'),set('ZXCVBNM')]
        res = []
        for x in words:
            for y in wordList:
                if set(x.upper()) <= y:
                    res.append(x)
                    break
        return res