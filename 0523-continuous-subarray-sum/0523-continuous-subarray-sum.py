class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums)<=1:
            return False
        d = {0:-1}
        prefix_sum = 0
        for index, num in enumerate(nums):
            prefix_sum += num
            mod = prefix_sum % k 
            if mod in d and index - d[mod] >= 2:
                return True
            
            if mod not in d:
                d[mod] = index
        
        return False