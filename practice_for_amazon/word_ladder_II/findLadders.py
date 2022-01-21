'''
A tranformation sequence from word beginWord to word endWord using a dictionary wordList is a seqence of words beginWord -> s1 -> s2 -> .... -> sk such that:

- every adjacent pair of words differs by a single letter
- every s1 for 1 <= i <= k is in wordList.  Note that beginWord does not need to be in wordList
- sk == endWord

Given 2 words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or empty list if no such sequence exists.  Reach sequence should be returned as a list of the words [beginWord, s1, s2, .., sk]

Example 1:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

Output: [["hit", "hot", "dot", "dog", "cog"], ["hit", "hot", "lot". "log", "cog"]]
Explanation: there are 2 shortest transformation sequences:

"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"

Example 2:
input: beginWord = "hit", endWord = "cog", wordList = ["hot", "dot", "dog", "lot", "log"]
output: []
Explanation: the endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
'''

def findLadders(beginWord, endWord, wordList):