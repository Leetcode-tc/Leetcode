ass Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = {'13#': 'm', '11#': 'k', '25#': 'y', '17#': 'q', '23#': 'w', '15#': 'o', '21#': 'u', '19#': 's', '18#': 'r', '1': 'a', '3': 'c', '2': 'b', '5': 'e', '4': 'd', '7': 'g', '6': 'f', '9': 'i', '8': 'h', '26#': 'z', '12#': 'l', '24#': 'x', '10#': 'j', '22#': 'v', '16#': 'p', '20#': 't', '14#': 'n'}
        i= len(s)-1
        res = ""
        while i >= 0:
            if s[i] == '#':
                tmp = s[i-2:i+1]
                res += d[tmp]
                i -= 3
            else:
                res += d[s[i]]
                i -= 1
        return res[::-1]


