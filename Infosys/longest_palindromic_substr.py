# Q. Longest Palindromic Substring Given a string s, return the longest palindromic substring in s. A string is called a palindrome if it reads the same forward and backward. Example 1: Input: s = "babad" Output: "bab" Explanation: "aba" is also a valid answer. Example 2: Input: s = "cbbd" Output: "bb" Constraints: 1 <= s.length <= 1000 s consist of only digits and English letters.
# Ans. Find the longest substring of a string that reads the same forwards and backwards.
# Approach
# Initialize variables to track the start and max length of the longest palindrome found.
# Iterate over the string, for each index expand around it to check for longest odd length palindrome.
# Similarly, expand around the gap between current and next index to check for longest even length palindrome.
# Update tracking variables whenever a longer palindrome is found during the expansions.
# Return the substring corresponding to the longest palindrome tracked.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        start, max_len = 0, 1

        def expand_around_center(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        for i in range(len(s)):
            len1 = expand_around_center(i, i)
            len2 = expand_around_center(i, i+1)
            curr_len = max(len1, len2)
            if curr_len > max_len:
                max_len = curr_len
                start = i - (curr_len - 1) // 2

        return s[start:start + max_len]