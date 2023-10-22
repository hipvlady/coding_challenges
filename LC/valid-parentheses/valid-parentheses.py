def isValid(s: str) -> bool:
    # A mapping of closing brackets to their corresponding opening brackets
    bracket_map = {")": "(", "}": "{", "]": "["}
    # A list used as a stack to keep track of opening brackets
    open_brackets_stack = []

    # Iterate through each character in the input string
    for char in s:
        # If the character is a closing bracket
        if char in bracket_map:
            # Pop the last element from the stack if it's not empty, otherwise use a dummy value
            top_element = open_brackets_stack.pop() if open_brackets_stack else '#'

            # Check if the popped bracket matches the mapping, if not return false
            if bracket_map[char] != top_element:
                return False
        else:
            # If it's an opening bracket, push onto the stack
            open_brackets_stack.append(char)

    # If the stack is empty, all brackets were matched correctly
    return not open_brackets_stack


# Examples
print(isValid("()"))  # Output: True
print(isValid("()[]{}"))  # Output: True
print(isValid("(]"))  # Output: False
