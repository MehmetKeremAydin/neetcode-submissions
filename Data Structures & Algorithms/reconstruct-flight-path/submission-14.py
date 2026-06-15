class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        answer = ["JFK"]
        adjMap = {}
        tickets = sorted(tickets)
        for conn in tickets:
            begin, end = conn
            node_conn = adjMap.get(begin, deque())
            node_conn.append(end)
            adjMap[begin] = node_conn

        def recursiveSearch(node):
            print(node)
            if len(answer) == len(tickets) + 1:
                return True
            if not (node in adjMap and adjMap[node]):
                return False
            for destIdx in range(len(adjMap[node])):
                dest = adjMap[node].popleft()
                answer.append(dest)
                result = recursiveSearch(dest)
                if result:
                    return True
                adjMap[node].append(dest)
                answer.pop()
            return False
        recursiveSearch("JFK")
        return answer
        