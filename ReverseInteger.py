class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative =0 

        

        if x<0:
            negative =1 
            x = x*-1  
            
        s = str(x)
        srev = s[::-1]
        


        if negative:
            inrev= int(srev)*-1
            if(inrev< (-2**31)):
                return 0 
            else: 
                return inrev
        else: 
            inrev =  int(srev)
            if(inrev> ( 2**31)):
                return 0 
            else: 
                return inrev

       
        
        
