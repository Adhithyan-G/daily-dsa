# 72. Edit Distance

'''
Question:
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
'''

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        w1 = len(word1)
        w2 = len(word2)
        track = [x for x in range(w2+1)]
        prev_diag  = track[0]
        for i in range(w1):
            for j in range(w2+1):
                temp = track[j]
                if j==0:
                    track[j] = i+1
                    prev_diag  = temp
                    continue
                if word1[i] == word2[j-1]:
                    track[j] = prev_diag 
                else:
                    track[j] = min(track[j], track[j-1], prev_diag) + 1
                prev_diag  = temp
        return track[-1]

'''
Explanation:
Given: Two strings, word1 and word2.
Aim: To determine the minimum number of edit operations (insert, delete, replace) required to transform word1 into word2.

Approach:
- Set w1 and w2 as lengths of word1 and word2 respectively.
- Initiate an array of w2+1 elements where each element in the array denotes number of operations to convert word1 to word2 if word1 was empty at each character stage of word2 starting from assuming word2 as empty to last character of word2.
- Set prev_diag as track[0]

- For each index until w1:
    - For index until w2+1 (including prefixed empty character assumption):
        - Record track[j] before change as temp
        - Set track[j] as i+1 if j == 0, Update prev_diag as temp and move to next iteration for j
        - If characters match -> copy prev_diag (no cost).
        - Else -> take min of (track[j], track[j-1], prev_diag) + 1. Which is just taking the minimum cost of (Inserting a new character, deleting this character, updating this character) of word1 respectively
    - Update prev_diag as temp for the next interation.

- After processing all characters, track[-1] contains the final minimum edit distance.
- Return track[-1] as the result.
'''