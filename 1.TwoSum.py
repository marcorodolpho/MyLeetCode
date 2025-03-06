#The link for this problem on LeetCode: https://leetcode.com/problems/two-sum/description/
#I used the default code from leetcode and built from it

class Solution(object):     

    def twoSum(self, nums, target):

        seen_numbers =  {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen_numbers:
                return [seen_numbers[complement], i]
            
            seen_numbers[num] = i

            

