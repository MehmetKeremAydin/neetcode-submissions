class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        avaLUT = {}
        times = []
        order = []
        for i,task in enumerate(tasks):
              ls = avaLUT.get(task[0], [])
              ls.append((task[1], i))
              avaLUT[task[0]] = ls
              if not task[0] in times:
                heapq.heappush(times, task[0])
        curtime = times[0]
        priQ = []
        while times:
            new_tasks = list()
            while times and times[0] <= curtime:
                time = heapq.heappop(times)
                new_tasks += avaLUT[time]
            for new_task in new_tasks:
                heapq.heappush(priQ, new_task)
            if priQ:
                taskDone = heapq.heappop(priQ)
                order.append(taskDone[1])
                curtime += taskDone[0]
            else:
                curtime = times[0]
        while priQ:
            order.append(heapq.heappop(priQ)[1])
        return order
            