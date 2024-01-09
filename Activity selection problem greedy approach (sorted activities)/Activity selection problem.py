def select_activities(s, f):
    i = 0
    print(f"Activity number {i} is done with start time = {s[i]} and finish time = {f[i]}!")
    for j in range(1, len(f)):
        if s[j] >= f[i]:
            print(f"Activity number {j} is done with start time = {s[j]} and finish time = {f[j]}!")
            i = j

s = [1, 3, 0, 5, 8, 5]
f = [2, 4, 6, 7, 9, 9]
select_activities(s, f)