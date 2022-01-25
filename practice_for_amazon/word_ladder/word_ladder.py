"""
Given 2 words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest tranformation sequence from beginWord to endWord, or 0 if no such sequence exists

Exampl 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
Output: 5
Explanation: one shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> "cog", which is 5 words long


- use a intermediate dictionary as a place to look up for BFS:
- key is intermediate words, value is the word from wordList
- process BFS start with begin word


"""


def ladderLength(beginWord, endWord, wordList):
    from collections import defaultdict
    from collections import deque

    if endWord not in wordList or not endWord or not beginWord or not wordList:
        return 0

    # since all words are of same length
    L = len(beginWord)

    # Dictionary to hold combination of words that can be formed
    # from any given word. By changing one letter at a time
    all_combo_dict = defaultdict(list)
    for word in wordList:
        for i in range(L):
            # key is the generic word
            # value is a list of words which have the same intermediate generic word
            # each word will belong to the number of keys that is equal to the word len.
            key = word[:i] + "*" + word[i + 1 :]
            all_combo_dict[key].append(word)

    # queue for BFS
    queue = deque([(beginWord, 1)])
    # visited to make sure we don't repreat processing same word
    visited = {beginWord: True}

    while queue:
        print(queue)
        current_word, level = queue.popleft()

        for i in range(L):
            # intermediate words for current word
            intermediate_word = current_word[:i] + "*" + current_word[i + 1 :]
            # next states are all the words which share the same intermediate state
            for word in all_combo_dict[intermediate_word]:

                # if at any point if we find what we are looking for
                # i.e. the end word - we can return with the answer
                if word == endWord:
                    return level + 1
                # Otherwise, add it fo the BFS Queue, Also mark it visited
                if word not in visited:
                    visited[word] = True
                    queue.append((word, level + 1))

            # empty that intermidiate word after process it so that we dont go back.

            all_combo_dict[intermediate_word] = []
        print("queue", queue)

    return 0


wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

print(ladderLength("hit", "cog", wordList))

"""
Complexity Analysis
let M is the length of each word and N is the total number of words in the input word list

- Time Complexity: O(M^2 x N)
+ For each word in world list, we iterate over its length to find all the intermediate words corresponding to it.  Since the length of each word is M and we have N words, the total number of iterations the alg takes to create all_combo_dict is MxN.  Additionally, forming each of the intermediate word takes O(M) time because of the substring operation used to create the new string.  This adds up to a complexity of O(M^2 x N)

- Breadth first search in the worst case might go to each of the N words.  For each word, we need to examine M possible intermediate words/combinations.  Notice, we have used the substring operation to find each of the combination.  Thus, M combinations take O(M^2) time.  As a result, the time complexity of BFS traversal would also be O(M^2 x N)

Space: come from the dic of intermediate words
- N*M*M = NxM^2

hot => *ot, h*t, ho* => save 3 copy of hot for these 3 itermediate wordds
*ot: hot
h*t: hot
ho*: hot

- Visited dictionary would need a space of O(MxN) as each word is of length M
- Queue for BFS in worst case would need a space for all O(N) words and this would also result in a space complexity of O(MxN)

=> O(M^2 x N)
"""
