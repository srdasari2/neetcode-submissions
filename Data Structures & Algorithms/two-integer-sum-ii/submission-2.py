class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while not numbers[i] + numbers[j] == target:
            if target < numbers[i] + numbers[j]:
                j -= 1
            elif target > numbers[i] + numbers[j]:
                i += 1
        return [i+1, j+1]