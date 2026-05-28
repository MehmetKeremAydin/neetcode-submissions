class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def createBoardFromState(state:list)->list:
            assert len(state) == n
            board = list()
            for entry in state:
                row = entry*"." + "Q" + (n-1-entry)*"."
                board.append(row)
            return board
        
        def elimAvailability(availableSqs, qRow, qCol):
            for i in range(qRow+1, n):
                newset = availableSqs[i].copy()
                newset.discard(qCol)
                newset.discard(qCol+(i-qRow))
                newset.discard(qCol-(i-qRow))
                availableSqs[i] = newset
            return availableSqs


        def recursiveSearch(i, state, availableSqs):
            #print(state)
            #print(availableSqs)
            if i == n:
                board = createBoardFromState(state)
                answer.append(board)
                return
            rowAvailability = availableSqs[i]
            for entry in rowAvailability:
                state.append(entry)
                newAvailability = elimAvailability(availableSqs.copy(), i, entry)
                recursiveSearch(i+1, state, newAvailability)
                state.pop()

        
        answer = []
        baseAvailableSqs = {}
        state = []
        for i in range(n):
            baseAvailableSqs[i] = set()
            for j in range(n):
                baseAvailableSqs[i].add(j)
        recursiveSearch(0, state, baseAvailableSqs)
        return answer
            
        

                
        