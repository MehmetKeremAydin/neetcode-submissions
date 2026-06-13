class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def find(a:int) -> int:
            while parents[a] != a:
                a = parents[a]
            return a
        
        def union(a:int,b:int):
            p1, p2 = find(a), find(b)
            if p1 == p2:
                return False
            if rank[p2] > rank[p1]:
                parents[p1] = p2
                rank[p2] += rank[p1]
            else:
                parents[p2] = p1
                rank[p1] += rank[p2]
            return True

        edgeMap = {}
        for i, acc in enumerate(accounts):
            for addIdx in range(1, len(acc)):
                con = edgeMap.get(acc[addIdx], [])
                con.append(i)
                edgeMap[acc[addIdx]] = con
        
        parents = [i for i in range(len(accounts))]
        rank = [1] * len(accounts)
        
        for i, mail in enumerate(edgeMap):
            conns = edgeMap[mail]
            for i in range(1, len(conns)):
                union(conns[0], conns[i])
        
        answerDict = {}
        for i, mail in enumerate(edgeMap):
            parentNode = find(edgeMap[mail][0])
            parentMails = answerDict.get(parentNode, [])
            parentMails.append(mail)
            answerDict[parentNode] = parentMails

        answer = []
        for key in answerDict:
            mails = sorted(answerDict[key])
            curAnswer = [accounts[key][0]]
            curAnswer = curAnswer + mails
            answer.append(curAnswer)
        
        return answer