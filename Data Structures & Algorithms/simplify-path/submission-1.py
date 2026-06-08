class Solution:
    def simplifyPath(self, path: str) -> str:
        pathList = path.split("/")
        pathStack = []
        for entry in pathList:
            if entry == "" or entry == ".":
                continue
            if entry == "..":
                if pathStack:
                    pathStack.pop()
            else:
                pathStack.append(entry)
        simplified = ""
        for elem in pathStack:
            simplified += "/" + elem
        return simplified if pathStack else "/"
            
        