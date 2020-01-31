class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        radius = 0
        heaters.sort()
        def findClosest(housePos):
            left, right = 0, len(heaters)-1
            while left <= right:
                mid = left + (right -left)/2
                if heaters[mid] == housePos:
                    return 0
                elif heaters[mid] > housePos:
                    right = mid -1
                else:
                    left = mid + 1
            res = 2 ** 31 -1
            if left < len(heaters):
                res = min(abs(heaters[left]-housePos), res)
            if right >= 0:
                res = min(abs(heaters[right]-housePos), res)
            return res
        for x in houses:
            dis = findClosest(x)
            radius = dis if dis > radius else radius
        return radius