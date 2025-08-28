# 30. Substring with Concatenation of All Words

'''
Question: 

You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

Constraints: 
1 <= s.length <= 104
1 <= words.length <= 5000
1 <= words[i].length <= 30 (ALL OF THEM ARE OF THE SAME LENGTH!)
s and words[i] consist of lowercase English letters.
'''

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordlen=len(words[0])
        wordct=len(words)
        minsubstrlen=wordlen*wordct
        slen=len(s)
        if (slen<minsubstrlen):
            return list()
        finlist=[]
        wordncount=dict()
        for i in words:
            wordncount[i]=wordncount.get(i, 0)+1
        
        for left in range(wordlen):
            seen=dict()
            ct=0
            for right in range(left+wordlen,slen+1,wordlen):
                word=s[right-wordlen:right]
                if word in wordncount:
                    ct+=1
                    seen[word] = seen.get(word, 0)+1
                    while(seen[word]>wordncount[word]):
                        leftw=s[left:left+wordlen]
                        seen[leftw]-=1
                        left+=wordlen
                        ct-=1
                    if ct==wordct:
                        finlist.append(left)
                else:
                    seen=dict()
                    ct=0
                    left=right
        return finlist

'''
Explanation: 
Given: List of strings (words) and another string (s)
Aim: Determine all the indices in the string from where a concatenated substring formed by adding all the strings in the list in any order can be observed

Approach:
- Find the length of each word in list (wordlen), number of words in the list (wordct), length of the substring (minsubstrlen) and length of the string (slen)
- If slen is smaller than minsubstrlen, then we don't even have enough characters! So return empty list
- Initialise an empty list (finlist) that we'll return with indices (if we find any)
- Create a dictionary with {key, value} pairs as {word, its count}
- We know all words will be of same size, so checking will be repeating after wordlen characters so have left index range from 0 to wordlen loop:
    - Initialize an empty dictionary to track the words seen and the number of times they were seen and ct as 0 to track number of words that has been processed
    - Set right as the first letter of next word and increment it by wordlen as we are going to process word by word as all words are of same length until we reach last word.
        - Set word being processed as string sliced from index right-wordlen to right
        - If word exists, 
            - Increase the total word count and the seen count of the word
            - While the seen count of the word exceeds available count, 
                - Move the left index to the next word
                - Reduce the seen count of the word just skipped by 1
                - Decrease the total count of words by 1
            - If the total count is the same as the number of words in the list, add the left index to finlist
        If word does not exist at all, reset count and seen dictionary and set left to right
- Now, We have all the starting indices in finlist that we return.
'''