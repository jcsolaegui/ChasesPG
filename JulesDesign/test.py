### ¯\_(ツ)_/¯ don't you think google will know you took this from the top hit on a google search
def base10toN(num,base):
    converted_string, modstring = "",""
    currentnum = num
    if not 1 < base < 37:
        raise ValueError("base must be between 2 and 36")
    if not num:
        return '0'
    while currentnum:
        mod = currentnum % base
        currentnum = currentnum // base
        converted_string = chr(48 + mod + 7*(mod > 10)) + converted_string
    return (converted_string) ### You need to return results to use them

def isPalindrome(n):
    return str(n) == str(n)[::-1] ### You need to return results to use them

def getLowestBaseThatMakesPalindrome(number):
    for i in range(2, 36):  ### didn't know the structure for python loops, but google searching helps
        if (isPalindrome(base10toN(number,i))):
            return i

print getLowestBaseThatMakesPalindrome(42)
print getLowestBaseThatMakesPalindrome(0)
print getLowestBaseThatMakesPalindrome(23)
