class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        res = [1] * len(nums)

        for i in range(len(nums)):
            prefix[0] = nums[0]
            if i > 0:
                prefix[i] = prefix[i-1] * nums[i]
                print(f"Prefix array is: {prefix[i]}")
            j = len(nums) - 1 - i
            postfix[-1] = nums[-1]
            if j < len(nums) - 1:
                postfix[j] = postfix[j + 1] * nums[j]
                print(f"Postfix array is: {postfix[j]}")
        
        for i in range(len(nums)):
            if 0 < i < len(nums) - 1:
                res[i] = prefix[i-1] * postfix[i+1]

            res[0] = postfix[1]
            res[-1] = prefix[-2]
        
        return res
