
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

import collections


def ladderLength(beginWord, endWord, wordList):
    wordList = set(wordList)
    queue = collections.deque([[beginWord, 1]])
    endWord = ''.join(endWord)
    while queue:
        word, length = queue.popleft()
        word = ''.join(word)
        endWord = ''.join(endWord)
        if word == endWord:
            return length
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i + 1:]
                if next_word in wordList:
                    wordList.remove(next_word)
                    queue.append([next_word, length + 1])
    return 0



x = ladderLength(beginWord, endWord, wordList)
print(x)