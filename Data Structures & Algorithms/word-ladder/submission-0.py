class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        def checker(w1, w2):

            count = 0
            i1, i2 = 0, 0
            while i1 < len(w1) and i2 < len(w2):
                if w1[i1] != w2[i2]:
                    count +=1

                i1 += 1
                i2 += 1

            return count == 1

        n = len(wordList)
        q = deque()
        graph = defaultdict(list)
        for i in range(n):
            if checker(beginWord, wordList[i]):
                q.append(wordList[i])

            for j in range(i + 1, n):
                if checker(wordList[i], wordList[j]):
                    graph[wordList[i]].append(wordList[j])
                    graph[wordList[j]].append(wordList[i])

        ans = 1
        visited = set()
        while q:
            qn = len(q)
            for _ in range(qn):
                word = q.popleft()
                visited.add(word)

                if word == endWord:
                    return ans + 1

                for nei in graph[word]:
                    if nei not in visited:
                        q.append(nei)

            ans += 1

        return 0



        


        