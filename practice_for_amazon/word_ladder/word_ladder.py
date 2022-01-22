'''
Given 2 words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest tranformation sequence from beginWord to endWord, or 0 if no such sequence exists

Exampl 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
Output: 5
Explanation: one shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> "cog", which is 5 words long

'''

def ladderLength(beginWord, endWord, wordList):