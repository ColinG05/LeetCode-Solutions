class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash = {} # hashmap 
        for i in range(len(nums)): #get values in hashma 
            hash[nums[i]]=i #find proper index in hashmap to store value at 
        # from here you can just check every index, if you remove this element from hash, and the leftover number has a value, then the solution exist with this element, else it does 
        for i in range(len(nums)):
            second = target - nums[i]
            if second in hash and hash[second] != i:
                return [i, hash[second]]
        return[]
        
