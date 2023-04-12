"""Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Implement regular expression matching with the following special characters:
. (period) which matches any single character
* (asterisk) which matches zero or more of the preceding element
That is, implement a function that takes in a string and a valid regular expression and returns whether
or not the string matches the regular expression.
For example, given the regular expression "ra." and the string "ray", your function should return true. 
The same regular expression on the string "raymond" should return false.
Given the regular expression ".*at" and the string "chat", your function should return true. 
The same regular expression on the string "chats" should return false."""

def re_match(re: str, s: str)-> bool:
    repeater = ""
    repeating = False
    re_index = 0
    s_index = 0
    while True:
        if (re_index >= len(re) and repeating == False) or s_index>=len(s):
                break
        if not repeating:
            if re[re_index] == ".":
                re_index+=1
                s_index +=1
                continue
            if re[re_index] == "*":
                repeater = re[re_index-1]
                repeating = True
                continue
            if re[re_index] != s[s_index]:
                    return False
            re_index+=1
            s_index+=1
        if repeating and repeater == "." and re_index==len(re)-1:
            return True
        if repeating and repeater ==".":
            if re_index == len(re)-1:
                return True
            else:
                re_index+=1
                found = False
                while s_index<len(s):
                    if s[s_index] == re[re_index]:
                        found = True
                        break
                    else:
                        s_index +=1
                if not found:
                    return False
                else:
                    repeating = False
                    continue
        if repeating:
            if s[s_index] != repeater:
                re_index +=1
                repeating = False
                continue
            if s[s_index] == repeater:
                s_index +=1
                continue
        
    return True if s_index == len(s) else False

print(re_match("c.a*", "chaagshtsryts"))