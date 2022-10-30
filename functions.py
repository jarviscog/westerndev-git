import math
import pyfiglet
import warnings

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    l = len(nums)
    for i in range(0, l):
        for j in range(i + 1, l):
            if (nums[i] + nums[j]) == target:
                return [i, j]


if __name__ == '__main__':
    print_hi('WDS')
