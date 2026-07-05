class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        res = []
        zeros = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            else:
                total *= nums[i]
        
        for i in range(len(nums)):
            if zeros > 1:
                res += [0]
            elif zeros == 1:
                if not nums[i] == 0:
                    res += [0]
                else:
                    res += [int(total)]
            else:
                res += [int(total / nums[i])]
        return res
