class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # Time complexity:O(nlogn) due to sorting
        # followed by O(n) for the sliding window
        # Space complexity:O(1) if sorting is done in-place
        nums.sort()
        j = 0
        max_length = 0

        for i in range(len(nums)):
            while nums[i] - nums[j] > 1:
                j += 1
            if nums[i] - nums[j] == 1:
                max_length = max(max_length, i - j + 1)
        
        return max_length
