class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        r = len(digits) - 1
        carry = (digits[r] + 1) // 10
        digits[r] = (digits[r] + 1) % 10
        r -= 1
        while carry > 0 and r >= 0:
            
            addition = digits[r] + carry
            digits[r] = addition % 10
            carry = addition // 10

            r -= 1
        
        if carry > 0:
            digits = [1] + digits
        return digits
            
            
        