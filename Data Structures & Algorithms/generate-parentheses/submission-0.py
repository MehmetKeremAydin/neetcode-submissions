class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def recursiveSearch(toBeOpened:int, toBeClosed, curPar:str):
            if toBeOpened == 0:
                answer.append( curPar + toBeClosed*")" )
                return
            if toBeClosed == 0:
                curPar += "("
                recursiveSearch(toBeOpened-1, toBeClosed+1, curPar)
            else:
                recursiveSearch(toBeOpened-1, toBeClosed+1, curPar+"(")
                recursiveSearch(toBeOpened, toBeClosed-1, curPar+")")
            return

        
        answer = []
        curPar = ""
        recursiveSearch(n, 0, curPar)
        return answer

        
        