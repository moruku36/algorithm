"""
32. Longest Valid Parentheses

Given a string containing just the characters '(' and ')', return the length 
of the longest valid (well-formed) parentheses substring.

Examples:
- s = "(()" -> Output: 2 (The longest valid parentheses substring is "()")
- s = ")()())" -> Output: 4 (The longest valid parentheses substring is "()()")
- s = "" -> Output: 0

Constraints:
- 0 <= s.length <= 3 * 10^4
- s[i] is '(' or ')'
"""


class Solution:
    """LeetCode style solution class."""
    
    def longestValidParentheses(self, s: str) -> int:
        """
        Find the length of the longest valid parentheses substring.
        Using dynamic programming approach.
        
        Args:
            s: String containing only '(' and ')'
            
        Returns:
            Length of the longest valid parentheses substring
        """
        if not s:
            return 0
        
        n = len(s)
        # dp[i] represents the length of longest valid parentheses ending at index i
        dp = [0] * n
        max_length = 0
        
        for i in range(1, n):
            if s[i] == ')':
                if s[i - 1] == '(':
                    # Case: ...()
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                elif dp[i - 1] > 0:
                    # Case: ...))
                    # Find the matching '(' for current ')'
                    match_index = i - dp[i - 1] - 1
                    if match_index >= 0 and s[match_index] == '(':
                        dp[i] = dp[i - 1] + 2 + (dp[match_index - 1] if match_index > 0 else 0)
                
                max_length = max(max_length, dp[i])
        
        return max_length


def longest_valid_parentheses_stack(s: str) -> int:
    """
    Stack-based approach to find longest valid parentheses.
    
    Args:
        s: String containing only '(' and ')'
        
    Returns:
        Length of the longest valid parentheses substring
    """
    if not s:
        return 0
    
    stack = [-1]  # Initialize with base index
    max_length = 0
    
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:  # char == ')'
            stack.pop()
            if not stack:
                # No matching '(' found, push current index as new base
                stack.append(i)
            else:
                # Calculate current valid length
                current_length = i - stack[-1]
                max_length = max(max_length, current_length)
    
    return max_length


def longest_valid_parentheses_two_pass(s: str) -> int:
    """
    Two-pass approach without extra space.
    
    Args:
        s: String containing only '(' and ')'
        
    Returns:
        Length of the longest valid parentheses substring
    """
    if not s:
        return 0
    
    max_length = 0
    
    # Left to right pass
    left = right = 0
    for char in s:
        if char == '(':
            left += 1
        else:
            right += 1
        
        if left == right:
            max_length = max(max_length, 2 * right)
        elif right > left:
            left = right = 0
    
    # Right to left pass
    left = right = 0
    for char in reversed(s):
        if char == '(':
            left += 1
        else:
            right += 1
        
        if left == right:
            max_length = max(max_length, 2 * left)
        elif left > right:
            left = right = 0
    
    return max_length


def longest_valid_parentheses_brute_force(s: str) -> int:
    """
    Brute force approach - check all possible substrings.
    Time complexity: O(n^3), not efficient for large inputs.
    
    Args:
        s: String containing only '(' and ')'
        
    Returns:
        Length of the longest valid parentheses substring
    """
    def is_valid(substring):
        """Check if a substring has valid parentheses."""
        stack = []
        for char in substring:
            if char == '(':
                stack.append(char)
            else:  # char == ')'
                if not stack:
                    return False
                stack.pop()
        return len(stack) == 0
    
    max_length = 0
    n = len(s)
    
    # Check all even-length substrings
    for i in range(n):
        for j in range(i + 2, n + 1, 2):  # Only even lengths can be valid
            if is_valid(s[i:j]):
                max_length = max(max_length, j - i)
    
    return max_length


def test_solution():
    """Test all solutions with example cases."""
    test_cases = [
        ("(()", 2),
        (")()())", 4),
        ("", 0),
        ("()", 2),
        ("()(()", 2),
        ("((((", 0),
        ("))))", 0),
        ("()(())", 6),
        ("(()())", 6),
        ("()())", 4),
        ("((()))", 6),
        ("()()()", 6),
        ("))(())", 4),
    ]
    
    solution = Solution()
    
    print("Testing Solution.longestValidParentheses (DP approach):")
    for s, expected in test_cases:
        result = solution.longestValidParentheses(s)
        status = "✓" if result == expected else "✗"
        print(f"{status} s='{s}' -> {result} (expected: {expected})")
    
    print("\nTesting longest_valid_parentheses_stack (Stack approach):")
    for s, expected in test_cases:
        result = longest_valid_parentheses_stack(s)
        status = "✓" if result == expected else "✗"
        print(f"{status} s='{s}' -> {result} (expected: {expected})")
    
    print("\nTesting longest_valid_parentheses_two_pass (Two-pass approach):")
    for s, expected in test_cases:
        result = longest_valid_parentheses_two_pass(s)
        status = "✓" if result == expected else "✗"
        print(f"{status} s='{s}' -> {result} (expected: {expected})")
    
    print("\nTesting longest_valid_parentheses_brute_force (Brute force - small inputs only):")
    # Test only smaller inputs for brute force due to O(n^3) complexity
    small_test_cases = [case for case in test_cases if len(case[0]) <= 10]
    for s, expected in small_test_cases:
        result = longest_valid_parentheses_brute_force(s)
        status = "✓" if result == expected else "✗"
        print(f"{status} s='{s}' -> {result} (expected: {expected})")


def demonstrate_approaches():
    """Demonstrate different approaches with detailed explanations."""
    test_string = ")()())"
    print(f"Demonstrating with string: '{test_string}'")
    print("Expected result: 4 (substring '()()')")
    print()
    
    solution = Solution()
    
    print("1. Dynamic Programming Approach:")
    print("   - Time: O(n), Space: O(n)")
    print("   - Build dp array where dp[i] = length of longest valid parentheses ending at i")
    result1 = solution.longestValidParentheses(test_string)
    print(f"   - Result: {result1}")
    print()
    
    print("2. Stack Approach:")
    print("   - Time: O(n), Space: O(n)")
    print("   - Use stack to track indices and calculate lengths")
    result2 = longest_valid_parentheses_stack(test_string)
    print(f"   - Result: {result2}")
    print()
    
    print("3. Two-pass Approach:")
    print("   - Time: O(n), Space: O(1)")
    print("   - Left-to-right and right-to-left scanning")
    result3 = longest_valid_parentheses_two_pass(test_string)
    print(f"   - Result: {result3}")
    print()


if __name__ == "__main__":
    print("=== Longest Valid Parentheses ===\n")
    
    # Run example test cases
    solution = Solution()
    
    # Example 1
    s1 = "(()"
    result1 = solution.longestValidParentheses(s1)
    print(f"Example 1: s = '{s1}' -> {result1}")
    
    # Example 2
    s2 = ")()())"
    result2 = solution.longestValidParentheses(s2)
    print(f"Example 2: s = '{s2}' -> {result2}")
    
    # Example 3
    s3 = ""
    result3 = solution.longestValidParentheses(s3)
    print(f"Example 3: s = '{s3}' -> {result3}")
    
    print("\n" + "="*60)
    
    # Demonstrate different approaches
    demonstrate_approaches()
    
    print("="*60)
    
    # Run comprehensive tests
    test_solution()
