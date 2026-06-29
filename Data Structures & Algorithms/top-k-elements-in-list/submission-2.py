class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1
        print(len(d))
        if len(d) == 0:
            return []
        sortedData = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        sortedKeys = list(sortedData.keys())
        print(sortedKeys)
        temp = []
        for i in range(k):
            temp.append(sortedKeys[i])
        return temp
        