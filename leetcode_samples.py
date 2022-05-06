# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c for c in s if c.isalnum()).lower()
        return s == s[::-1]


# 480 / 480 test cases passed.
# Status: Accepted
# Runtime: 46 ms
# Memory Usage: 14.6 MB




# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(list(s))
        sorted_t = sorted(list(t))
        return sorted_s == sorted_t


# 36 / 36 test cases passed.
# Status: Accepted
# Runtime: 47 ms
# Memory Usage: 15.6 MB




# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        
        for s in strs:
            sorted_str = ''.join(sorted(s))
            if sorted_str not in anagrams:
                anagrams[sorted_str] = []
            anagrams[sorted_str].append(s)
        return [list(v) for k, v in anagrams.items()]


# 115 / 115 test cases passed.
# Status: Accepted
# Runtime: 196 ms
# Memory Usage: 18.3 MB




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




# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and uses only constant extra space.

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num_counts = {}
        for _, v in enumerate(nums):
            num_counts[v] = 1 if v not in num_counts else num_counts[v] + 1
        return [i for i in num_counts if num_counts[i] > 1][0]


# 58 / 58 test cases passed.
# Status: Accepted
# Runtime: 953 ms
# Memory Usage: 35.9 MB




# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        new_arr = []
        runningTotal = 0
        for k, v in enumerate(nums):
            if k == 0:
                new_arr.append(v)
                runningTotal = v
            else:
                runningTotal = runningTotal + v
                new_arr.append(runningTotal)
        return new_arr


# 53 / 53 test cases passed.
# Status: Accepted
# Runtime: 60 ms
# Memory Usage: 14.1 MB




# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        s = [0,1]
        for i in range(n + 1):
            if i > 1:
                s.append(s[-1] + s[-2])
        return s[-1]


# 31 / 31 test cases passed.
# Status: Accepted
# Runtime: 38 ms
# Memory Usage: 13.9 MB




# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return [num**2 for num in sorted(nums, key=abs)]


# 137 / 137 test cases passed.
# Status: Accepted
# Runtime: 244 ms
# Memory Usage: 16.4 MB




# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return True if len(set(nums)) != len(nums) else False


# 70 / 70 test cases passed.
# Status: Accepted
# Runtime: 508 ms
# Memory Usage: 26.1 MB




# You are given a string title consisting of one or more words separated by a single space, where each word consists of English letters. Capitalize the string by changing the capitalization of each word such that:

# If the length of the word is 1 or 2 letters, change all letters to lowercase.
# Otherwise, change the first letter to uppercase and the remaining letters to lowercase.
# Return the capitalized title.

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words_arr = title.split(" ")
        for index, word in enumerate(words_arr):
            if len(word) < 3:
                words_arr[index] = word.lower()
            else:
                words_arr[index] = word.capitalize()
        return " ".join(words_arr)


# 200 / 200 test cases passed.
# Status: Accepted
# Runtime: 43 ms
# Memory Usage: 13.8 MB




# There is a programming language with only four operations and one variable X:

# ++X and X++ increments the value of the variable X by 1.
# --X and X-- decrements the value of the variable X by 1.
# Initially, the value of X is 0.

# Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for operation in operations:
            if "-" in operation:
                x -= 1
            else:
                x += 1
        return x


# 259 / 259 test cases passed.
# Status: Accepted
# Runtime: 80 ms
# Memory Usage: 13.8 MB





# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

class Solution:
    def longestPalindrome(self, s: str) -> int:
        str_len = len(s)
        if str_len == 0:
            return 0 
        if str_len == 1:
            return 1 

        char_count = {}
        contains_odd = False
        palindrome_len = 0

        for c in s:
            char_count[c] = char_count.get(c, 0) + 1

        for char in char_count:
            if char_count[char] % 2 == 0:
                palindrome_len += char_count[char]
            else:
                palindrome_len += char_count[char]-1
                contains_odd = True

        return palindrome_len + 1 if contains_odd else palindrome_len


# 95 / 95 test cases passed.
# Status: Accepted
# Runtime: 33 ms
# Memory Usage: 13.8 MB
