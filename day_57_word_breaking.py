"""
Given a string s and an integer k, break up the string into multiple lines such that each line has a length of k or less. 
You must break it up so that words don't break across lines. 
Each line has to have the maximum possible amount of words. If there's no way to break the text up, then return null.
You can assume that there are no spaces at the ends of the string and that there is exactly one space between each word.
For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, you should return: 
["the quick", "brown fox", "jumps over", "the lazy", "dog"]. No string in the list has a length of more than 10.
"""

def breaker(word: str, k:int)->list:
    words = word.split(" ")
    res = []
    curr_word = words[0]
    for w in words[1:]:
        if len(w)>k:
            return None
        elif len(curr_word) + 1 + len(w)<=k:
            curr_word = curr_word + " "+w
        else:
            res.append(curr_word)
            curr_word = w
    res.append(curr_word)
    return res

print(breaker("the quick brown fox jumps over the lazy dog",20))

#Still thinking about a harder interpretation: what if we want the highest minimum length?
    