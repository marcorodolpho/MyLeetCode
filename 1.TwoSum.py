#The link for this problem on LeetCode: https://leetcode.com/problems/two-sum/description/
#I used the default code from leetcode and built from it

class Solution(object):     

    def twoSum(self, nums, target):

        seen_numbers =  {}
        results = []

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen_numbers:
                results.append([seen_numbers[complement], i])
                
            seen_numbers[num] = i

        return results
    
#Creating a way to execute a local test

nums = list(map(int, input("Type the numbers:   ").split()))
target = int(input("Type the target:  "))

solution = Solution()
result = solution.twoSum(nums, target)

print(result)            

