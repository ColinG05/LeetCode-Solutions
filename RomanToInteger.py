class Solution(object):
    def romanToInt(self, s):
        total = 0
        curr = 0
        nums = list(s)

        while curr < len(nums):
            curr_char = nums[curr]

            if curr_char == "I":
                if curr + 1 < len(nums) and nums[curr + 1] == "V":
                    total += 4
                    curr += 2
                elif curr + 1 < len(nums) and nums[curr + 1] == "X":
                    total += 9
                    curr += 2
                else:
                    total += 1
                    curr += 1

            elif curr_char == "V":
                total += 5
                curr += 1

            elif curr_char == "X":
                if curr + 1 < len(nums) and nums[curr + 1] == "L":
                    total += 40
                    curr += 2
                elif curr + 1 < len(nums) and nums[curr + 1] == "C":
                    total += 90
                    curr += 2
                else:
                    total += 10
                    curr += 1

            elif curr_char == "L":
                total += 50
                curr += 1

            elif curr_char == "C":
                if curr + 1 < len(nums) and nums[curr + 1] == "D":
                    total += 400
                    curr += 2
                elif curr + 1 < len(nums) and nums[curr + 1] == "M":
                    total += 900
                    curr += 2
                else:
                    total += 100
                    curr += 1

            elif curr_char == "D":
                total += 500
                curr += 1

            elif curr_char == "M":
                total += 1000
                curr += 1

        return total
