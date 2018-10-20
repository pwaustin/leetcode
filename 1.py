def two_sum(nums, target):
    """
    Problem:
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    :type nums: List[int]
    :type target: int
    :rtype: List[int]

    Solution:
    Enroll all the nums in a dictionary as value/index pairs. For each number considered, see whether the
    matching value needed to attain the sum has already been enrolled. If found, return the indices, else -1.
    """

    my_dict = {}

    for i in range(0, len(nums)):
        complement = target - nums[i]
        if complement in my_dict:
            return [my_dict.get(complement), i]
        my_dict[nums[i]] = i
    return -1
