'''
Given a sorted array and a target value, return the index if the target is found. If not,
return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
'''
class Solution:
    def searchInsert(self, nums, target):
        '''
        :param nums: List[int]
        :param target: int
        :return: int
        '''
        if len(nums) == 0:
            return 0
        elif target <= nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        elif target == nums[-1]:
            return len(nums) - 1
        else:
            for i in range(len(nums)):
                if target > nums[i]:
                    i += 1
                else:
                    return i


