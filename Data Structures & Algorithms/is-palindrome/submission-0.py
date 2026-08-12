class Solution:
    def isPalindrome(self, s: str) -> bool:
        rev = ""
        clean = ""
        for char in s:
            if char.isalnum():
                clean += char.lower() 
                rev = char.lower() + rev
            
        if rev == clean:
            return True
        else:
            return False

        