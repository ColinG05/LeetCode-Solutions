class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        t= str(x) 
        rev  = t[::-1]
        if(t== rev): 
            return True 
        else: 
            return False
        
