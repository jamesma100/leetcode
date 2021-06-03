# return largest water container given heights


def water_container(heights):
    l, r = 0, len(heights)
    max_area = 0
    while l < r:
        cur_area = (r-l) * min(heights[l],heights[r])
        max_area = max(max_area, cur_area)
        if heights[l] < heights[r]:
            l+=1
        else:
            r-=1
    return max_area

