class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        roomStatus = [-1] * n
        roomUsage = [0] * n
        meetings = sorted(meetings)
        for m in meetings:
            curBegin, curEnd = m
            #print(curBegin, curEnd)
            assigned = False
            earliestAvailable = [-1, math.inf]
            for i in range(n):
                if roomStatus[i] < earliestAvailable[1]:
                    earliestAvailable = [i, roomStatus[i]]
                if roomStatus[i] <= curBegin:
                    roomStatus[i] = curEnd
                    roomUsage[i] += 1
                    assigned = True
                    break
            if not assigned:
                #print("E", earliestAvailable)
                roomStatus[earliestAvailable[0]] = roomStatus[earliestAvailable[0]] + curEnd - curBegin
                roomUsage[earliestAvailable[0]] += 1
            #print(roomStatus)
        maxRoomUsage = -1
        maxUsedRoom = -1
        for i,usage in enumerate(roomUsage):
            if usage > maxRoomUsage:
                maxUsedRoom = i
                maxRoomUsage = usage
        return maxUsedRoom
        
                
        