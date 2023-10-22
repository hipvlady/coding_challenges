import re
"""
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
"""

input = "A man, a plan, a canal: Panama"
new_input = ""

input_str = "A man, a plan, a canal: Panama"
cleaned_str = ''.join(char for char in input_str if char.isalnum()).lower()
# using regex
# cleaned_str = re.sub(r'[^a-zA-Z0-9]', '', input_str).lower()

is_palindrome = cleaned_str == cleaned_str[::-1]
print(is_palindrome)  # True for the given example
