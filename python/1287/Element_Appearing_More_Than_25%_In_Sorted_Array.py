class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        cur, cnt = arr[0], 1
        for i in range(1, n):
            if arr[i] == cur:
                cnt += 1
                if cnt * 4 > n:
                    return cur
            else:
                cur, cnt = arr[i], 1
        return cur

