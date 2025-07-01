class Solution:
    def isPalindrome(self, x: int) -> bool:
        my_number_str = str(x)
        formatted_number = my_number_str.replace(" ", "").lower()
        return formatted_number == formatted_number[::-1]
