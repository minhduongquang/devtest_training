# Step 1 – Basic Implementation	"Write a Python function named `kth_smallest_basic(nums: List[int], k: int) -> int`.
# This function should return the k-th smallest number in the list by using a simple approach.
# You can use built-in methods like sorting."
######
# Your code here
from typing import List

def kth_smallest_basic(nums: List[int], k: int) -> int:
    # Sort the list in ascending order
    sorted_nums = sorted(nums)
    # Return the k-th smallest element (k-1 due to zero-based indexing)
    return sorted_nums[k - 1]

# Step 2 – Analysis and Explanation	"Explain the advantages and disadvantages of your solution in Step 1.
# Include:
# - Time complexity in Big O notation
# - Space complexity
# - When this solution might be acceptable or unacceptable in practice"
#######
# Your code here
 
 
# Step 3 – Advanced Optimization	"Propose an optimized version of your solution that improves on the time or space complexity.
# You are allowed to use algorithms like Quickselect, Heap, or other appropriate data structures.
# Explain the improvement in performance and any trade-offs involved."
#####
# Your code here