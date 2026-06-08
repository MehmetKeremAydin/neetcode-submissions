class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        newState = []
        asteroids = deque(asteroids)
        while asteroids:
            ast = asteroids.popleft()
            if not newState or not (newState[-1] > 0 and ast < 0):
                newState.append(ast)
            else:
                prevAst = newState.pop()
                if abs(prevAst) > abs(ast):
                    asteroids.appendleft(prevAst)
                elif abs(prevAst) < abs(ast):
                    asteroids.appendleft(ast)
        return newState