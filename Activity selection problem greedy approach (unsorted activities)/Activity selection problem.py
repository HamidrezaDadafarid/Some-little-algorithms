def take_second(elem):
    return elem[1]

def selected_activites(activities):
    sorted_activities = sorted(activities, key = take_second)
    i = 0
    print(f"Activity number {i} is done with start time = {sorted_activities[i][0]} and finish time = {sorted_activities[i][1]}")
    for j in range(1, len(sorted_activities)):
        if sorted_activities[j][0] >= sorted_activities[i][1]:
            print(f"Activity number {j} is done with start time = {sorted_activities[j][0]} and finish time = {sorted_activities[j][1]}")
            i = j

activities = [[5, 9], [1, 2], [3, 4], [0, 6], [5, 7], [8, 9]]
selected_activites(activities)

