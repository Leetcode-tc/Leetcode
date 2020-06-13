class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 时间复杂度 O(n)
        a, b = 0, 1
        for i in range(n):
            a, b = b, a+b
        return b
    
    
    # 时间复杂度 O(lgn)
    def climbStairs_2(self, n):
        """
        :type n: int
        :rtype: int
        """
        # [
        #   [Fn+1, Fn  ],
        #   [Fn,   Fn-1]
        # ]
        # matrix ** n
        
        matrix = [
                    [1, 1], 
                    [1, 0]
                 ]
        def fibonacci(n):
            if n == 1:
                return matrix
            else:
                half_matrix = fibonacci(n/2)
                res = matrix_mul(half_matrix, half_matrix)
                return matrix_mul(res, matrix) if n&1 else res
            
        def matrix_mul(m1, m2):
            return [[
                        m1[0][0]*m2[0][0]+m1[0][1]*m2[1][0], 
                        m1[0][0]*m2[0][1]+m1[0][1]*m2[1][1]
                        ], 
                    [
                        m1[1][0]*m2[0][0]+m1[1][1]*m2[1][0],
                        m1[1][0]*m2[0][1]+m1[1][1]*m2[1][1]
                        ]
                    ]
        return fibonacci(n)[0][0]

        # f0   f1  f2  f3  f4
        #  0   1   1    2   3
        #      1   2    3   5
