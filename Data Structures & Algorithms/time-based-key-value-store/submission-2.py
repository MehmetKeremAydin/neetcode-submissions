class TimeMap:

    def __init__(self):
        self.storage = dict()
        self.t_stor = dict()
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storage[(key, timestamp)] = value
        if key in self.t_stor:
            self.t_stor[key].append(timestamp)
        else:
            self.t_stor[key] = [timestamp]
        

    def get(self, key: str, timestamp: int) -> str:
        if (not key in self.t_stor) or (timestamp < self.t_stor[key][0]):
            return ""
        elif timestamp >= self.t_stor[key][-1]:
            return self.storage.get((key, self.t_stor[key][-1]))
        else:
            l, r = 0, len(self.t_stor[key]) - 1
            while(l<=r):
                m = (l + r) // 2
                if self.t_stor[key][m] <= timestamp < self.t_stor[key][m+1]:
                    return self.storage.get((key, self.t_stor[key][m]))
                elif self.t_stor[key][m] <= timestamp:
                    l = m + 1
                else:
                    r = m - 1
        return ""
        
