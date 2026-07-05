class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        numsNew = sorted(set(nums))
        counts = [1]
        temp = 0
        for i in range(len(numsNew) - 1):
            if numsNew[i] + 1 == numsNew[i + 1]:
                print(counts)
                counts[temp] += 1
            else:
                temp += 1
                counts += [1]
        maxCounts = 0 
        print(counts)
        for i in range(len(counts)):
            if counts[i] > maxCounts:
                maxCounts = counts[i]
        return maxCounts