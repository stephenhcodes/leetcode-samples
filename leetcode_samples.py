# Number of Laser Beems in a Bank

# Anti-theft security devices are activated inside a bank. You are given a 0-indexed binary string array bank representing the floor plan of the bank, which is an m x n 2D matrix. bank[i] represents the ith row, consisting of '0's and '1's. '0' means the cell is empty, while'1' means the cell has a security device.

# There is one laser beam between any two security devices if both conditions are met:

# The two devices are located on two different rows: r1 and r2, where r1 < r2.
# For each row i where r1 < i < r2, there are no security devices in the ith row.

# Laser beams are independent, i.e., one beam does not interfere nor join with another.

# Return the total number of laser beams in the bank.

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        tmp = [r.count('1') for r in bank if r.count('1') > 0]
        num_of_beams = 0
        if len(tmp) == 1:
            return num_of_beams
        for i in range(1, len(tmp)):
            num_of_beams += tmp[i] * tmp[i - 1]
        return num_of_beams


# 146 / 146 test cases passed.
# Status: Accepted
# Runtime: 158 ms
# Memory Usage: 16.1 MB




# Power of Four Problem

# Given an integer n, return true if it is a power of four. Otherwise, return false.

# An integer n is a power of four if there exists an integer x such that n == 4x.

import math

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return math.log(n, 4) % 1 == 0 if n > 0 else False


# 1061 / 1061 test cases passed.
# Status: Accepted
# Runtime: 36 ms
# Memory Usage: 13.9 MB




# Single Number Problem

# Given a non-empty array of integer nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and only use constant extra space.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return [x for x in nums if nums.count(x) == 1][0]


# 61 / 61 test cases passed.
# Status: Accepted
# Runtime: 8275 ms
# Memory Usage: 16.7 MB




# Majority Element Problem

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than [n / 2] times.

import numpy as np
from scipy import stats

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return np.array(stats.mode(nums))[0][0]


# 47 / 47 test cases passed.
# Status: Accepted
# Runtime: 862 ms
# Memory Usage: 62.5 MB




# Fizz Buzz Problem

# Given an integer n, return a string array answer (1-indexed) where:

# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        new_arr = []

        for i in range(n + 1):
            if i == 0: continue
            if i % 3 == 0 and i % 5 == 0:
                new_arr.append('FizzBuzz')
            elif i % 3 == 0:
                new_arr.append('Fizz')
            elif i % 5 == 0:
                new_arr.append('Buzz')
            else:
                new_arr.append(str(i))

        return new_arr


# 8 / 8 test cases passed.
# Status: Accepted
# Runtime: 55 ms
# Memory Usage: 14.9 MB

