class TimeMap:

    def __init__(self):
        self.t_stor = dict()
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.t_stor:
            self.t_stor[key].append((timestamp, value))
        else:
            self.t_stor[key] = [(timestamp, value)]
        

    def get(self, key: str, timestamp: int) -> str:
        print(self.t_stor)
        if (not key in self.t_stor) or (timestamp < self.t_stor[key][0][0]):
            return ""
        elif timestamp >= self.t_stor[key][-1][0]:
            return self.t_stor.get(key)[-1][1]
        else:
            l, r = 0, len(self.t_stor[key]) - 1
            while(l<=r):
                m = (l + r) // 2
                if self.t_stor[key][m][0] <= timestamp < self.t_stor[key][m+1][0]:
                    return self.t_stor.get(key)[m][1]
                elif self.t_stor[key][m][0] <= timestamp:
                    l = m + 1
                else:
                    r = m - 1
        return ""
        
