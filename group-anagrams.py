# 49. Group Anagrams

'''
Question:
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordsgrouped=dict()
        for word in strs:
            key=['0' for i in range(26)]
            for ch in word:
                key[ord(ch)-ord('a')]=str(int(key[ord(ch)-ord('a')])+1)
            keystring='#'.join(key)
            if keystring not in wordsgrouped:
                wordsgrouped[keystring] = [word]
            else:
                wordsgrouped[keystring].append(word)
        res=list()
        for k in wordsgrouped:
            res.append(wordsgrouped[k])
        return res
'''
Explanation: 
Given: A list (strs) of strings
Aim: To group all anagrams of the list together into seperate lists and return list of lists

Approach:
- Create an empty dictionary (wordsgrouped) which will contain the groups and the words
- For every string in strs:
    - Initialize a list (key) with 26 '0' as we will only have the smaller case letters
    - For every character in the string, calculate their index in the key using their ASCII value and increase the value at that index by 1 by converting it to int, adding and converting it back to string
    - When all characters are processed, Join all values of key into a string with '#' as a seperator (keystring)
    - We need a seperator such that we don't use wrong keys like 10'b's and 1 'c' will be '01010....' and also 1 'b' and 10 'd's will also be '01010.....', Hence the need for seperators!
    - If the keystring does at exist in wordsgrouped, Add the key with its value as a list containing the current string
    - Else, Append the string to the list already assigned to the keystring
- Append every list in wordsgrouped to empty list and return the final grouped list of lists
'''