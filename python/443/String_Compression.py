class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i = 0
        k = -1  # 0 ~ k 表示已经用了的数组下标
        while i < len(chars):
            j = i + 1
            while j < len(chars) and chars[i] == chars[j]:
                j += 1
            chars[k+1] = chars[i] 
            k += 1
            if j - i > 1:
                for x in str(j - i):
                    chars[k+1] = x
                    k += 1
            i = j
        return k + 1
