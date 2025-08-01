"""
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, find the starting 
and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Examples:
- nums = [5,7,7,8,8,10], target = 8 -> Output: [3,4]
- nums = [5,7,7,8,8,10], target = 6 -> Output: [-1,-1]
- nums = [], target = 0 -> Output: [-1,-1]

Constraints:
- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
- nums is a non-decreasing array
- -10^9 <= target <= 10^9
"""

from typing import List


class Solution:
    """LeetCode style solution class."""
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Find the starting and ending position of target in sorted array.
        Using two binary searches: one for leftmost, one for rightmost position.
        
        Args:
            nums: Sorted array in non-decreasing order
            target: Target value to find
            
        Returns:
            List [start, end] positions, or [-1, -1] if not found
        """
        if not nums:
            return [-1, -1]
        
        def find_leftmost(nums: List[int], target: int) -> int:
            """Find the leftmost position of target."""
            left, right = 0, len(nums) - 1
            result = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    result = mid
                    right = mid - 1  # Continue searching left
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return result
        
        def find_rightmost(nums: List[int], target: int) -> int:
            """Find the rightmost position of target."""
            left, right = 0, len(nums) - 1
            result = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    result = mid
                    left = mid + 1  # Continue searching right
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return result
        
        left_pos = find_leftmost(nums, target)
        if left_pos == -1:
            return [-1, -1]
        
        right_pos = find_rightmost(nums, target)
        return [left_pos, right_pos]


def search_range_single_pass(nums: List[int], target: int) -> List[int]:
    """
    Alternative approach using a single modified binary search.
    
    Args:
        nums: Sorted array in non-decreasing order
        target: Target value to find
        
    Returns:
        List [start, end] positions, or [-1, -1] if not found
    """
    if not nums:
        return [-1, -1]
    
    def binary_search_bound(nums: List[int], target: int, find_left: bool) -> int:
        """
        Generic binary search to find left or right boundary.
        
        Args:
            nums: Sorted array
            target: Target value
            find_left: True to find leftmost, False to find rightmost
            
        Returns:
            Index of boundary, or -1 if not found
        """
        left, right = 0, len(nums) - 1
        result = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                result = mid
                if find_left:
                    right = mid - 1  # Search left for leftmost
                else:
                    left = mid + 1   # Search right for rightmost
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return result
    
    left_bound = binary_search_bound(nums, target, True)
    if left_bound == -1:
        return [-1, -1]
    
    right_bound = binary_search_bound(nums, target, False)
    return [left_bound, right_bound]


def search_range_expand(nums: List[int], target: int) -> List[int]:
    """
    Find target first, then expand left and right (not O(log n) in worst case).
    
    Args:
        nums: Sorted array in non-decreasing order
        target: Target value to find
        
    Returns:
        List [start, end] positions, or [-1, -1] if not found
    """
    if not nums:
        return [-1, -1]
    
    # First, find any occurrence of target using standard binary search
    left, right = 0, len(nums) - 1
    found_index = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            found_index = mid
            break
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    if found_index == -1:
        return [-1, -1]
    
    # Expand left and right from found position
    start = found_index
    end = found_index
    
    # Expand left
    while start > 0 and nums[start - 1] == target:
        start -= 1
    
    # Expand right
    while end < len(nums) - 1 and nums[end + 1] == target:
        end += 1
    
    return [start, end]


def search_range_linear(nums: List[int], target: int) -> List[int]:
    """
    Linear search approach (O(n) - not optimal but correct).
    
    Args:
        nums: Sorted array in non-decreasing order
        target: Target value to find
        
    Returns:
        List [start, end] positions, or [-1, -1] if not found
    """
    if not nums:
        return [-1, -1]
    
    start = -1
    end = -1
    
    for i, num in enumerate(nums):
        if num == target:
            if start == -1:
                start = i
            end = i
    
    return [start, end] if start != -1 else [-1, -1]


def test_solution():
    """Test all solutions with example cases."""
    test_cases = [
        ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
        ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
        ([], 0, [-1, -1]),
        ([1], 1, [0, 0]),
        ([1], 2, [-1, -1]),
        ([2, 2], 2, [0, 1]),
        ([1, 2, 3], 2, [1, 1]),
        ([1, 1, 1, 1, 1], 1, [0, 4]),
        ([1, 2, 2, 2, 3], 2, [1, 3]),
        ([5, 7, 7, 8, 8, 10], 5, [0, 0]),
        ([5, 7, 7, 8, 8, 10], 10, [5, 5]),
        ([1, 3, 3, 3, 3, 3, 3, 5], 3, [1, 6]),
    ]
    
    solution = Solution()
    
    print("Testing Solution.searchRange (Two Binary Searches):")
    for nums, target, expected in test_cases:
        result = solution.searchRange(nums, target)
        status = "✓" if result == expected else "✗"
        print(f"{status} nums={nums}, target={target} -> {result} (expected: {expected})")
    
    print("\nTesting search_range_single_pass (Single Binary Search Function):")
    for nums, target, expected in test_cases:
        result = search_range_single_pass(nums, target)
        status = "✓" if result == expected else "✗"
        print(f"{status} nums={nums}, target={target} -> {result} (expected: {expected})")
    
    print("\nTesting search_range_expand (Find and Expand - not always O(log n)):")
    for nums, target, expected in test_cases:
        result = search_range_expand(nums, target)
        status = "✓" if result == expected else "✗"
        print(f"{status} nums={nums}, target={target} -> {result} (expected: {expected})")
    
    print("\nTesting search_range_linear (Linear Search):")
    for nums, target, expected in test_cases:
        result = search_range_linear(nums, target)
        status = "✓" if result == expected else "✗"
        print(f"{status} nums={nums}, target={target} -> {result} (expected: {expected})")


def demonstrate_algorithm_steps():
    """Demonstrate step-by-step execution of the algorithm."""
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    
    print(f"Demonstrating algorithm with nums = {nums}, target = {target}")
    print("Expected result: [3, 4]")
    print()
    
    solution = Solution()
    
    print("Two Binary Search approach:")
    print("1. Find leftmost position of target")
    print("2. Find rightmost position of target")
    print("3. Return [leftmost, rightmost]")
    print()
    
    # Simulate finding leftmost
    print("Finding leftmost position:")
    left, right = 0, len(nums) - 1
    result = -1
    step = 1
    
    while left <= right:
        mid = (left + right) // 2
        print(f"Step {step}: left={left}, right={right}, mid={mid}, nums[mid]={nums[mid]}")
        
        if nums[mid] == target:
            result = mid
            print(f"Found target at {mid}, but continue searching left for leftmost")
            right = mid - 1
        elif nums[mid] < target:
            print(f"nums[mid] < target, search right half")
            left = mid + 1
        else:
            print(f"nums[mid] > target, search left half")
            right = mid - 1
        
        step += 1
    
    leftmost = result
    print(f"Leftmost position: {leftmost}")
    print()
    
    # Simulate finding rightmost
    print("Finding rightmost position:")
    left, right = 0, len(nums) - 1
    result = -1
    step = 1
    
    while left <= right:
        mid = (left + right) // 2
        print(f"Step {step}: left={left}, right={right}, mid={mid}, nums[mid]={nums[mid]}")
        
        if nums[mid] == target:
            result = mid
            print(f"Found target at {mid}, but continue searching right for rightmost")
            left = mid + 1
        elif nums[mid] < target:
            print(f"nums[mid] < target, search right half")
            left = mid + 1
        else:
            print(f"nums[mid] > target, search left half")
            right = mid - 1
        
        step += 1
    
    rightmost = result
    print(f"Rightmost position: {rightmost}")
    print(f"\nFinal result: [{leftmost}, {rightmost}]")
    print(f"Actual result: {solution.searchRange(nums, target)}")


def demonstrate_edge_cases():
    """Demonstrate handling of edge cases."""
    edge_cases = [
        ([], 0, "Empty array"),
        ([1], 1, "Single element - found"),
        ([1], 2, "Single element - not found"),
        ([1, 1, 1], 1, "All elements same"),
        ([1, 2, 3], 4, "Target larger than all elements"),
        ([2, 3, 4], 1, "Target smaller than all elements"),
        ([1, 3, 5], 3, "Single occurrence in middle"),
        ([1, 1, 2, 2, 2, 3, 3], 2, "Multiple occurrences"),
    ]
    
    solution = Solution()
    
    print("Edge Cases Demonstration:")
    for nums, target, description in edge_cases:
        result = solution.searchRange(nums, target)
        print(f"{description}:")
        print(f"  nums = {nums}, target = {target}")
        print(f"  result = {result}")
        print()


if __name__ == "__main__":
    print("=== Find First and Last Position of Element in Sorted Array ===\n")
    
    # Run example test cases
    solution = Solution()
    
    # Example 1
    nums1 = [5, 7, 7, 8, 8, 10]
    target1 = 8
    result1 = solution.searchRange(nums1, target1)
    print(f"Example 1: nums = {nums1}, target = {target1} -> {result1}")
    
    # Example 2
    nums2 = [5, 7, 7, 8, 8, 10]
    target2 = 6
    result2 = solution.searchRange(nums2, target2)
    print(f"Example 2: nums = {nums2}, target = {target2} -> {result2}")
    
    # Example 3
    nums3 = []
    target3 = 0
    result3 = solution.searchRange(nums3, target3)
    print(f"Example 3: nums = {nums3}, target = {target3} -> {result3}")
    
    print("\n" + "="*60)
    
    # Demonstrate algorithm steps
    demonstrate_algorithm_steps()
    
    print("\n" + "="*60)
    
    # Demonstrate edge cases
    demonstrate_edge_cases()
    
    print("="*60)
    
    # Run comprehensive tests
    test_solution()
