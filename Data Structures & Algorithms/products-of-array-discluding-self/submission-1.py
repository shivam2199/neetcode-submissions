class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right_prod = [1]*len(nums)
        left_prod = [1]*len(nums)

        for i in range(1, len(nums)):
            right_prod[i] = right_prod[i-1] * nums[i-1]
        
        for i in range(len(nums)-2, -1, -1):
            left_prod[i] = left_prod[i+1] * nums[i+1]

        res = []
        for i in range(len(nums)):
            res.append(right_prod[i]*left_prod[i])
        
        return res


