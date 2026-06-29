class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for i in range(len(strs)):
            sortedString = "".join(sorted(strs[i]))
            if sortedString in res:
                res[sortedString].append(strs[i])
            else:
                res[sortedString] = [strs[i]]
        return list(res.values())
