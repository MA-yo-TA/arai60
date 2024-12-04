from typing import List
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        words_to_check: deque[tuple[str, int]] = deque([(beginWord, 1)])
        while words_to_check:
            current_word, distance = words_to_check.popleft()
            if current_word == endWord:
                return distance

            for i in range(len(current_word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    candidate = current_word[:i] + c + current_word[i + 1 :]
                    if candidate in wordSet:
                        words_to_check.append((candidate, distance + 1))
                        wordSet.remove(candidate)

        return 0
