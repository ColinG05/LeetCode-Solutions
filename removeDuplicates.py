
class Solution(object):
    def removeDuplicates(self, nums):
        count = 0
        unique = []

        for i in nums:
            if i not in unique:
                unique.append(i)
                count += 1

        for i in range(count):
            nums[i] = unique[i]

        return count
