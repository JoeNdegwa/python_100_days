## Space Complexity O(N)
## Time Complexity O(N)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        my_number_str = str(x)
        formatted_number = my_number_str.replace(" ", "").lower()
        return formatted_number == formatted_number[::-1]

## 100% Solution
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        rev = 0
        num = x
        
        while num != 0:
            rev = rev * 10 + num % 10
            num = num // 10
        
        return rev == x
