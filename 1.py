def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    my_dict = {}
    for i in range(0, len(nums)):
        complement = target - nums[i]
        if complement in my_dict:
            return [my_dict.get(complement),i]
        my_dict[nums[i]] = i
    return -1