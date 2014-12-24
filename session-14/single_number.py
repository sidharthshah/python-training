#Solution to: https://oj.leetcode.com/problems/single-number/
from collections import defaultdict

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        counts = defaultdict(int)
        for x in A:
            counts[x] += 1
        
        for k,v in counts.items():
            if v == 1:
                return k

if __name__ == "__main__":
    s = Solution()
    print s.singleNumber([1,2,3,4,5,2,3,4,5])
    print s.singleNumber([1,2,2,1,3,3,4,4,5,6,5])
