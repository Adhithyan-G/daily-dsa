# 71. Simplify Path

'''
Question:
You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. Your task is to transform this absolute path into its simplified canonical path.

The rules of a Unix-style file system are as follows:

A single period '.' represents the current directory.
A double period '..' represents the previous/parent directory.
Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
Any sequence of periods that does not match the rules above should be treated as a valid directory or file name. For example, '...' and '....' are valid directory or file names.
The simplified canonical path should follow these rules:

The path must start with a single slash '/'.
Directories within the path must be separated by exactly one slash '/'.
The path must not end with a slash '/', unless it is the root directory.
The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.
Return the simplified canonical path.
'''
class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split('/')
        pathlist = []
        for i in dirs:
            if i in ['', '.']:
                continue
            elif i == '..':
                if pathlist:
                    pathlist.pop()
            else:
                pathlist.append(i)
        path = ''
        for i in pathlist:
            path = path+'/'+i
        return path if path != '' else '/'

'''
Explanation:
Given: A string path representing an absolute Unix-style file path.
Aim: To return the simplified canonical path that follows Unix rules.

Approach:
- Split the input path by '/' to isolate directory names and symbols.
- Initialize an empty list pathlist to simulate a directory stack.
- Iterate through each element in the split list:
    - If the element is empty ('') or '.', skip it (as it represents the current directory or redundant slashes).
    - If the element is '..':
        - Pop the last directory from pathlist if it exists (move one level up).
    - Otherwise:
        - Append the directory name to pathlist (valid directory or file name).
- After processing all parts, reconstruct the canonical path:
    - Join the directories in pathlist with '/' and prefix a single leading '/'.
    - If pathlist is empty, return '/' to represent the root directory.
- Return the final simplified canonical path.
'''