class Solution:
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        subs = [set() for _ in range(9)]
        for i,row in enumerate(board):
            for j,entry in enumerate(row):
                if entry == ".":
                    continue
                sub_idx = 3*(i//3) + j//3
                if entry in rows[i] or entry in cols[j] or entry in subs[sub_idx]:
                    # print(i, j, sub_idx, entry)
                    # print(rows)
                    return False
                rows[i].add(entry)
                cols[j].add(entry)
                subs[sub_idx].add(entry)
        return True
        