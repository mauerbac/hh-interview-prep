#https://www.interviewcake.com/question/merging-ranges
#Given a list find merged times

#  [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)] - meeting times
#   [(0, 1), (3, 8), (9, 12)] -merged 

def find_times(times):
    times = sorted(times, key=lambda x: x[0])  # sort by lower bound
    print "sorted"
    print times
    # sorted : [(0, 1), (3, 5), (4, 8), (9, 10), (10, 12)]
    merged = [times.pop(0)] #0,1
    for current in times:
        lower = merged[-1]
        print "lower", lower
        if current[0] <= lower[1]:
            upper_bound = max(lower[1], current[1])
            print upper_bound
            merged[-1] = (lower[0], upper_bound)
        else:
            merged.append(current)
    return merged
 
 
print find_times([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
