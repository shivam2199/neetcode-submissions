class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        idx_map = {}
        for i in range(len(nums)):
            idx_map[nums[i]] = i
        max_count = 0
        for i in range(len(nums)):
            count = 1
            curr = nums[i]
            if curr-1 not in idx_map:
                while curr+1 in idx_map:
                    count+=1
                    curr+=1
            max_count = max(max_count, count)
        
        return max_count