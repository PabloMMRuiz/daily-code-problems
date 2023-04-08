"""This problem was asked by Amazon.
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb"."""

def solution(s: str, k: int):
    currentSubString = ""
    currentMaxLength = 0
    for index in range(0, len(s)):
        substringChars = set()
        tempLength = 0
        i = index
        temp = ""
        while i < len(s):
            substringChars.add(s[i])
            if(len(substringChars))<=k:
                tempLength +=1
                temp = temp + s[i]
                i+=1
                
            else:
                break
        if tempLength > currentMaxLength:
            currentSubString = temp
            currentMaxLength = tempLength
        if currentMaxLength > len(s)-i:
            return currentSubString

    return currentSubString

if __name__ == "__main__":
    print(solution("abcbapbaaaaaaa", 3))
    ord