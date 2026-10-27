class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        temp = []
        sNums = sorted(nums)
        print(sNums)
        a = []
        
        for i in range(len(nums) - 2):
            
            if sNums[i] in a:
                continue
            elif sNums[i] > 0:
                break
                
            else:
                a += [sNums[i]]
                #print(a)
                b = []
                l = i + 1
                r = len(sNums) - 1
                while l < r:
                    if sNums[l] in b:
                        l += 1
                        continue
                    if sNums[r] + sNums[l] < -sNums[i]:
                        l += 1
                    elif sNums[r] + sNums[l] > -sNums[i]:
                        r -= 1
                    else:
                        if not [sNums[i], sNums[l], sNums[r]] in temp:
                            temp += [[sNums[i], sNums[l], sNums[r]]]
                            b += [sNums[l]]
                        l += 1
                        r -= 1
                        
        return temp
            