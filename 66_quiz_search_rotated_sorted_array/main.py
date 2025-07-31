"""
33. Search in Rotated Sorted Array

There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown 
pivot index k such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], 
nums[0], nums[1], ..., nums[k-1]].

Given the array nums after the possible rotation and an integer target, return 
the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Examples:
- nums = [4,5,6,7,0,1,2], target = 0 -> Output: 4
- nums = [4,5,6,7,0,1,2], target = 3 -> Output: -1
- nums = [1], target = 0 -> Output: -1

Constraints:
- 1 <= nums.length <= 5000
- -10^4 <= nums[i] <= 10^4
- All values of nums are unique
- nums is an ascending array that is possibly rotated
- -10^4 <= target <= 10^4
"""

from typing import List


class Solution:
    """LeetCode style solution class."""
    
    def search(self, nums: List[int], target: int) -> int:
        """
        Search for target in rotated sorted array using binary search.
        
        Args:
            nums: Rotated sorted array with distinct values
            target: Target value to find
            
        Returns:
            Index of target if found, -1 otherwise
        """
        if not nums:
            return -1
        
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Found target
            if nums[mid] == target:
                return mid
            
            # Determine which half is sorted
            if nums[left] <= nums[mid]:
                # Left half is sorted
                if nums[left] <= target < nums[mid]:
                    # Target is in left half
                    right = mid - 1
                else:
                    # Target is in right half
                    left = mid + 1
            else:
                # Right half is sorted
                if nums[mid] < target <= nums[right]:
                    # Target is in right half
                    left = mid + 1
                else:
                    # Target is in left half
                    right = mid - 1
        
        return -1


def search_rotated_array_two_step(nums: List[int], target: int) -> int:
    """
    Two-step approach: first find pivot, then binary search.
    
    Args:
        nums: Rotated sorted array with distinct values
        target: Target value to find
        
    Returns:
        Index of target if found, -1 otherwise
    """
    if not nums:
        return -1
    
    n = len(nums)
    
    # Step 1: Find the pivot (minimum element) index
    def find_pivot():
        left, right = 0, n - 1
        
        # Array is not rotated
        if nums[left] <= nums[right]:
            return 0
        
        while left <= right:
            mid = (left + right) // 2
            
            # Found pivot
            if mid < n - 1 and nums[mid] > nums[mid + 1]:
                return mid + 1
            if mid > 0 and nums[mid - 1] > nums[mid]:
                return mid
            
            # Decide which half to search
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        
        return 0
    
    # Step 2: Binary search in the appropriate half
    def binary_search(start: int, end: int) -> int:
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1
    
    pivot = find_pivot()
    
    # Search in left part [0, pivot-1]
    if pivot > 0 and nums[0] <= target <= nums[pivot - 1]:
        return binary_search(0, pivot - 1)
    
    # Search in right part [pivot, n-1]
    if nums[pivot] <= target <= nums[n - 1]:
        return binary_search(pivot, n - 1)
    
    return -1


def search_rotated_array_linear(nums: List[int], target: int) -> int:
    """
    Linear search approach (O(n) - not optimal but correct).
    
    Args:
        nums: Rotated sorted array with distinct values
        target: Target value to find
        
    Returns:
        Index of target if found, -1 otherwise
    """
    for i, num in enumerate(nums):
        if num == target:
            return i
    return -1


def find_pivot_index(nums: List[int]) -> int:
    """
    Helper function to find the pivot (rotation) index.
    
    Args:
        nums: Rotated sorted array
        
    Returns:
        Index where rotation occurred (index of minimum element)
    """
    if not nums:
        return -1
    
    left, right = 0, len(nums) - 1
    
    # Array is not rotated
    if nums[left] <= nums[right]:
        return 0
    
    while left <= right:
        mid = (left + right) // 2
        
        # Found pivot
        if mid < len(nums) - 1 and nums[mid] > nums[mid + 1]:
            return mid + 1
        if mid > 0 and nums[mid - 1] > nums[mid]:
            return mid
        
        # Decide which half to search
        if nums[mid] >= nums[left]:
            left = mid + 1
        else:
            right = mid - 1
    
    return 0


def test_solution():
    """Test all solutions with example cases."""
    test_cases = [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1], 0, -1),
        ([1], 1, 0),
        ([1, 3], 3, 1),
        ([3, 1], 1, 1),
        ([5, 1, 3], 3, 2),
        ([4, 5, 6, 7, 8, 1, 2, 3], 8, 4),
        ([6, 7, 0, 1, 2, 4, 5], 0, 2),
        ([6, 7, 0, 1, 2, 4, 5], 3, -1),
        ([2, 3, 4, 5, 6, 7, 0, 1], 0, 6),
        ([1, 2, 3, 4, 5], 3, 2),  # No rotation
        ([5, 4, 3, 2, 1], 3, -1),  # This would be invalid input (not sorted)
    ]
    
    solution = Solution()
    
    print("Testing Solution.search (Modified Binary Search):")
    for nums, target, expected in test_cases:
        # Skip invalid test case
        if nums == [5, 4, 3, 2, 1]:
            continue
        result = solution.search(nums, target)
        status = "✓" if result == expected else "✗"
        print(f"{status} nums={nums}, target={target} -> {result} (expected: {expected})")
    
    print("\nTesting search_rotated_array_two_step (Two-step approach):")
    for nums, target, expected in test_cases:
        # Skip invalid test case
        if nums == [5, 4, 3, 2, 1]:
            continue
        result = search_rotated_array_two_step(nums, target)
        status = "✓" if result == expected else "✗"
        print(f"{status} nums={nums}, target={target} -> {result} (expected: {expected})")
    
    print("\nTesting search_rotated_array_linear (Linear search):")
    for nums, target, expected in test_cases:
        # Skip invalid test case
        if nums == [5, 4, 3, 2, 1]:
            continue
        result = search_rotated_array_linear(nums, target)
        status = "✓" if result == expected else "✗"
        print(f"{status} nums={nums}, target={target} -> {result} (expected: {expected})")


def demonstrate_pivot_finding():
    """Demonstrate how to find pivot in rotated arrays."""
    test_arrays = [
        [4, 5, 6, 7, 0, 1, 2],
        [6, 7, 0, 1, 2, 4, 5],
        [2, 3, 4, 5, 6, 7, 0, 1],
        [1, 2, 3, 4, 5],  # No rotation
        [5, 1, 2, 3, 4],
        [1],
        [2, 1],
    ]
    
    print("Demonstrating Pivot Finding:")
    for nums in test_arrays:
        pivot = find_pivot_index(nums)
        min_val = nums[pivot] if pivot < len(nums) else "N/A"
        print(f"Array: {nums}")
        print(f"Pivot index: {pivot}, Min value: {min_val}")
        print(f"Left part: {nums[:pivot] if pivot > 0 else []}")
        print(f"Right part: {nums[pivot:] if pivot < len(nums) else []}")
        print()


def demonstrate_algorithm_steps():
    """Demonstrate step-by-step execution of the algorithm."""
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    
    print(f"Demonstrating algorithm with nums = {nums}, target = {target}")
    print("Expected result: 4")
    print()
    
    solution = Solution()
    
    print("Modified Binary Search approach:")
    print("1. We don't need to find pivot explicitly")
    print("2. At each step, determine which half is sorted")
    print("3. Check if target is in the sorted half")
    print("4. Narrow down search space accordingly")
    
    # Simulate the algorithm
    left, right = 0, len(nums) - 1
    step = 1
    
    while left <= right:
        mid = (left + right) // 2
        print(f"\nStep {step}: left={left}, right={right}, mid={mid}")
        print(f"nums[mid] = {nums[mid]}")
        
        if nums[mid] == target:
            print(f"Found target at index {mid}!")
            break
        
        if nums[left] <= nums[mid]:
            print(f"Left half [{left}:{mid}] is sorted: {nums[left:mid+1]}")
            if nums[left] <= target < nums[mid]:
                print(f"Target {target} is in left half")
                right = mid - 1
            else:
                print(f"Target {target} is in right half")
                left = mid + 1
        else:
            print(f"Right half [{mid}:{right}] is sorted: {nums[mid:right+1]}")
            if nums[mid] < target <= nums[right]:
                print(f"Target {target} is in right half")
                left = mid + 1
            else:
                print(f"Target {target} is in left half")
                right = mid - 1
        
        step += 1
    
    print(f"\nFinal result: {solution.search(nums, target)}")


if __name__ == "__main__":
    print("=== Search in Rotated Sorted Array ===\n")
    
    # Run example test cases
    solution = Solution()
    
    # Example 1
    nums1 = [4, 5, 6, 7, 0, 1, 2]
    target1 = 0
    result1 = solution.search(nums1, target1)
    print(f"Example 1: nums = {nums1}, target = {target1} -> {result1}")
    
    # Example 2
    nums2 = [4, 5, 6, 7, 0, 1, 2]
    target2 = 3
    result2 = solution.search(nums2, target2)
    print(f"Example 2: nums = {nums2}, target = {target2} -> {result2}")
    
    # Example 3
    nums3 = [1]
    target3 = 0
    result3 = solution.search(nums3, target3)
    print(f"Example 3: nums = {nums3}, target = {target3} -> {result3}")
    
    print("\n" + "="*60)
    
    # Demonstrate pivot finding
    demonstrate_pivot_finding()
    
    print("="*60)
    
    # Demonstrate algorithm steps
    demonstrate_algorithm_steps()
    
    print("\n" + "="*60)
    
    # Run comprehensive tests
    test_solution()
