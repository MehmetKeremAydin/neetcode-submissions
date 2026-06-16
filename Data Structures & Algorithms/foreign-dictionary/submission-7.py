class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        def getEdge(word1, word2):
            for i in range(min(len(word1), len(word2))):
                if word1[i] != word2[i]:
                    return True, (word1[i], word2[i])
            if len(word1) > len(word2):
                return False, ("z", "z")
            else:
                return False, ("a", "a")
            
        def postOrderDFS(node, word, path):
            print(path)
            nodeCons = adjMap[node]
            visited.add(node)
            path.add(node)
            for dst in nodeCons:
                if dst in path:
                    return "KEREM"
                if not dst in visited:
                    word = postOrderDFS(dst, word, path)
                    if word == "KEREM":
                        return word
            path.discard(node)
            word += node
            return word
        
        allLetters = set([i for word in words for i in word])
        nodeSet = set()
        edgeList = []
        for i in range(1, len(words)):
            found, edge = getEdge(words[i-1], words[i])
            if found:
                edgeList.append(edge)
                nodeSet.add(edge[0])
                nodeSet.add(edge[1])
            else:
                if edge == ("z", "z"): return ""
        
        allLetters = allLetters.difference(nodeSet)

        adjMap = {node:[] for node in nodeSet}
        for edge in edgeList:
            adjMap[edge[0]].append(edge[1])
            nodeSet.discard(edge[1])
        if not nodeSet and edgeList:
            return ""
        
        answer = ""
        visited = set()
        for node in nodeSet:
            curOrder= ""
            path = set()
            curOrder = postOrderDFS(node, curOrder, path)
            if curOrder == "KEREM":
                return ""
            answer += curOrder[::-1]
        for letter in allLetters:
            answer+= letter
        return answer