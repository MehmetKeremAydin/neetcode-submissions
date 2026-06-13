class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustVote = {}
        meanPeople = set([i for i in range(1, n+1)])
        candidates = set()
        
        for rel in trust:
            meanPeople.discard(rel[0])
            trustVote[rel[1]] = trustVote.get(rel[1], 0) + 1
            if trustVote[rel[1]] == n-1 and rel[1] in meanPeople:
                candidates.add(rel[1])
        for person in candidates:
            if person in meanPeople:
                return person
        return -1 
        