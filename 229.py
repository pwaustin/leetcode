def majority_element(nums):
    """
    Problem:
    Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in
    linear time and in O(1) space.

    :type nums: List[int]
    :rtype: List[int]

    Solution:
    There are at most two such elements. We implement a version of the Boyer-Moore majority vote algorithm with two
    candidates and two counts to do this in O(n) time and O(1) space. The first pass finds two candidate values, then
    we verify the candidates actually occurred at least the required number of times.
    """

    if not nums:
        return []

    count1, count2, candidate1, candidate2 = 0, 0, 0, 1

    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1 = num
            count1 = 1
        elif count2 == 0:
            candidate2 = num
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1

    return [n for n in (candidate1, candidate2) if nums.count(n) > len(nums) // 3]
