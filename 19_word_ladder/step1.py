from typing import List
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        endNode = -1
        for i in range(len(wordList)):
            if wordList[i] == endWord:
                endNode = i

        if endNode < 0:
            return 0

        beginNode = len(wordList)
        for i in range(len(wordList)):
            if beginWord == wordList[i]:
                beginNode = i
                break

        if beginNode == len(wordList):
            wordList.append(beginWord)

        adj_list: List[List[int]] = [[] for _ in range(len(wordList))]
        for i in range(len(wordList) - 1):
            for j in range(i + 1, len(wordList)):
                if self.differ_single(wordList[i], wordList[j]):
                    adj_list[i].append(j)
                    adj_list[j].append(i)

        return self.search_end_word(beginNode, endNode, adj_list)

    def differ_single(self, str1: str, str2: str) -> bool:
        if len(str1) != len(str2):
            # wordList[i].length == beginWord.length so don't come here
            return False

        count = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                count += 1

        if count == 1:
            return True
        else:
            return False

    def search_end_word(
        self,
        beginNode: int,
        endNode: int,
        adj_list: List[List[int]],
    ) -> int:
        nodes_to_visit: deque[tuple[int, int]] = deque()
        visited_nodes: set[int] = set()

        nodes_to_visit.append((beginNode, 1))

        while nodes_to_visit:
            current_node, dist = nodes_to_visit.popleft()
            visited_nodes.add(current_node)
            if current_node == endNode:
                return dist

            for next in adj_list[current_node]:
                if next not in visited_nodes:
                    nodes_to_visit.append((next, dist + 1))

        return 0
