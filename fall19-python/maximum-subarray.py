# O(n)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # iterate over integer array starting at second element in array
        for i in range(1, len(nums)):
            # if the integer before the current integer is positive, we want to add
            # the previous number to the current to get the current sum of the 
            # contiguous subarray
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            # otherwise, if the previous number is negative don't add it because it will
            # decrease the current sum
            # which breaks the contiguous subarray and moves onto the next
            
        #return the max sum of all the sums
        return max(nums)
    
# O(n)

class Solution:
    def maxSubArray(self, A):
        
        currSum = A[0]
        maxSum = A[0]
        for num in A[1:]:
            currSum = max(num, currSum+num)
            maxSum = max(maxSum, currSum)
        return maxSum
