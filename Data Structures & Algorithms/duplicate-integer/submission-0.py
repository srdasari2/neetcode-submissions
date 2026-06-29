class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        table = {}
        for i in range(len(nums)):
            if nums[i] in table:
                return True
            else:
                table[nums[i]] = i
        return False