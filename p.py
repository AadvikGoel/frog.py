def isPalindrome(string):
    left_pos = 0
    right_pos = len(string) - 1


    while right_pos >= left_pos:
        left_pos += 1
        right_pos -= 1
    return True
print("Is this a Palindrome?")
print(isPalindrome('malayalam'))
