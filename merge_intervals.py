
def merge_intervals(intervals)):

    intervals.sort(key = lambda i: i[0])

    output = [intervals[0]]

    for start, end in intervals[1:]:

        # determine if there is any overlap with previous value
        last_end = output[-1][1]

        if start <= last_end:
            output[-1][1] = max(last_end, start)
        else:
            output.append([start, end])
    
    return output
