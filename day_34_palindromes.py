"""Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word. 
If there is more than one palindrome of minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).
For example, given the string "race", you should return "ecarace", since we can add three letters to it 
(which is the smallest amount to make a palindrome). There are seven other palindromes that can be made from "race" by adding three letters, 
but "ecarace" comes first alphabetically
As another example, given the string "google", you should return "elgoogle"."""

def get_palindrome(word:str)->str:
    if(word[::-1] == word):
        return word
    length = len(word)

    if word[0] == word[-1]:
        return word [0] + get_palindrome(word[1:length-1]) + word[0]
    else:
        pal_left = get_palindrome(word+word[0])
        pal_right = get_palindrome(word[-1] + word)

    if len(pal_left) != len(pal_right):
        return min(pal_right, pal_left, key=lambda a:len(a))
    else:
        return min(pal_left, pal_right)


print(get_palindrome("hola"))