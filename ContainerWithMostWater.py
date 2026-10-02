class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # easiest solution is just to bruteforce, check all possible pairs compute area and see what is best 

        #best solution is probably sliding window type solution, we can start with max width
        # and then keep moving the smallest index from L-R to the next one , essentially 
        #whatever height is restricting the object from growing is the suboptimal option so we move it one closer

        #we just keep track of max area possible 

        ans = 0 

        l=0 
        r= len(height) -1 

        while l<r: 
            ans = max(ans, (min(height[r],height[l])* (r-l)))

            if height[l] <height[r]: #right is the one restricting 
                l+= 1 
            else: 
                r-=1
            
        return ans


        
