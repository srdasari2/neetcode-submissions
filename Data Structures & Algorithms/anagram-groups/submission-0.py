class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        res["".join(sorted(strs[0]))] = [strs[0]]
        print(res)
        for i in range(1, len(strs)):
            sortedString = "".join(sorted(strs[i]))
            if sortedString in res:
                res[sortedString].append(strs[i])
            else:
                res[sortedString] = [strs[i]]
        print(res.values())
        return list(res.values())
