# Q. Given a list of natural numbers, find the largest increasing subsequence from it.
# Ans. Find the largest strictly increasing subsequence in a list of natural numbers.
# Approach
# Initialize an array dp where dp[i] stores the length of the longest increasing subsequence ending at index i.
# Use another array prev to track the indices of previous elements in the subsequence to reconstruct the LIS.
# Iterate through each element and for all previous elements less than current, update dp[i] if a longer subsequence is possible.
# Find the maximum length in dp and backtrack using prev array to build the largest increasing subsequence.

