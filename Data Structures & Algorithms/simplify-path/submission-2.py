class Solution:
    def simplifyPath(self, path: str) -> str:
        pathParts = path.split("/")
        stack = []
        for part in pathParts:
            if part == "" or part == ".":
                continue
            if part == "..":
                if stack: stack.pop()
            else:
                stack.append("/"+part)
        if stack:
            answer = "".join(stack)
            return answer
        else:
            return "/"