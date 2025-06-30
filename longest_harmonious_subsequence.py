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

## Solution 2: Using Hashmaps
from collections import Counter

class Solution:
    def findLHS(self, nums: list[int]) -> int:
        # Using HashMaps
        # Time complexity: O(n)
        # Space complexity:O(n)
        frequency_map = Counter(nums)
        max_length = 0

        for num in frequency_map:
            if num + 1 in frequency_map:
                current_length = frequency_map[num] + frequency_map[num + 1]
                max_length = max(max_length, current_length)

        return max_length
