# merge overlapping intervals and return non-overlapping intervals
# loop through intervals, if current can be merged with previous, merge
# else: current is non overlapping with previous, so append to result
def merge(self, intervals):
    intervals.sort(key = lambda x: x[0])
    res = [intervals[0]]
    for interval in intervals[1:]:
        if interval[0] <= res[-1][1]:
            res[-1][1] = max(res[-1][1], interval[1])
        else:
            res.append(interval)
    return res