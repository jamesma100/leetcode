# Given set of non-overlapping inttervals, insert new interval
# Merge if necessary
# Assume intervals initially sorted according to start time

def insert(self, intervals, newInterval):
    res = []
    i = 0
    # add all intervals ending before newInterval starts
    while i < len(intervals) and intervals[i][1] < newInterval[0]:
        res.append(intervals[i])
        i += 1
    # at this point all intervals end after newInterval starts
    # merge intervals that start before newInterval ends
    # initialize merge to newInterval so if no merging required, 
    # newInterval is added
    merged = [newInterval[0], newInterval[1]]
    while i < len(intervals) and intervals[i][0] <= newInterval[1]:
        merged[0] = min(intervals[i][0], merged[0])
        merged[1] = max(intervals[i][1], merged[1])
        i += 1
    res.append(merged)
    # add remaining intervals that start after newInterval ends
    while i < len(intervals):
        res.append(intervals[i])
        i += 1
    return res
