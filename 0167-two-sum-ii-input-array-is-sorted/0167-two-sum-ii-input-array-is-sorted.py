class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # d = {}
        # for i,num in enumerate(numbers):
        #     if target - num in d:
        #         return [d[target-num]+1,i+1]
        #     else:
        #         d[num]=i

        i, j = 0, len(numbers) - 1
        while i < j:
            total = numbers[i] + numbers[j]
            if total == target:
                return [i + 1, j + 1]
            elif total < target:
                i += 1
            else:
                j -= 1