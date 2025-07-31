"""
28. Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first occurrence 
of needle in haystack, or -1 if needle is not part of haystack.

Examples:
- haystack = "sadbutsad", needle = "sad" -> Output: 0
- haystack = "leetcode", needle = "leeto" -> Output: -1

Constraints:
- 1 <= haystack.length, needle.length <= 10^4
- haystack and needle consist of only lowercase English characters
"""


class Solution:
    """LeetCode style solution class."""
    
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Find the index of the first occurrence of needle in haystack.
        
        Args:
            haystack: The string to search in
            needle: The string to search for
            
        Returns:
            The index of the first occurrence, or -1 if not found
        """
        # Edge case: empty needle
        if not needle:
            return 0
        
        # Edge case: needle is longer than haystack
        if len(needle) > len(haystack):
            return -1
        
        # Using built-in find method
        return haystack.find(needle)


def str_str(haystack: str, needle: str) -> int:
    """
    Find the index of the first occurrence of needle in haystack.
    
    Args:
        haystack: The string to search in
        needle: The string to search for
        
    Returns:
        The index of the first occurrence, or -1 if not found
    """
    # Edge case: empty needle
    if not needle:
        return 0
    
    # Edge case: needle is longer than haystack
    if len(needle) > len(haystack):
        return -1
    
    # Method 1: Using built-in find method (simplest)
    return haystack.find(needle)


def str_str_manual(haystack: str, needle: str) -> int:
    """
    Manual implementation without using built-in methods.
    
    Args:
        haystack: The string to search in
        needle: The string to search for
        
    Returns:
        The index of the first occurrence, or -1 if not found
    """
    # Edge case: empty needle
    if not needle:
        return 0
    
    # Edge case: needle is longer than haystack
    if len(needle) > len(haystack):
        return -1
    
    # Iterate through haystack
    for i in range(len(haystack) - len(needle) + 1):
        # Check if needle matches at position i
        if haystack[i:i + len(needle)] == needle:
            return i
    
    return -1


def str_str_kmp(haystack: str, needle: str) -> int:
    """
    KMP (Knuth-Morris-Pratt) algorithm implementation.
    Time complexity: O(m + n), where m = len(haystack), n = len(needle)
    
    Args:
        haystack: The string to search in
        needle: The string to search for
        
    Returns:
        The index of the first occurrence, or -1 if not found
    """
    if not needle:
        return 0
    
    if len(needle) > len(haystack):
        return -1
    
    # Build the LPS (Longest Proper Prefix which is also Suffix) array
    def build_lps(pattern):
        lps = [0] * len(pattern)
        length = 0  # length of the previous longest prefix suffix
        i = 1
        
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        
        return lps
    
    lps = build_lps(needle)
    
    i = 0  # index for haystack
    j = 0  # index for needle
    
    while i < len(haystack):
        if haystack[i] == needle[j]:
            i += 1
            j += 1
        
        if j == len(needle):
            return i - j
        elif i < len(haystack) and haystack[i] != needle[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return -1


def test_solution():
    """Test the solution with example cases."""
    test_cases = [
        ("sadbutsad", "sad", 0),
        ("leetcode", "leeto", -1),
        ("hello", "ll", 2),
        ("aaaaa", "bba", -1),
        ("", "a", -1),
        ("a", "", 0),
        ("mississippi", "issip", 4),
        ("aabaaabaaac", "aabaaac", 4),
    ]
    
    # Test LeetCode style Solution class
    solution = Solution()
    print("Testing Solution.strStr (LeetCode style):")
    for haystack, needle, expected in test_cases:
        result = solution.strStr(haystack, needle)
        status = "✓" if result == expected else "✗"
        print(f"{status} haystack='{haystack}', needle='{needle}' -> {result} (expected: {expected})")
    
    print("\nTesting str_str (built-in method):")
    for haystack, needle, expected in test_cases:
        result = str_str(haystack, needle)
        status = "✓" if result == expected else "✗"
        print(f"{status} haystack='{haystack}', needle='{needle}' -> {result} (expected: {expected})")
    
    print("\nTesting str_str_manual (manual implementation):")
    for haystack, needle, expected in test_cases:
        result = str_str_manual(haystack, needle)
        status = "✓" if result == expected else "✗"
        print(f"{status} haystack='{haystack}', needle='{needle}' -> {result} (expected: {expected})")
    
    print("\nTesting str_str_kmp (KMP algorithm):")
    for haystack, needle, expected in test_cases:
        result = str_str_kmp(haystack, needle)
        status = "✓" if result == expected else "✗"
        print(f"{status} haystack='{haystack}', needle='{needle}' -> {result} (expected: {expected})")


if __name__ == "__main__":
    # Run the example test cases
    print("=== Find the Index of the First Occurrence in a String ===\n")
    
    # LeetCode style examples
    solution = Solution()
    
    # Example 1
    haystack1 = "sadbutsad"
    needle1 = "sad"
    result1 = solution.strStr(haystack1, needle1)
    print(f"Example 1: haystack = '{haystack1}', needle = '{needle1}' -> {result1}")
    
    # Example 2
    haystack2 = "leetcode"
    needle2 = "leeto"
    result2 = solution.strStr(haystack2, needle2)
    print(f"Example 2: haystack = '{haystack2}', needle = '{needle2}' -> {result2}")
    
    print("\n" + "="*60)
    
    # Run comprehensive tests
    test_solution()
