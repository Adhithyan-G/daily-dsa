# 68. Text Justification

'''
Question:
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
'''

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        line = list()
        wordct = 0
        lineLen = 0
        resLines = list()
        for i in words:
            wordLen = len(i)
            if (lineLen + wordLen) > maxWidth:
                res =line[0]
                if wordct == 1:
                    res = line[0] + " "*(maxWidth-len(line[0]))
                else:
                    lineLen -= 1
                    minGap = (maxWidth - (lineLen - (wordct-1))) // (wordct-1)
                    extraGap = (maxWidth - (lineLen - (wordct-1))) % (wordct-1)
                    for j in range(1, len(line)):
                        res = res + " "*minGap
                        if extraGap > 0:
                            res = res + " "
                            extraGap -= 1
                        res = res + line[j]
                    if len(res) < maxWidth:
                        res = res + " "*(maxWidth-len(res))
                resLines.append(res)
                wordct = 0
                lineLen = 0
                line = []
            wordct += 1
            lineLen = lineLen + wordLen
            lineLen += 1
            line.append(i)
        res = " ".join(line)
        res = res + " "*(maxWidth-len(res))
        resLines.append(res)
        return resLines
    
'''
Explanation:
Given: An array of words and an integer maxWidth representing the desired line width.
Aim: To format the text such that each line is fully justified (both left and right) and contains exactly maxWidth characters but the last line is left justified

Approach:
- Initialize:
  - line = list to store current line's words.
  - wordct = count of words in the current line.
  - lineLen = length of characters in the current line including atleast one space between words.
  - resLines = final list of justified lines.

- Iterate through each word in words:
  - Compute its length (wordLen).
  - If adding the word would exceed maxWidth:
    - Justify the current line before starting a new one.
    - For single-word lines:
        - Append spaces to the right until reaching maxWidth.
    - For multi-word lines:to remove the trailing space that would be present before calculating gap values.
        - Decrement lineLen by 1 
        - Calculate total spaces to distribute:
            - minGap = minimum spaces between words.
            - extraGap = leftover spaces to add starting from the leftmost gaps.
        - Build the justified line by:
            - Adding words separated by minGap spaces.
            - Adding one extra space to the leftmost gaps while extraGap > 0.
        - If the line length is still less than maxWidth, pad trailing spaces.
    - Append the justified line to resLines.
    - Reset line, wordct, and lineLen for the next line.
- Add the word to the line and update wordct and lineLen accordingly (including one space for separation).

- After processing all words:
  - Join the last line with single spaces (left-justified).
  - Append trailing spaces to reach maxWidth.
  - Add this final line to resLines.

- Return resLines containing all justified lines.
'''