class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_map = {}
        res = [-1]*2
        for i in range (len(nums)):
            idx_map[nums[i]] = i
        for j in range (len(nums)):
            diff = target - nums[j]
            if diff in idx_map and idx_map[diff] > j:
                res[0] = j
                res[1] = idx_map[diff]
                break
        
        return res
