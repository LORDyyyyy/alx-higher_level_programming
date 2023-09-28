#!/usr/bin/python3
""" find_peak function """


def find_peak(nums):
    """
    Finds the peak number of a list.
    The peak is a number that's bigger than or eaual to his neighbors.

    Args:
        nums: an unsorted list of integers

    Return:
        the peak number, only 1 number if there many answers.
    """

    if len(nums) == 0:
        return None

    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return nums[left]
