class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1
        totalTasks = 0
        freqs = []
        for k, v in freq.items():
            totalTasks += v
            freqs.append(v)
        heapq.heapify_max(freqs)
        ops = deque()
        time = 0
        while totalTasks > 0:
            if(len(freqs) > 0):
                ops.append(heapq.heappop_max(freqs)-1)
                totalTasks -= 1
            else:
                ops.append(0)
            if(len(ops)>n):
                num = ops.popleft()
                if num>0:
                    heapq.heappush_max(freqs, num)
            time += 1
        return time