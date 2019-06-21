def ispalindrome(inputstring):
    try:
        tempstring=inputstring[::-1]
        for i in range(len(inputstring)):
            if tempstring[i] != inputstring[i]:
                print("Given string is not a Palindrome")
                return False
        print("Given string is a Palindrome")
        return True
    except Exception as e:
        print("Input Error",e)
            