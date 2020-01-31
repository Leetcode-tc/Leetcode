class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        tmp = [-1]
        for i in range(len(arr)-1,0,-1):
            tmp.append(arr[i]) if arr[i] > tmp[-1] else tmp.append(tmp[-1])
        return tmp[::-1]

